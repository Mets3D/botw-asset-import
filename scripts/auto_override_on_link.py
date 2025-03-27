# This script makes it so that when you link a collection with any armatures,
# it automatically gets overridden.
# This functionality will not persist when opening another .blend file.
# Only works while this script is present.

import bpy

def auto_override_on_link(lapp_context):
    if 'LINK' not in lapp_context.options:
        return
    context = bpy.context
    context.scene['active_object'] = context.active_object

    for item in lapp_context.import_items:
        id = item.id
        if id.id_type == 'COLLECTION' and item.import_info == set():
            override_hierarchy = id.override_hierarchy_create(context.scene, context.view_layer)
            armatures = [obj for obj in override_hierarchy.all_objects if obj.type == 'ARMATURE']
            context.scene['override_armatures'] = armatures
            for arm_ob in armatures:
                arm_ob.override_library.is_system_override = False

    bpy.app.handlers.depsgraph_update_post.append(delete_instancer_empty)

def constrain_armatures(context, slaves, master, space='WORLD'):
    if not slaves or not master:
        return
    slaves = [s for s in slaves if s.type == 'ARMATURE']
    if master.type != 'ARMATURE':
        return
    for arm in slaves:
        if arm == master:
            continue
        arm.select_set(False)

        for pb in arm.pose.bones:
            if pb.name in master.pose.bones:
                existing_con = next((con for con in pb.constraints if con.type == 'COPY_TRANSFORMS' and con.target == master and con.subtarget == pb.name), None)
                if not existing_con:
                    con = pb.constraints.new(type='COPY_TRANSFORMS')
                    con.target = master
                    con.subtarget = pb.name
                    con.owner_space = con.target_space = space
                    if space == 'LOCAL' and pb.name == 'Skl_Root':
                        target_pb = master.pose.bones.get(pb.name)
                        if target_pb:
                            con.influence = pb.bone.head.z / target_pb.bone.head.z
                pb.bone.hide = True

    master.select_set(True)
    context.view_layer.objects.active = master

def delete_instancer_empty(scene, depsgraph):
    context = bpy.context
    bpy.data.objects.remove(context.active_object)
    override_armatures = scene.get('override_armatures')
    if override_armatures:
        for arm_ob in scene['override_armatures']:
            arm_ob.select_set(True)
        if len(scene.view_layers) == 1:
            scene.view_layers[0].objects.active = arm_ob
        constrain_armatures(context, override_armatures, scene.get('active_object'))
        del scene['active_object']
        del scene['override_armatures']
    bpy.app.handlers.depsgraph_update_post.remove(delete_instancer_empty)

def register():
    bpy.app.handlers.blend_import_post.append(auto_override_on_link)

def unregister():
    bpy.app.handlers.blend_import_post.remove(auto_override_on_link)

register()