import bpy, os, re, glob
from bpy.props import BoolProperty, StringProperty
from math import pi

from mathutils import Vector, Euler
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from ...databases.asset_names import asset_names
from ...utils.collections import ensure_collection, set_active_collection
from ...utils.resources import ensure_widget, ensure_lib_datablock
from ...prefs import get_addon_prefs
from ...utils.material import deduplicate_materials, refresh_images
from ...utils.timer import Timer
from ...utils.pixel_image import PixelImage
from ...utils.dae_fixer import fix_dae_uvmaps_in_place
from ...utils.mesh import is_uvmap_all_zero, are_uv_maps_identical

# This is just here to make Reload Scripts work... at least when I run it twice...?
from . import constants, process_material
modules = [constants, process_material]

from .process_material import process_mat
from .constants import ICON_EXTENSION, OBJ_PREFIXES, PRIMITIVE_NAMES, GARBAGE_MATS, LEAF_ZFIGHT_HACK, ensure_caches

PRINT_LATER = []

def print_later(*msg):
    PRINT_LATER.append("".join([str(m) for m in msg]))

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all .dae & .fbx files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW .dae + .fbx"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE', 'HIDDEN'})

    rename_collections: BoolProperty(name="Rename Collections", description="Rename collections to their asset name.", default=True)
    rename_ob_mat: BoolProperty(name="Rename Objects & Materials", description="Prepend asset name to object and material names, and remove garbage strings. Useful when importing many assets into a single file to keep names unique, but can also result in exceeding the 63-character limit (those cases will not be renamed.).", default=True)

    apply_transforms: BoolProperty(name="Apply Transforms", description="Necessary for wind shader effects to work, and in some cases also necessary for correct armature replacement from .fbx files if you have them.", default=True)
    remove_redundant_armatures: BoolProperty(name="Remove Redundant Armatures", description="If an armature has only 1 bone and it's at the world origin, or if it doesn't deform any objects with any of its bones, remove it", default=True)
    remove_redundant_UVs: BoolProperty(name="Remove Redundant UVs", description="If a UVMap is the same as a previous one, or if it's empty, remove it", default=True)

    create_parent_collections: BoolProperty(name="Create Parent Collections", description="When a directory has more than 1 file, create a parent collection that represents that directory", default=True)

    deduplicate_materials: BoolProperty(name="Deduplicate Materials", description="If two materials end up with identical nodetrees, merge them into one", default=True)

    force_update_caches: BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'rename_collections')
        layout.prop(self, 'rename_ob_mat')
        layout.separator()

        layout.prop(self, 'create_parent_collections')
        layout.separator()

        layout.prop(self, 'apply_transforms')
        if self.apply_transforms:
            layout.prop(self, 'remove_redundant_armatures')
        layout.separator()

        layout.prop(self, 'deduplicate_materials')

    def execute(self, context):
        global PRINT_LATER
        PRINT_LATER = []

        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

        any_dae_files = dae_files = glob.glob(f"{self.directory}/**/*.dae", recursive=True)
        if not any_dae_files:
            self.report({'WARNING'}, "No .dae files were found anywhere in this folder or its sub-folders.")
            return {'CANCELLED'}

        # Ensure dependent settings aren't enabled without their dependency.
        if not self.apply_transforms:
            self.remove_redundant_armatures = False

        with Timer("Load caches"):
            ensure_caches(self.force_update_caches)

        ensure_botw_scene_settings(context)

        root_dir_name = self.directory.split(os.sep)[-2]

        counter = 0
        imported_objects = []
        for root, _subdirs, files in os.walk(self.directory):
            dae_files = [f for f in files if f.lower().endswith(".dae") and "Fxmdl" not in f]
            parent_coll = None
            dirname = root.split(os.sep)[-1]
            if dirname.endswith("_Far") or dirname.endswith("_Animation"):
                # These are LOD meshes, we don't want those.
                continue
            if len(dae_files) > 1 and self.create_parent_collections:
                parent_coll_name = root.split(os.sep)[-1]
                if root_dir_name != parent_coll_name:
                    parent_coll_name = asset_names.get(parent_coll_name, parent_coll_name)
                    parent_coll = ensure_collection(context, parent_coll_name)

            for dae_name in dae_files:

                full_path = os.path.join(root, dae_name)
                with Timer("Full Import", dae_name):
                    imported_coll = import_and_process_dae(
                        context, 
                        full_path, 
                        parent_coll, 
                        rename_objects=self.rename_ob_mat, 
                        apply_transforms=self.apply_transforms,
                        remove_redundant_armatures=self.remove_redundant_armatures,
                        remove_redundant_UVs=self.remove_redundant_UVs,
                    )
                    imported_objects += imported_coll.all_objects
                    if self.rename_collections:
                        imported_coll.name = imported_coll['asset_name']
            counter += 1

        for lateprint in PRINT_LATER:
            print(lateprint)

        if self.deduplicate_materials:
            deduplicate_materials(imported_objects)
        bpy.ops.outliner.orphans_purge()
        refresh_images()

        # Dump cache, in case the garbage collector doesn't. (it should, but this makes extra sure.)
        PixelImage.cache = {}
        Timer.summarize()

        return {'FINISHED'}

def derive_asset_name(dae_filename: str, dirname: str, remove_prefixes=True) -> str:
    without_ext = dae_filename.replace(".dae", "")
    asset_name = asset_names.get(without_ext, without_ext)

    # If the asset name wasn't in the dictionary, try without any _A, _B suffixes.
    if asset_name == without_ext and (without_ext.endswith("_A") or without_ext.endswith("_B")):
        asset_name = asset_names.get(without_ext[:-2], without_ext[:-2])

    # Guess Weapon sheaths based on the entries for weapons in the dictionary.
    for find, replace in (("Lsheath", "Lsword"), ("SpearSheath", "Spear"), ("Sheath", "Sword")):
        if asset_name == without_ext and find in asset_name:
            weapon_name = asset_names.get(asset_name.replace(find, replace))
            if weapon_name:
                asset_name = weapon_name + " Sheath"
                break

    # Make the "Enemy_" prefix optional in the dictionary.
    if asset_name == without_ext and "Enemy" in asset_name:
        asset_name = asset_names.get(asset_name.replace("Enemy_", ""), asset_name)

    if not remove_prefixes:
        return asset_name

    return tidy_name(asset_name)

def ensure_botw_scene_settings(context):
    # Zelda shaders absolutely depend on EEVEE.
    context.scene.render.engine = 'BLENDER_EEVEE_NEXT'

    # Set sRGB view transform, as that's what the game probably uses.
    context.scene.view_settings.view_transform = 'Standard'

    # Set some settings that make things prettier. (and more expensive of course)
    context.scene.eevee.use_shadow_jitter_viewport = True
    context.scene.eevee.use_raytracing = True
    context.scene.eevee.ray_tracing_options.resolution_scale = '16'

    if context.scene.world:
        context.scene.world.use_fake_user = True
    context.scene.world = ensure_world_and_lights(context)

    if not context.scene.use_nodes:
        # Enable compositing nodes.
        context.scene.use_nodes = True
        nodetree = context.scene.node_tree
        nodes = nodetree.nodes
        links = nodetree.links
        # Add a Bloom node at the end of the compositing node tree.
        output_node = nodes['Composite']
        previous_socket = output_node.inputs[0].links[0].from_socket
        bloom_node = nodes.new("CompositorNodeGlare")
        bloom_node.glare_type = 'BLOOM'
        bloom_node.quality = 'HIGH'
        bloom_node.inputs['Size'].default_value = 0.15
        bloom_node.inputs['Strength'].default_value = 2.0
        links.new(previous_socket, bloom_node.inputs['Image'])
        links.new(bloom_node.outputs['Image'], output_node.inputs['Image'])

    # Set viewport shading to the BotW MatCap.
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.shading.type = 'SOLID'
            area.spaces.active.shading.light = 'MATCAP'
            area.spaces.active.shading.studio_light = 'botw.exr'
            area.spaces.active.shading.color_type = 'TEXTURE'
            # Enable viewport compositing for bloom.
            area.spaces.active.shading.use_compositor = 'ALWAYS'

def ensure_world_and_lights(context) -> bpy.types.World:
    """Append BotW world from resources.blend, important for its custom properties
    and drivers. This also brings special lights, hooked up to said properties.
    These properties are then referenced by the shaders via Attribute nodes.
    This way of referencing world properties is 100x faster than using drivers.

    Also de-duplicate resulting light objects and nested node trees.
    """
    world = ensure_lib_datablock('worlds', "BotW Lights", link=False)

    # Ensure the lighting objects are linked to the scene and de-duplicated.
    for obj in bpy.data.objects[:]:
        if 'LGT-botw' in obj.name:
            if obj.name.endswith(".001"):
                existing = bpy.data.objects.get(obj.name[:-4])
                obj.user_remap(existing)
                bpy.data.objects.remove(obj)
                obj = existing
            if obj not in set(context.scene.collection.all_objects):
                context.scene.collection.objects.link(obj)

    return world

def import_and_process_dae(
        context, 
        full_path: str, 
        parent_coll=None, 
        rename_objects=False, 
        apply_transforms=True,
        remove_redundant_armatures=True,
        remove_redundant_UVs=True,
    ) -> bpy.types.Collection:
    dae_filename = os.path.basename(full_path)
    dirname = os.path.basename(os.path.dirname(full_path))

    asset_name = dae_filename.replace(".dae", "")
    asset_name = derive_asset_name(dae_filename, dirname)
    dirname = os.path.basename(os.path.dirname(full_path))

    # Create the collection and set it as active so all the objects get imported there to begin with.
    noext_filename = dae_filename.replace(".dae", "")
    coll_name = noext_filename
    collection = ensure_collection(context, coll_name, parent=parent_coll)
    collection.asset_mark()
    collection['dirname'] = dirname
    collection['asset_name'] = asset_name
    collection['file_name'] = noext_filename
    set_active_collection(context, collection)

    with Timer("Import .dae + .fbx", asset_name):
        objs = import_dae(context, full_path, discard_types=('EMPTY'), apply_transforms=apply_transforms)
        rig_name = "RIG-"+asset_name if rename_objects else ""
        objs = import_and_merge_fbx_armature(
            context,
            dae_objs=objs,
            dae_path=full_path,
            rig_name=rig_name,
            apply_transforms=apply_transforms
        )
    if not objs:
        return []

    prefs = get_addon_prefs(context)
    # Try to load an in-game icon for this asset, 
    # if user has specified an icon dirpath in the add-on preferences.
    if prefs.game_icons_folder:
        override = context.copy()
        override["id"] = collection
        icon_filepath = os.path.join(prefs.game_icons_folder, dae_filename.replace(".dae", ""), dae_filename.replace(".dae", ICON_EXTENSION))
        if os.path.exists(icon_filepath):
            with context.temp_override(**override):
                bpy.ops.ed.lib_id_load_custom_preview(filepath=icon_filepath)

    for obj in objs:
        obj = process_object(
            collection, 
            obj, 
            rename_ob_mat=rename_objects, 
            remove_redundant_armatures=remove_redundant_armatures,
            remove_redundant_UVs=remove_redundant_UVs,
        )
        if obj:
            hide_obj_if_useless(obj)
            if apply_transforms:
                hack_zfighting_leaves(collection, obj)

    return collection

def process_object(
        collection, 
        obj, 
        *,
        rename_ob_mat=False, 
        remove_redundant_armatures=True,
        remove_redundant_UVs=True,
    ):
    if obj.type == 'ARMATURE':
        if obj.animation_data and obj.animation_data.action:
            obj.animation_data.action = None
        if remove_redundant_armatures and not is_armature_useful(obj):
            bpy.data.objects.remove(obj)
            return
    elif obj.type == 'MESH':
        if rename_ob_mat:
            new_name = tidy_name(obj.name)
            new_name = collection['asset_name'] + "_" + new_name
            if len(new_name) < 64:
                obj.name = new_name
            else:
                # This will happen often if `rename_collections==False` but `rename_ob_mat_unique==True`.
                # That's just not a recommended combination of settings.
                print("Couldn't rename due to 63-char limit: ", obj.name, new_name)

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

        for uv_layer, name in zip(obj.data.uv_layers, ("Albedo", "SPM")):
            # NOTE: I shouldn't have force-named the UV maps by their "purpose" since it often isn't accurate. 
            # But it's kinda too late to fix now. Sorry!
            # Sometimes there's also a 3rd UV layer.
            uv_layer.name = name

        for mat in obj.data.materials:
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
                process_mat(collection, obj, mat)
                set_object_color(obj)

    obj.data.name = obj.name
    return obj

def hack_zfighting_leaves(collection, obj):
    for filename, obname in LEAF_ZFIGHT_HACK:
        if collection['file_name'] == filename and obj['import_name'] == obname:
            obj.location.z = -0.025
            return

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

def rename_object(obj):
    new_name = obj.name
    if "_Mt_" in new_name:
        new_name = new_name.split("_Mt_")[0]

    new_name = tidy_name(new_name)
    if len(new_name) < 64:
        obj.name = new_name
    else:
        # This should never happen because we don't make names longer here.
        print_later("Couldn't rename due to 63-char limit: ", obj.name, new_name)

def tidy_name(name):
    """This function is allowed to be fairly "destructive" in order to achieve a clean looking name,
    even at the cost of uniqueness (eg. a lot of garbage names might get turned into the same clean name)
    """
    trash = PRIMITIVE_NAMES + ["_Model", "_Root", "_lowpoly", "_low", "__abc", "_Mdl"]
    swap = {
        "_": " ",
        "  " : " ",
        "D L C" : "DLC",
    }

    new_name = name

    if "_MT_" in new_name:
        new_name = new_name.split("_MT_")[1]

    # Nuke certain strings
    for word in trash:
        new_name = new_name.replace(word, "")

    # Remove some prefixes
    for prefix in OBJ_PREFIXES:
        if new_name.startswith(prefix):
            new_name = new_name[len(prefix):]

    # Change CamelCase to Title Case
    new_name = re.sub(r'(?<!^)(?=[A-Z])', ' ', new_name)

    # Find and replace as per the `swap` dict
    for find, replace in swap.items():
        if find in new_name:
            new_name = new_name.replace(find, replace)

    # Remove _001
    suffix_pattern = re.compile(r"\_\d{3}$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    # Remove .001
    suffix_pattern = re.compile(r"\.\d{3}$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    # Remove _group###
    suffix_pattern = re.compile(r"_group\d*$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    if new_name.endswith("_"):
        new_name = new_name[:-1]

    # Remove numbers from end unless preceeded by a symbol (usually . or _)
    suffix_pattern = re.compile(r"(?<=[A-Za-z])\d+$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    return new_name

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

def import_and_merge_fbx_armature(context, *, dae_objs, dae_path, rig_name="", apply_transforms=True):
    """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
    dae_armatures = [ob for ob in dae_objs if ob.type=='ARMATURE']
    if not dae_armatures:
        return dae_objs

    fbx_path = dae_path.replace(".dae", ".fbx")
    if not os.path.isfile(fbx_path):
        return dae_objs
    armatures_to_replace = [a for a in dae_objs if a.type=='ARMATURE' if len(a.pose.bones) > 1 or 'Root' not in a.pose.bones]
    if not armatures_to_replace:
        return dae_objs
    fbx_armatures = import_fbx(context, fbx_path, discard_types=('EMPTY', 'MESH'), apply_transforms=apply_transforms)
    if not fbx_armatures:
        return

    ret_objs = dae_objs[:]

    assert len(fbx_armatures) == len(dae_armatures) == 1

    fbx_arm = fbx_armatures[0]
    dae_arm = dae_armatures[0]
    dae_arm.user_remap(fbx_arm)
    ret_objs.remove(dae_arm)
    bpy.data.objects.remove(dae_arm)

    for fbx_arm in fbx_armatures:
        if rig_name:
            fbx_arm.name = rig_name
        cleanup_fbx_armature(context, fbx_arm)

    ret_objs += fbx_armatures

    return ret_objs

def import_fbx(context, filepath, discard_types=('MESH', 'EMPTY'), apply_transforms=True):
    return import_dae_or_fbx(context, is_dae=False, filepath=filepath, discard_types=discard_types, apply_transforms=apply_transforms)

def import_dae(context, filepath, discard_types=('EMPTY'), apply_transforms=True):
    fix_dae_uvmaps_in_place(filepath)
    return import_dae_or_fbx(context, is_dae=True, filepath=filepath, discard_types=discard_types, apply_transforms=apply_transforms)

def import_dae_or_fbx(context, *, is_dae: bool, filepath: str, discard_types=('EMPTY'), apply_transforms=True):
    # Both of these functions take a "filepath" property, 
    # and both load the contents to the active collection and select all objects.
    import_func = bpy.ops.wm.collada_import if is_dae else bpy.ops.import_scene.fbx

    if not os.path.exists(filepath):
        return False
    if context.active_object:
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    # I've tried a million ways to suppress the .dae importer prints but it can't be done without a PR to Blender.
    # (Or by Popen()ing another blender instance to import and then appending from that, which would be too silly.)
    import_func(filepath=filepath)

    # NOTE: The transform values of some objects are not their actual transforms. (probably some .dae importer bug)
    # They just need to be nudged so they snap to their actual transform values (which do seem to import correctly).
    # But this VERY IMPORTANT to be done before Apply Transforms!!!
    bpy.ops.transform.translate()
    if apply_transforms:
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    for obj in context.selected_objects[:]:
        if obj.type in discard_types:
            bpy.data.objects.remove(obj)
            continue
        if obj.type == 'MESH':
            obj['import_name'] = obj.name[:-4] if obj.name[-4]=="." and obj.name[-3:].isdigit() else obj.name
            for mat in obj.data.materials:
                if 'import_name' not in mat:
                    orig_name = mat.name
                    if len(orig_name) > 4 and orig_name[-4] == ".":
                        orig_name = orig_name[:-4]
                    mat['import_name'] = mat.name[:-4] if mat.name[-4]=="." and mat.name[-3:].isdigit() else mat.name
    return context.selected_objects[:]

def cleanup_fbx_armature(context, fbx_arm):
    assert fbx_arm.visible_get()

    root = fbx_arm.data.bones.get("Root")

    if not root or root.tail_local != Vector((0, 1, 0)):
        # Root bone needs to exist for animations to work.
        context.view_layer.objects.active = fbx_arm
        bpy.ops.object.mode_set(mode='EDIT')
        root_eb = fbx_arm.data.edit_bones.get("Root")
        if not root_eb:
            root_eb = fbx_arm.data.edit_bones.new(name="Root")
        root_eb.head = Vector((0, 0, 0))
        root_eb.tail = Vector((0, 1, 0))
        root_eb.roll = 0
        for eb in fbx_arm.data.edit_bones:
            if not eb.parent and eb != root_eb:
                eb.parent = root_eb
        bpy.ops.object.mode_set(mode='OBJECT')
        root = fbx_arm.data.bones["Root"]

    root_pb = fbx_arm.pose.bones['Root']
    root_pb.custom_shape = ensure_widget('Root')
    root_pb.use_custom_shape_bone_size = False
    root_pb.custom_shape_scale_xyz = [max(fbx_arm.dimensions)/2]*3
    root_pb.custom_shape_rotation_euler = Euler()

    fbx_arm.show_in_front = False
    if fbx_arm.animation_data and fbx_arm.animation_data.action:
        fbx_arm.animation_data.action = None

    for pb in fbx_arm.pose.bones:
        pb.matrix_basis.identity()
        pb.custom_shape = ensure_widget('Bone')
        if "Root" in pb.name:
            pb.custom_shape = ensure_widget('Root')
            pb.use_custom_shape_bone_size = False
            if pb.name in ("Face_Root"):
                for child_pb in pb.children_recursive:
                    child_pb.custom_shape_scale_xyz *= 0.1
        if "_Controled" in pb.name:
            # Found in Hylian heads, eg. "Neck_Controled", "Head_Controled"
            # Probably referring to the fact that in the game engine, 
            # these bones are constrained to another armature's bones of the same name.
            pb.name = pb.name.replace("_Controled", "")
        else:
            if any([pb.name.endswith(suf) for suf in ("_R", "_FR", "_BR", "_R_1", "_R_2")]):
                pb.custom_shape_rotation_euler.z = 0
            else:
                pb.custom_shape_rotation_euler.z = -pi

def set_object_color(obj):
    if obj.type != 'MESH':
        return
    if len(obj.data.materials) == 0:
        return
    mat = obj.data.materials[0]
    if mat:
        obj.color = obj.data.materials[0].diffuse_color
    obj.data.uv_layers.active_index = 0

### Registry

def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="BotW (.dae & .fbx)")

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
