import bpy, os
from bpy.props import EnumProperty, BoolProperty, StringProperty
from .prefs import get_addon_prefs
from .io_anim_seanim.import_seanim import load_seanim, remove_redundant_keyframes
from .asset_names import asset_names
from math import pi

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
    fix_root: BoolProperty(
        name="Fix Root Animation",
        description="Fix the root being rotated by 90 degrees using baking and shennanigans",
        default=True
    )

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        anim_folder = get_addon_prefs(context).game_anims_folder
        objs = context.scene.objects if self.import_mode=='ALL' else context.selected_objects
        for rig in [r for r in objs if r.type=='ARMATURE']:
            dir_names = set()
            for child in rig.children_recursive:
                if 'dirname' in child:
                    dir_names.add(child['dirname'])

            # TODO: context override might be better. (it never is)
            context.view_layer.objects.active = rig
            rig.select_set(True)
            if not rig.visible_get() or not rig.select_get():
                print("Couldn't select rig: ", rig.name)
                continue
            actions = []
            for dir_name in dir_names:
                anim_name = dir_name + "_Animation"
                asset_name = asset_names.get(dir_name, dir_name)
                another_name = dir_name.rsplit("_", 1)[0] + "_Animation"
                for dirname in (anim_name, dir_name, another_name):
                    asset_anim_folder = anim_folder+dirname
                    if not os.path.isdir(asset_anim_folder):
                        continue

                    print("Asset anim folder found: ", asset_anim_folder)

                    for entry in os.listdir(asset_anim_folder):
                        if not entry.endswith(".seanim"):
                            continue

                        existing_action = bpy.data.actions.get(asset_name + ": " + entry.split(".")[0])
                        if existing_action:
                            actions.append(existing_action)
                            continue
                        fullpath = os.path.join(asset_anim_folder, entry)
                        print("Loading anim: ", fullpath)
                        action = load_seanim(context, filepath=fullpath)
                        action.name = asset_name + ": " + action.name
                        action.asset_mark()
                        actions.append(action)

            bpy.ops.object.mode_set(mode='OBJECT')

            if self.fix_root:
                for action in actions:
                    action.slots[0].name_display = rig.name
                fix_root_motion_with_baking(context, rig, actions)

            if rig.animation_data:
                rig.animation_data.action = None
            for pb in rig.pose.bones:
                pb.matrix_basis.identity()

        return {'FINISHED'}


class SCENE_OT_fix_botw_anims(bpy.types.Operator):
    """Fix BotW animation roots using baking and shennanigans"""
    bl_idname = "scene.fix_botw_anims"
    bl_label = "Fix BotW Animations"
    bl_options = {'REGISTER', 'UNDO'}

    action_prefix: StringProperty(name="Action Prefix", description="Operate on actions whose name starts with this string")
    do_slot_rename: BoolProperty(name="Rename Default Slot", default=False)
    slot_name: StringProperty(name="Slot Name", description="Set the first slot of each matching action to this string")
    do_root_fix: BoolProperty(name="Fix Root Rotation", description="Fix the Root bone's 90 degree rotation using some constraints and baking", default=True)

    @classmethod
    def poll(cls, context):
        return context.active_object and context.active_object.type == 'ARMATURE'

    def invoke(self, context, _event):
        rig = context.active_object
        for child in rig.children_recursive:
            if 'asset_name' in child:
                self.action_prefix = child['asset_name'] + ":"
                break
            if 'dirname' in child:
                self.action_prefix = asset_names.get(child['dirname'] + ":", "")
                break
        self.slot_name = context.active_object.name
        return context.window_manager.invoke_props_dialog(self)

    def get_actions(self):
        return [a for a in bpy.data.actions if a.name.startswith(self.action_prefix)]

    def draw(self, context):
        self.layout.prop(self, 'action_prefix')
        self.layout.label(text=f"Found {len(self.get_actions())} actions to fix")
        self.layout.prop(self, 'do_root_fix')
        self.layout.prop(self, 'do_slot_rename')
        if self.do_slot_rename:
            self.layout.prop(self, 'slot_name')

    def execute(self, context):
        actions = self.get_actions()
        if self.do_slot_rename:
            for action in actions:
                action.slots[0].name_display = self.slot_name
        if self.do_root_fix:
            fix_root_motion_with_baking(context, context.active_object, actions)
        return {'FINISHED'}


def fix_root_motion_with_baking(context, rig, actions):
    """Animations import with a root bone rotation of 90 degrees, and I couldn't figure out the math for fixing the fcurves, and this feels safer."""
    assert rig.visible_get()
    assert "Root" in rig.pose.bones
    assert rig.library == None # Override is supported, linked is not.

    bpy.ops.object.select_all(action='DESELECT')

    rig.select_set(True)
    context.view_layer.objects.active = rig
    rig.animation_data_create()
    rig.animation_data.action = None
    for pb in rig.pose.bones:
        pb.matrix_basis.identity()

    bpy.ops.object.duplicate()
    rig_clone = context.active_object
    if rig_clone.library or rig_clone.override_library:
        rig_clone.make_local()
    if rig_clone.data.library:
        old_data = rig_clone.data
        old_data.make_local()
        rig.data = old_data
    bpy.ops.object.mode_set(mode='EDIT')
    eb = rig_clone.data.edit_bones.new("Root Rotation Fixer")
    root_eb = rig_clone.data.edit_bones["Root"]
    eb.head = root_eb.head.copy()
    eb.tail = root_eb.tail.copy()
    eb.roll = root_eb.roll
    eb.parent = root_eb
    for child_eb in root_eb.children:
        child_eb.parent = eb

    bpy.ops.object.mode_set(mode='OBJECT')

    root_pb = rig.pose.bones["Root"]
    helper_pb = rig_clone.pose.bones["Root Rotation Fixer"]

    empty = bpy.data.objects.new("Empty", object_data=None)    # Has to have a target to be evaluated, meh...
    for pb, xrot in zip((rig_clone.pose.bones["Root"], helper_pb), (-pi/2, pi/2)):
        con = pb.constraints.new(type='TRANSFORM')
        con.target = empty
        con.target_space = con.owner_space = 'LOCAL'
        con.map_to = 'ROTATION'
        con.to_min_x_rot = xrot

    for b in rig.data.bones:
        b.hide = False
        b.select = False

    for copier_pb in [root_pb] + list(root_pb.children):
        con = copier_pb.constraints.new(type='COPY_TRANSFORMS')
        con.target = rig_clone
        con.subtarget = copier_pb.name
        copier_pb.bone.select = True

    rig_clone.select_set(False)
    rig.select_set(True)
    context.view_layer.objects.active = rig
    context.view_layer.update()
    bpy.ops.object.mode_set(mode='POSE')

    for action in actions:
        if action.name.startswith("Face") or action.name.split(": ")[1].startswith("Face"):
            bad_curves = [fc for fc in action.fcurves if "Root" in fc.data_path]
            print("Removing root keyframes from face anim: ", action.name)
            for fc in bad_curves:
                action.fcurves.remove(fc)
            continue

        print("Fixing root rotation: ", action.name)
        for rig in (rig_clone, rig):
            for pb in rig.pose.bones:
                pb.matrix_basis.identity()

        rig.animation_data.action = action
        rig.animation_data.action_slot = rig.animation_data.action_suitable_slots[0]
        rig_clone.animation_data.action = action
        rig_clone.animation_data.action_slot = rig.animation_data.action_suitable_slots[0]
        start, end = action.curve_frame_range
        bpy.ops.nla.bake(frame_start=max(0, int(start)), frame_end=int(end)+1, only_selected=True, visual_keying=True, clear_constraints=action==actions[-1], clear_parents=False, use_current_action=True, clean_curves=True, bake_types={'POSE'}, channel_types={'LOCATION', 'ROTATION'})
        remove_redundant_keyframes(action)

    bpy.ops.object.mode_set(mode='OBJECT')

    rig.animation_data.action = None
    for pb in rig.pose.bones:
        pb.matrix_basis.identity()

    bpy.data.objects.remove(rig_clone)
    bpy.data.objects.remove(empty)

registry = [
    SCENE_OT_import_batch_seanim, 
    SCENE_OT_fix_botw_anims
]
