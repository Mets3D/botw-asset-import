import bpy, os
from bpy.props import EnumProperty
from .prefs import get_addon_prefs
from .io_anim_seanim.import_seanim import load_seanim

class SCENE_OT_import_batch_seanim(bpy.types.Operator):
    """Import .seanim files from the Animations folder specified in the preferences, for every BotW asset found in this scene"""
    bl_idname = "scene.import_batch_seanim"
    bl_label = "Auto-Import .seanim for all assets"
    bl_options = {'REGISTER', 'UNDO'}

    import_mode: EnumProperty(
        name="Import Mode",
        items=[
            ('SELECTED', 'Selected', 'Auto-import animations of selected armatures'),
            ('ALL', 'All', 'Auto-import animations of all visible armatures'),
        ])

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        anim_folder = get_addon_prefs(context).game_anims_folder
        objs = context.scene.objects if self.import_mode=='ALL' else context.selected_objects
        for rig in [r for r in objs if r.type=='ARMATURE']:
            asset_name = ""
            for child in rig.children_recursive:
                if 'dirname' in child:
                    asset_name = child['dirname']
                    break

            # TODO: context override might be better.
            bpy.context.view_layer.objects.active = rig
            rig.select_set(True)
            anim_name = asset_name + "_Animation"
            if not rig.visible_get() or not rig.select_get():
                print("Couldn't select rig: ", rig.name)
                continue
            for asset_anim_folder in (anim_folder+anim_name, anim_folder+asset_name):
                if not os.path.isdir(asset_anim_folder):
                    continue

                print("Asset anim folder found: ", asset_anim_folder)

                for entry in os.listdir(asset_anim_folder):
                    if not entry.endswith(".seanim"):
                        continue

                    if asset_name + ": " + entry.split(".")[0] in bpy.data.actions:
                        continue
                    fullpath = os.path.join(asset_anim_folder, entry)
                    print("Loading anim: ", fullpath)
                    action = load_seanim(context, filepath=fullpath)
                    action.name = asset_name + ": " + action.name
    
            if rig.animation_data:
                rig.animation_data.action = None
            for pb in rig.pose.bones:
                pb.matrix_basis.identity()

        return {'FINISHED'}

registry = [SCENE_OT_import_batch_seanim]