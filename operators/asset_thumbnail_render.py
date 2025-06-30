import bpy, os
from .asset_focus import focus_action, focus_collections, focus_view_on_objects
from bpy.props import BoolProperty
from ..utils.pixel_image import PixelImage
from ..utils.progressbar import ProgressBar
from ..utils.timer import Timer

class ASSET_OT_thumbnail_from_viewport(bpy.types.Operator):
    """Create an asset preview from a viewport render."""

    bl_idname = "asset.thumbnail_from_viewport"
    bl_label = "Thumbnail From Viewport"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context, 'id'):
            return bool(context.id)

    def execute(self, context):
        org_res = context.scene.render.resolution_x, context.scene.render.resolution_y
        org_transparent = context.scene.render.film_transparent
        org_format = context.scene.render.image_settings.file_format
        org_png_format = context.scene.render.image_settings.color_mode
        org_png_depth = context.scene.render.image_settings.color_depth
        ret = asset_thumbnail_from_viewport(context, context.id, self)
        context.scene.render.film_transparent = org_transparent
        context.scene.render.resolution_x, context.scene.render.resolution_y = org_res
        context.scene.render.image_settings.file_format = org_format
        context.scene.render.image_settings.color_mode = org_png_format
        context.scene.render.image_settings.color_depth = org_png_depth
        return ret

class ASSET_OT_batch_thumbnail_from_viewport(bpy.types.Operator):
    """Create an asset preview from a viewport render for all selected assets."""

    bl_idname = "asset.batch_thumbnail_from_viewport"
    bl_label = "Batch Thumbnail From Viewport"
    bl_options = {'REGISTER', 'UNDO'}

    focus_each: BoolProperty(name="Focus Each", default=True, description="Focus the viewport on each asset before making the preview render.")
    use_progress_bar: BoolProperty(name="Show Progress", description="Drawing a progress bar requires re-drawing the entire UI, which slows down the process by about 10%", default=True)

    @classmethod
    def poll(cls, context):
        if hasattr(context, 'id'):
            return bool(context.id)

    def modal(self, context, event):
        with Timer("Thumbnail everything"):
            self.pb.update(context, self.index)
            result = self.render_thumbnail(context, self.ids[self.index])
            if result == {'CANCELLED'}:
                self.report({'ERROR'}, "Failed to render thumbnail. (For Actions, select an Armature)")
                return result
            self.index += 1
            
            if self.index > len(self.ids)-1:
                self.reset_output_props(context)
                self.pb.destroy()
                Timer.summarize()
                return {'FINISHED'}
            else:
                return {'PASS_THROUGH'}

    def invoke(self, context, event):
        self.org_res = context.scene.render.resolution_x, context.scene.render.resolution_y
        self.org_transparent = context.scene.render.film_transparent
        self.org_format = context.scene.render.image_settings.file_format
        self.org_png_format = context.scene.render.image_settings.color_mode
        self.org_png_depth = context.scene.render.image_settings.color_depth
        
        context.scene.render.film_transparent = True
        context.scene.render.resolution_x, context.scene.render.resolution_y = 512, 512
        context.scene.render.image_settings.file_format = 'PNG'
        context.scene.render.image_settings.color_mode = 'RGBA'
        context.scene.render.image_settings.color_depth = '8'

        if not self.use_progress_bar:
            return self.execute(context)
        self.pb = ProgressBar(len(context.selected_ids), menu=bpy.types.ASSETBROWSER_MT_editor_menus)
        context.window_manager.modal_handler_add(self)
        self.ids = context.selected_ids[:]
        self.index = 0

        return {'RUNNING_MODAL'}

    def execute(self, context):
        total = len(context.selected_ids)
        for i, id in enumerate(context.selected_ids):
            print(f"Thumbnail {i}/{total}")
            result = self.render_thumbnail(context, id)
            if result == {'CANCELLED'}:
                self.report({'ERROR'}, "Failed to generate preview for " + id.name)

        self.reset_output_props(context)
        return {'FINISHED'}

    def render_thumbnail(self, context, id):
        if type(id) == bpy.types.Action:
            if self.focus_each:
                context.scene.frame_current = int(id.curve_frame_range.length/2)
            result = focus_action(context, id, self.focus_each)
            if result == {'CANCELLED'}:
                # This can happen is the rig is not visible.
                return result
        elif type(id) == bpy.types.Collection:
            if self.focus_each:
                with Timer("Focus collections"):
                    focus_collections(context, [id], focus_view=self.focus_each, operator=self)
        elif type(id) == bpy.types.Object:
            if self.focus_each:
                focus_view_on_objects(context, [id])

        with Timer("Thumnail render"):
            asset_thumbnail_from_viewport(context, id)

    def reset_output_props(self, context):
        context.scene.render.film_transparent = self.org_transparent
        context.scene.render.resolution_x, context.scene.render.resolution_y = self.org_res
        context.scene.render.image_settings.file_format = self.org_format
        context.scene.render.image_settings.color_mode = self.org_png_format
        context.scene.render.image_settings.color_depth = self.org_png_depth

class ASSET_OT_crop_asset_thumbnails(bpy.types.Operator):
    """Create an asset preview from a viewport render for all selected assets."""

    bl_idname = "asset.crop_asset_thumbnails"
    bl_label = "Crop Asset Thumbnails"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not hasattr(context, 'selected_ids') or not context.selected_ids:
            cls.poll_message_set("No selected assets.")
            return False
        return True

    def execute(self, context):
        for id in context.selected_ids:
            crop_asset_preview(id)
        # Making any modification to any image datablock fires an update
        # which we need for the new asset previews to actually show up, lol.
        # Couldn't find any other way to trigger this update.
        if bpy.data.images:
            bpy.data.images[0].name = bpy.data.images[0].name
        return {'FINISHED'}

def crop_asset_preview(id) -> bool:
    if not id.preview:
        return False
    pixel_img = PixelImage.from_pixels(id.preview.image_size[0], id.preview.image_size[1], id.preview.image_pixels_float[:])
    success = pixel_img.crop_to_square_content()
    pixel_img.downscale_to_fit()
    id.preview.image_size = pixel_img.width, pixel_img.height
    id.preview.image_pixels_float = pixel_img.pixels
    return success

def asset_thumbnail_from_viewport(context, id, operator=None, change_output_settings=False):
    overlays_bkp = True

    show_overlays = False
    if type(id) == bpy.types.Object:
        if id.type=='MESH' and len(id.data.polygons)==0:
            # Mesh with no faces: enable overlays
            show_overlays = True
        elif id.type not in ('MESH', 'CURVE', 'CURVES', 'GREASEPENCIL', 'POINTCLOUD', 'META'):
            # Non-visible object type: enable overlays
            show_overlays = True

    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            overlays_bkp = area.spaces.active.overlay.show_overlays
            area.spaces.active.overlay.show_overlays = show_overlays
            break
    with Timer("OpenGL Render"):

        if change_output_settings:
            context.scene.render.film_transparent = True
            context.scene.render.resolution_x, context.scene.render.resolution_y = 512, 512
            context.scene.render.image_settings.file_format = 'PNG'
            context.scene.render.image_settings.color_mode = 'RGBA'
            context.scene.render.image_settings.color_depth = '8'

        bpy.ops.render.opengl()
    area.spaces.active.overlay.show_overlays = overlays_bkp
    render_result = next(image for image in bpy.data.images if image.type == "RENDER_RESULT")
    if not render_result:
        if operator:
            operator.report({'ERROR'}, "Couldn't find Render Result image.")
        return {'CANCELLED'}

    with Timer("Process Thumbnail"):
        filepath = os.path.join(bpy.app.tempdir, "asset_preview.png")
        render_result.save_render(filepath)
        temp_img = bpy.data.images.load(filepath)
        pixel_img = PixelImage.from_blender_image(temp_img, ignore_cache=True)
        pixel_img.crop_to_square_content()
        pixel_img.downscale_to_fit()
        if not id.preview:
            id.preview_ensure()
        id.preview.image_size = [min(256, pixel_img.width), min(256, pixel_img.height)]
        try:
            id.preview.image_pixels_float = pixel_img.pixels
        except ValueError as exc:
            print("Failed to assign image: ", exc)
        bpy.data.images.remove(temp_img)

    if operator:
        operator.report({'INFO'}, "Success.")
    return {'FINISHED'}

def draw_menu(self, context):
    self.layout.operator(ASSET_OT_thumbnail_from_viewport.bl_idname)
    self.layout.operator(ASSET_OT_batch_thumbnail_from_viewport.bl_idname)
    self.layout.operator(ASSET_OT_crop_asset_thumbnails.bl_idname)

registry = [
    ASSET_OT_thumbnail_from_viewport,
    ASSET_OT_batch_thumbnail_from_viewport,
    ASSET_OT_crop_asset_thumbnails,
]

def register():
    bpy.types.ASSETBROWSER_MT_metadata_preview_menu.append(draw_menu)

def unregister():
    bpy.types.ASSETBROWSER_MT_metadata_preview_menu.remove(draw_menu)