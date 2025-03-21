import bpy
from bpy.props import EnumProperty

class OBJECT_OT_armature_constrain(bpy.types.Operator):
    """Constrain matching bones of selected armatures to that of the active armature. Useful for applying appropriately rigged outfits."""

    bl_idname = "object.armature_outfit_constraint"
    bl_label = "Constrain Outfit Armature"
    bl_options = {'REGISTER', 'UNDO'}

    space: EnumProperty(
        name="Space", 
        items=[
            ('WORLD', 'World', "Copy the transforms of matching bones in world space"),
            ('LOCAL', 'Local', "Copy the transforms of matching bones in local space"),
        ])

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if not obj or obj.type != 'ARMATURE':
            cls.poll_message_set("No active armature to constrain to.")
            return False 
        selected_armatures = [a for a in context.selected_objects if a.type == 'ARMATURE']
        if len(selected_armatures) < 2:
            cls.poll_message_set("At least two armatures must be selected.")
            return False
        return True

    def execute(self, context):
        selected_armatures = [a for a in context.selected_objects if a.type == 'ARMATURE']
        active_arm = context.active_object
        counter = 0
        for arm in selected_armatures:
            if arm == active_arm:
                continue

            for pb in arm.pose.bones:
                if pb.name in active_arm.pose.bones:
                    # NOTE: Could check if the bone transforms are the same and otherwise throw at least a warning.
                    counter += 1
                    existing_con = next((con for con in pb.constraints if con.type == 'COPY_TRANSFORMS' and con.target == active_arm and con.subtarget == pb.name), None)
                    if not existing_con:
                        con = pb.constraints.new(type='COPY_TRANSFORMS')
                        con.target = active_arm
                        con.subtarget = pb.name
                        con.owner_space = con.target_space = self.space
                        if self.space == 'LOCAL' and pb.name == 'Skl_Root':
                            target_pb = active_arm.pose.bones.get(pb.name)
                            if target_pb:
                                con.influence = pb.bone.head.z / target_pb.bone.head.z

        self.report({'INFO'}, f"Constrained {counter}/{sum([len(a.pose.bones) for a in selected_armatures if a != active_arm])} bones.")
        return {'FINISHED'}

registry = [OBJECT_OT_armature_constrain]

def draw_armature_merge(self, context):
    if context.active_object and context.active_object.type == 'ARMATURE':
        self.layout.operator(OBJECT_OT_armature_constrain.bl_idname)

def register():
    bpy.types.VIEW3D_MT_object_constraints.append(draw_armature_merge)

def unregister():
    bpy.types.VIEW3D_MT_object_constraints.remove(draw_armature_merge)
