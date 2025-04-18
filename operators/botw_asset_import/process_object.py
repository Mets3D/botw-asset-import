import bpy

from ...utils.timer import Timer
from ...utils.mesh import is_uvmap_all_zero, are_uv_maps_identical
from .names import rename_object
from .process_material import process_mat
from .constants import LEAF_ZFIGHT_HACK, GARBAGE_MATS

def process_obj(
        collection, 
        obj, 
        *,
        rename_ob_mat=False, 
        remove_redundant_armatures=True,
        remove_redundant_UVs=True,
        do_leaf_z_hack=False,
    ):
    if obj.type == 'ARMATURE':
        if obj.animation_data and obj.animation_data.action:
            obj.animation_data.action = None
        if remove_redundant_armatures and not is_armature_useful(obj):
            bpy.data.objects.remove(obj)
            return
    elif obj.type == 'MESH':
        if rename_ob_mat:
            rename_object(collection, obj)

        if remove_redundant_UVs:
            uvs_to_delete = []
            for i, uv_layer in enumerate(obj.data.uv_layers):
                if is_uvmap_all_zero(obj, i):
                    uvs_to_delete.append(uv_layer)
                elif i>0 and any([are_uv_maps_identical(obj, i, j) for j in range(i)]):
                    uvs_to_delete.append(uv_layer)
            for bad_uv in uvs_to_delete:
                obj.data.uv_layers.remove(bad_uv)

        if len(obj.vertex_groups) == 1 and 'Root' in obj.vertex_groups:
            obj.vertex_groups.clear()

        for mod in obj.modifiers:
            if mod.type == 'ARMATURE' and not mod.object:
                obj.modifiers.remove(mod)

        if do_leaf_z_hack:
            hack_zfighting_leaves(collection, obj)

        for uv_layer, name in zip(obj.data.uv_layers, ("Albedo", "SPM")):
            # NOTE: I shouldn't have force-named the UV maps by their "purpose" since it often isn't accurate. 
            # But it's kinda too late to fix now. Sorry!
            # Sometimes there's also a 3rd UV layer.
            uv_layer.name = name

        for i, mat in enumerate(obj.data.materials):
            if rename_ob_mat:
                new_name = mat.name
                if "Mt_" in mat.name:
                    new_name = mat.name.split("Mt_")[1]
                new_name = collection['asset_name'] + ": " + new_name
                if new_name != mat.name and new_name in bpy.data.materials:
                    # If the material with this name already exists, overwrite it.
                    # Since material names are unique (on this code path), 
                    # this should only happen when trying to delete and re-import an asset, 
                    # and forgetting to purge.
                    existing_mat = bpy.data.materials.get(new_name)
                    existing_mat.user_remap(mat)
                    bpy.data.materials.remove(existing_mat)
                mat.name = new_name

            with Timer("Setup material", mat.name):
                mat = process_mat(collection, obj, mat)
                if mat:
                    obj.data.materials[i] = mat
                set_object_color(obj)

    if obj:
        hide_obj_if_useless(obj)

    obj.data.name = obj.name
    return obj

def hide_obj_if_useless(obj):
    """Hide specific useless objects."""
    if obj.type != 'MESH':
        return
    hide = False
    if any([s in obj.name for s in GARBAGE_MATS]):
        hide = True
    for m in obj.data.materials:
        if any([s in m.name for s in GARBAGE_MATS]):
            hide = True

    obj.hide_viewport, obj.hide_render = hide, hide

def is_armature_useful(arm_ob) -> bool:
    """Returns True if it deforms any of its child objects and consists of 
    more than just a deforming root bone at the origin."""
    if len(arm_ob.data.bones) == 1 and abs(arm_ob.data.bones[0].head.length) < 0.00001:
        return False

    def_bones = [b.name for b in arm_ob.data.bones if b.use_deform]
    for child_ob in arm_ob.children_recursive:
        if hasattr(child_ob, 'vertex_groups'):
            if any([vg.name in def_bones for vg in child_ob.vertex_groups]):
                return True
    return False

def hack_zfighting_leaves(collection, obj):
    for filename, obname in LEAF_ZFIGHT_HACK:
        if collection['file_name'] == filename and obj['import_name'] == obname:
            obj.location.z = -0.025
            return

def set_object_color(obj):
    if obj.type != 'MESH':
        return
    if len(obj.data.materials) == 0:
        return
    mat = obj.data.materials[0]
    if mat:
        obj.color = obj.data.materials[0].diffuse_color
    obj.data.uv_layers.active_index = 0
