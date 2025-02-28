import bpy, os
from .op_focus_asset import focus_action, focus_collections
from bpy.props import BoolProperty
from .botw_batch_fbx_import import PixelImage

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
        return asset_thumbnail_from_viewport(context, context.id, self)

class ASSET_OT_batch_thumbnail_from_viewport(bpy.types.Operator):
    """Create an asset preview from a viewport render for all selected assets."""

    bl_idname = "asset.batch_thumbnail_from_viewport"
    bl_label = "Batch Thumbnail From Viewport"
    bl_options = {'REGISTER', 'UNDO'}

    focus_each: BoolProperty(name="Focus Each", default=True, description="Focus the viewport on each asset before making the preview render.")

    @classmethod
    def poll(cls, context):
        if hasattr(context, 'id'):
            return bool(context.id)

    def execute(self, context):
        for id in context.selected_ids[:]:
            if type(id) == bpy.types.Action:
                if self.focus_each:
                    context.scene.frame_current = int(id.curve_frame_range.length/2)
                result = focus_action(context, id, self.focus_each)
                if result == {'CANCELLED'}:
                    # This can happen is the rig is not visible.
                    continue
            elif type(id) == bpy.types.Collection:
                if self.focus_each:
                    focus_collections(context, [id], self.focus_each, self)

            asset_thumbnail_from_viewport(context, id, self)

        return {'FINISHED'}

class ASSET_OT_crop_asset_thumbnails(bpy.types.Operator):
    """Create an asset preview from a viewport render for all selected assets."""

    bl_idname = "asset.crop_asset_thumbnails"
    bl_label = "Crop Asset Thumbnails"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.selected_ids:
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

def crop_asset_preview(id):
    if not id.preview:
        return
    pixel_img = PixelImage(id.preview.image_size[0], id.preview.image_size[1], id.preview.image_pixels_float[:])
    pixel_img.crop_to_square_content()
    pixel_img.downscale_to_fit()
    id.preview.image_size = pixel_img.width, pixel_img.height
    print("width: ", pixel_img.width, "height: ", pixel_img.height, "pixels: ", len(pixel_img.pixels))
    id.preview.image_pixels_float = pixel_img.pixels

def asset_thumbnail_from_viewport(context, id, operator=None):
    overlays_bkp = True
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            overlays_bkp = area.spaces.active.overlay.show_overlays
            area.spaces.active.overlay.show_overlays = False
            break
    bpy.ops.render.opengl()
    area.spaces.active.overlay.show_overlays = overlays_bkp
    render_result = next(image for image in bpy.data.images if image.type == "RENDER_RESULT")
    if not render_result:
        if operator:
            operator.report({'ERROR'}, "Couldn't find Render Result image.")
        return {'CANCELLED'}

    filepath = os.path.join(bpy.app.tempdir, "asset_preview.png")
    render_result.save_render(filepath)
    temp_img = bpy.data.images.load(filepath)
    pixel_img = PixelImage.from_blender_image(temp_img)
    pixel_img.crop_to_square_content()
    pixel_img.downscale_to_fit()
    if not id.preview:
        id.preview_ensure()
    id.preview.image_size = pixel_img.width, pixel_img.height
    id.preview.image_pixels_float = pixel_img.pixels
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