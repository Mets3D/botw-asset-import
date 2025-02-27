import bpy, os

class ASSETBROWSER_OT_viewport_render_asset_thumbnail(bpy.types.Operator):
    """Create an asset preview from a viewport render."""

    bl_idname = "asset.thumbnail_from_viewport"
    bl_label = "Viewport Render Asset Thumbnail"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if hasattr(context, 'id'):
            return bool(context.id)

    def execute(self, context):
        id = context.id
        bpy.ops.ed.lib_id_generate_preview()
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
            self.report({'ERROR'}, "Couldn't find Render Result image.")
            return {'CANCELLED'}

        filepath = os.path.join(bpy.app.tempdir, "asset_preview.png")
        render_result.save_render(filepath)
        temp_img = bpy.data.images.load(filepath)
        id.preview.image_size = context.scene.render.resolution_x, context.scene.render.resolution_y
        id.preview.image_pixels_float = temp_img.pixels[:]
        bpy.data.images.remove(temp_img)

        self.report({'INFO'}, "Success.")
        return {'FINISHED'}

def draw_menu(self, context):
    self.layout.operator(ASSETBROWSER_OT_viewport_render_asset_thumbnail.bl_idname)

registry = [ASSETBROWSER_OT_viewport_render_asset_thumbnail]

def register():
    bpy.types.ASSETBROWSER_MT_metadata_preview_menu.append(draw_menu)

def unregister():
    bpy.types.ASSETBROWSER_MT_metadata_preview_menu.remove(draw_menu)