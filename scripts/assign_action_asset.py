# This script adds an operator called "Assign Action" in the Asset Browser's context menu.
# This operator assigns a selected Action asset to the active armature.

import bpy

class ASSETBROWSER_OT_assign_action(bpy.types.Operator):
    """Assign an Action asset to the active armature"""

    bl_idname = "asset.assign_action"
    bl_label = "Assign Action Asset"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context.area.ui_type == 'ASSETS':
            return False
        if not context.asset or context.asset.id_type != 'ACTION':
            cls.poll_message_set("Active asset is not an Action.")
            return False
        if not context.active_object or context.active_object.type != 'ARMATURE':
            cls.poll_message_set("Active object is not an Armature.")
            return False
        return True

    def execute(self, context):
        asset = context.asset
        action = None
        if context.id and type(context.id) == bpy.types.Action:
            action = context.id
        elif asset and hasattr(asset, 'id_type') and asset.id_type == 'ACTION':
            import_method = context.area.spaces.active.params.import_method
            if import_method == 'FOLLOW_PREFS':
                asset_library = get_asset_library(context, asset)
                if asset_library:
                    import_method = asset_library.import_method
                else:
                    # This is only if asset_library is None, which should never happen.
                    import_method = 'APPEND'
            link = import_method == 'LINK'
            action = get_or_import_action(asset.name, asset.full_library_path, link=link)

        if not action:
            return {'CANCELLED'}

        rig = context.active_object
        if not rig.animation_data:
            rig.animation_data_create()

        for pb in rig.pose.bones:
            pb.matrix_basis.identity()

        rig.animation_data.action = action
        rig.animation_data.action_slot = rig.animation_data.action_suitable_slots[0]
        context.scene.frame_start = int(action.curve_frame_range.x)
        context.scene.frame_end = int(action.curve_frame_range.y)
        
        self.report({'INFO'}, f"Assign Action: {asset.name}")
        return {'FINISHED'}


def get_or_import_action(action_name, library_path, link=False):
    if action_name in bpy.data.actions:
        return bpy.data.actions[action_name]

    with bpy.data.libraries.load(library_path, relative=True, link=link) as (data_from, data_to):
        if action_name in data_from.actions:
            data_to.actions.append(action_name)

    return bpy.data.actions.get(action_name)


def get_asset_library(context, asset):
     for asset_library in context.preferences.filepaths.asset_libraries:
          if asset.full_library_path.startswith(asset_library.path):
               return asset_library


def draw_assign_action(self, context):
    self.layout.operator(ASSETBROWSER_OT_assign_action.bl_idname)


def register():
    bpy.utils.register_class(ASSETBROWSER_OT_assign_action)
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_assign_action)

def unregister():
    bpy.utils.unregister_class(ASSETBROWSER_OT_assign_action)
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_assign_action)

# register()