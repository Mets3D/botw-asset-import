import bpy
from bpy.props import StringProperty

class ASSETBROWSER_OT_rename_asset(bpy.types.Operator):
    """Rename the active asset, if it is local."""

    bl_idname = "asset.rename"
    bl_label = "Rename Asset"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.id if hasattr(context, 'id') else False

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        row = self.layout.row()
        row.activate_init = True
        row.prop(context.id, 'name')

    def execute(self, context):
        return {'FINISHED'}

registry = [ASSETBROWSER_OT_rename_asset]
