import bpy


class OBJECT_OT_armature_merge_outfit(bpy.types.Operator):
    """Merge armatures into one by merging shared bones."""

    bl_idname = "object.armature_merge_outfit"
    bl_label = "Merge Outfit Armatures"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type != 'ARMATURE':
                obj.select_set(False)
        
        for obj in context.selected_objects:
            for bone in obj.data.bones:
                bone['parent'] = bone.parent.name if bone.parent else ""
                bone['name'] = bone.name

        bpy.ops.object.join()
        bpy.ops.object.mode_set(mode='EDIT')

        for obj in context.selected_objects:
            for ebone in obj.data.edit_bones:
                bone = obj.data.bones[ebone.name]
                if bone.name != bone['name']:
                    other_ebone = obj.data.edit_bones[bone['name']]
                    ebone.parent = other_ebone
                    if not other_ebone.parent and bone['parent']:
                        parent_ebone = obj.data.edit_bones[bone['parent']]
                        other_ebone.parent = parent_ebone
                    obj.data.edit_bones.remove(ebone)

        for child in obj.children_recursive:
            for m in child.modifiers:
                if m.type == 'ARMATURE' and not m.object:
                    m.object = obj

        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

registry = [OBJECT_OT_armature_merge_outfit]

def draw_armature_merge(self, context):
    if context.active_object and context.active_object.type == 'ARMATURE':
        self.layout.operator(OBJECT_OT_armature_merge_outfit.bl_idname)

def register():
    bpy.types.VIEW3D_MT_object.append(draw_armature_merge)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(draw_armature_merge)
