import bpy, os, re, json, zipfile, io, glob
from bpy.props import BoolProperty, StringProperty
from collections import OrderedDict
from math import pi, radians
from pathlib import Path
import pickle
from multiprocessing import shared_memory

from mathutils import Vector, Color, Euler
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from ..databases.asset_names import asset_names
from ..utils.collections import ensure_collection, set_active_collection
from ..utils.widgets import ensure_widget, get_resources_blend_path
from ..prefs import get_addon_prefs
from ..utils.deduplicate_materials import deduplicate_materials, hash_material
from ..utils.timer import Timer
from ..utils.pixel_image import PixelImage
from ..utils.dae_fixer import fix_dae_uvmaps_in_place
from ..utils.mesh import is_uvmap_all_zero, are_uv_maps_identical
from ..utils.string import increment_name

PRINT_LATER = []

# These things are case-sensitive but it shouldn't matter.
# TODO: Could make this extension-agnostic.
ICON_EXTENSION = ".jpg"
TEXTURE_EXTENSION = ".png"

DYES = ["Default", "Blue", "Red", "Yellow", "White", "Black", "Purple", "Green", "Light Blue", "Navy", "Orange", "Peach", "Crimson", "Light Yellow", "Brown", "Gray"]
OBJ_PREFIXES = ["Obj_", "TwnObj_", "TwnObjVillage_", "FldObj_", "DgnObj_", "DgnMrgPrt_"]
PRIMITIVE_NAMES = ["_polySurface", "_pCylinder", "_pSphere", "_pCube", "_pCone", "_pPlane", "pSolid", "_plantroot", "_pPipe"]
GARBAGE_MATS = ["InsideArea", "InsideMat"]
TEX_SUFFIXES = ["_Alb", "_Spm", "_Nrm", "_Emm", "_Emm", "_Clr", "_Mtl"]

# I really wanted to make wind work, but it's impossible to get perfect results from 
# just the material data because it's all inconsistent nonsense.
# So, I just hardcoded some stuff.
LEAF_WIND_UV_ROTATIONS = {
    'PlantTreeTropicalLeaf_A_Alb' : 90,
    'Leaf_TreeWillow_A_02_Alb' : 90,
    'Leaf_TreeWillow_A_01_Alb' : 180,
    'Plant_PalmJungle_A_Leaf_01_Alb': 90,
    'Plant_TreeBananaMiniLeaf_S_A_Alb' : -90,
    'Plant_TreeBananaLeaf_S_A_Alb' : -90,
    'PlantPalmBeach_A_Leaf_Alb' : -90,
    'TreeLeafPalmMini_A_Alb' : -90,
    'Plant_PalmMini_B_Alb': 180,
    'Plant_Palm_A_Leaf_01_Alb' : -90,

    # No rotation, but materials using these textures sometimes don't get detected as wind-blown materials, which is wrong.
    'Plant_TreeLeaf_B_Alb' : 0,
    'Plant_TreeBroadleaf_A_Alb' : 0,
    'Plant_TreeBroadleaf_B_Alb' : 0,
    'Plant_TreeBroadleaf_C_Alb' : 0,
    'TreeCherry_Leaf01_Alb' : 0,
    'TreeCherry_Leaf02_Alb' : 0,
    'Plant_TreeConiferousLow_Leaf_Alb' : 0,
    'Tree_TreeConiferousLeaf_A_Alb' : 0,
    'Tree_TreeConiferousLeaf_B_Alb' : 0,
    'Tree_TreeConiferousLeaf_C_Alb' : 0,
    'Plant_TreePine_Leaf_A_Alb' : 0,
    'Plant_TreePine_Leaf_B_Alb' : 0,
    'Plant_TreeZoraLow_A_Branch_Alb' : 0,
    'Plant_TreeZoraLow_B_Branch_Alb' : 0,

    'Cloth_GerudoMayerBedRoom_I_Alb' : 0,
    'Cloth_GerudoMayerBedRoom_K_Alb' : 0,
}
WIND_FORCE_USE_HEIGHT = [
    'Plant_ChiliPepper_A_01_Alb',
    'Plant_MelonAGrass_A_01_Alb',
    'PlantPumpkinGrass_A_Alb',
    'Obj_Plant_Juniperus_Snow_Alb',
    'Plant_LotusLeaf_A_Alb',
    'Obj_Plant_Weed_A_Alb',
    'Obj_Plant_Weed_B_Alb',
    'Obj_Plant_Weed_C_Alb',
    'Plant_Weed_A_Alb',
    'Plant_Weed_B_Alb',
    'CmnTex_Plant_Tropical_A_Alb',
    'CmnTex_Plant_Tropical_B_Alb',
    'Plant_VioletCliff_A_Alb',
    'Plant_LightGrass_A_Alb',
]
WIND_FORCE_NOWIND = [
    'CmnTex_Plant_KorokWood_A_01_Alb',
    'Plant_KorokColor_Chg_0_Alb',
    'Plant_Korok_Chg_0_Alb',
]
LEAF_ZFIGHT_HACK = [
    # These tree leaf meshes z-fight with the snowy leaves and win, when they shouldn't.
    ('Obj_TreeConiferous_A_Snow_01', 'A21__Mt_Treeleaf_01'),
    ('Obj_TreeConiferous_A_Snow_02', 'A1__Mt_Treeleaf_01'),
    ('Obj_TreeConiferous_A_Snow_03', 'A10__Mt_Treeleaf_01'),
]

METAL_ROUGHNESS = 0.6

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ADDON_DIR = os.sep.join(THIS_FOLDER.split(os.sep)[:-1])
MATERIAL_DATA_ZIP = os.path.join(ADDON_DIR, "databases", "materials.zip")
MATERIAL_DEFAULTS_JSON = os.path.join(ADDON_DIR, "databases", "material_defaults.json")
TEXTURE_INFO_JSON = os.path.join(ADDON_DIR, "databases", "texture_info.json")

CACHE_mat_defaults = {}
CACHE_tex_info = {}
CACHE_shader_data = {}
CACHE_image_paths = {}

def read_shared_dict(shm_name="my_shared_dict"):
    """Reads a dictionary from shared memory and deserializes it."""
    shm = shared_memory.SharedMemory(name=shm_name)  # Attach to shared memory
    serialized_data = bytes(shm.buf[:])  # Read bytes from shared memory
    data = pickle.loads(serialized_data)  # Deserialize back to dictionary

    return data

def ensure_caches(force=False, shared_mem_name=""):
    """Load a bunch of useful data into memory.
    Only needs to be done once per Blender session.
    Done when the the import operator is first used.
    """
    global CACHE_mat_defaults   # 18 kb
    global CACHE_tex_info       # 4.5 mb
    global CACHE_image_paths    # a few kb
    global CACHE_shader_data    # 100 mb

    if shared_mem_name:
        data = read_shared_dict(shared_mem_name)
        CACHE_mat_defaults = data['material_defaults']
        CACHE_tex_info = data['tex_info']
        CACHE_image_paths = data['image_paths']
        CACHE_shader_data = data['shader_data']
        return {'material_defaults':CACHE_mat_defaults, 'tex_info': CACHE_tex_info, 'image_paths': CACHE_image_paths, 'shader_data': CACHE_shader_data}

    if not CACHE_mat_defaults or force:
        with open(MATERIAL_DEFAULTS_JSON, "r", encoding="utf-8") as f:
            CACHE_mat_defaults = json.load(f)

    if not CACHE_tex_info or force:
        with open(TEXTURE_INFO_JSON, "r", encoding="utf-8") as f:
            CACHE_tex_info = json.load(f)

    if not CACHE_image_paths or force:
        cache_ensure_image_paths()

    if not CACHE_shader_data or force:
        cache_ensure_shader_data()

    return {'material_defaults':CACHE_mat_defaults, 'tex_info': CACHE_tex_info, 'image_paths': CACHE_image_paths, 'shader_data': CACHE_shader_data}

def cache_ensure_image_paths() -> dict[str, str]:
    """Create a mapping from image names to full filepaths in the Game Models folder."""

    global CACHE_image_paths
    prefs = get_addon_prefs()

    for dirpath, _subfolders, files in os.walk(prefs.game_models_folder):
        for file in files:
            if prefs.game_models_folder:
                dirpath = os.path.join(prefs.game_models_folder, os.path.basename(dirpath))
                # print_later("Directory path: ", dirpath)
            else:
                print_later("Game models folder not specified.")
            filepath = os.path.join(dirpath, file)
            if not os.path.exists(filepath):
                print_later(f"File does not exist: {filepath}")
                continue

            if file.lower().endswith(TEXTURE_EXTENSION):
                CACHE_image_paths[file[:-len(TEXTURE_EXTENSION)]] = filepath

    return CACHE_image_paths

def cache_ensure_shader_data():
    global CACHE_shader_data
    if not CACHE_shader_data:
        with open(MATERIAL_DATA_ZIP, "rb") as f:
            zip_data = f.read()

        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            for file_name in z.namelist():
                with z.open(file_name) as file:
                    CACHE_shader_data[file_name] = json.loads(file.read())
    return CACHE_shader_data

def get_image_path(image_name: str) -> str:
    if not CACHE_image_paths:
        with Timer("Image path cache"):
            cache_ensure_image_paths()
    # Allow passing a full path, why not.
    image_name = Path(image_name).stem
    return CACHE_image_paths.get(image_name, "")

def print_later(*msg):
    PRINT_LATER.append("".join([str(m) for m in msg]))

def camel_to_spaces(str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str)

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all .dae & .fbx files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW .dae + .fbx"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE', 'HIDDEN'})
    rename_known_assets: BoolProperty(name="Rename Known Assets", description="If an asset's name is found in the asset name map, rename it to that", default=True)
    rename_unknown_assets: BoolProperty(name="Rename Unknown Assets", description="If an asset's name isn't found in the asset name map, rename it to title case and remove some prefixes", default=True)

    rename_prepend: BoolProperty(name="Prepend Asset to Object Names", description="Prepend asset name to object and material names. Useful when importing many assets into a single file to keep names unique, but can also result in exceeding the 63-character limit. Those cases will be skipped (not renamed)", default=True)
    rename_clean_names: BoolProperty(name="Clean Object & Material Names", description="", default=True)

    apply_transforms: BoolProperty(name="Apply Transforms", description="Objects import with correct transforms, but in some cases they are not their default transforms. This should probably only be disabled if you're a modder and you plan to export this back into the game. Applying transforms is also necessary for wind shader effects to work", default=True)
    remove_redundant_armatures: BoolProperty(name="Remove Redundant Armatures", description="If an armature has only 1 bone and it's at the world origin, or if it doesn't deform any objects with any of its bones, remove it", default=True)
    remove_redundant_UVs: BoolProperty(name="Remove Redundant UVs", description="If a UVMap is the same as a previous one, or if it's empty, remove it", default=True)

    create_parent_collections: BoolProperty(name="Create Parent Collections", description="When a directory has more than 1 file, create a parent collection that represents that directory", default=True)

    deduplicate_materials: BoolProperty(name="Deduplicate Materials", description="If two materials end up with identical nodetrees, merge them into one", default=True)

    force_update_caches: BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'rename_known_assets')
        if self.rename_known_assets:
            layout.prop(self, 'rename_unknown_assets')
        layout.prop(self, 'rename_prepend')
        layout.prop(self, 'rename_clean_names')
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
        if not self.rename_known_assets:
            self.rename_unknown_assets = False

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
            if dirname.endswith("_Far"):
                # These are LOD meshes, we don't want those.
                continue
            if len(dae_files) > 1 and self.create_parent_collections:
                parent_coll_name = root.split(os.sep)[-1]
                if root_dir_name != parent_coll_name:
                    parent_coll_name = asset_names.get(parent_coll_name, parent_coll_name)
                    parent_coll = ensure_collection(context, parent_coll_name)
            for dae_name in dae_files:
                asset_name = dae_name.replace(".dae", "")
                if self.rename_known_assets:
                    asset_name = derive_asset_name(dae_name, dirname, len(dae_files)==1, remove_prefixes=self.rename_unknown_assets)

                if 'Animation' in asset_name:
                    continue
                full_path = os.path.join(root, dae_name)
                with Timer("Full Import", dae_name):
                    imported_objects += import_and_process_dae(
                        context, 
                        full_path, 
                        asset_name, 
                        parent_coll, 
                        uniqify_names=self.rename_prepend, 
                        clean_names=self.rename_clean_names,
                        apply_transforms=self.apply_transforms,
                        remove_redundant_armatures=self.remove_redundant_armatures,
                        remove_redundant_UVs=self.remove_redundant_UVs,
                    )
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

def derive_asset_name(dae_filename: str, dirname: str, is_single_file: bool, remove_prefixes=True) -> str:
    without_ext = dae_filename.replace(".dae", "")
    asset_name = asset_names.get(without_ext, without_ext)

    # If the asset name wasn't in the dictionary, try without any _A, _B suffixes.
    if asset_name == without_ext and (without_ext.endswith("_A") or without_ext.endswith("_B")):
        asset_name = asset_names.get(without_ext[:-2], without_ext[:-2])

    # If an asset directory only has one .dae file and its name wasn't in the asset dictionary, 
    # try the directory's name instead.
    if asset_name == without_ext and is_single_file:
        asset_name = asset_names.get(dirname, asset_name)

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

    # Most "Obj_" prefix meshes won't be in the dictionary, since they don't have any in-game strings 
    # that are exposed to the player. (non-cel shaded environment meshes)
    # So to avoid having to add all of these to the dictionary, just do some string operations.
    for prefix in OBJ_PREFIXES:
        if asset_name.startswith(prefix):
            asset_name = asset_name[len(prefix):]

    asset_name = asset_name.replace("D L C", "DLC")
    asset_name = camel_to_spaces(asset_name.replace("_", " ")).replace("  ", " ")

    return asset_name

def ensure_botw_scene_settings(context):
    # Zelda shaders absolutely depend on EEVEE.
    context.scene.render.engine = 'BLENDER_EEVEE_NEXT'

    # Set sRGB view transform, as that's what the game probably uses.
    context.scene.view_settings.view_transform = 'Standard'

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
        bloom_node.mix = -0.34
        bloom_node.threshold = 1.28
        bloom_node.size = 6
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
    abs_path = get_resources_blend_path()
    WORLD_NAME = "BotW Lights"
    # Check if it already exists locally.
    world = bpy.data.worlds.get(WORLD_NAME)
    if world:
        # World exists, so just return it.
        return world

    # Import World from resources.blend file.
    with bpy.data.libraries.load(abs_path, link=False, relative=False) as (
        data_from,
        data_to,
    ):
        for world in data_from.worlds:
            if world == WORLD_NAME:
                data_to.worlds.append(world)

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
    
    world = bpy.data.worlds.get(WORLD_NAME)
    return world

def import_and_process_dae(
        context, 
        full_path: str, 
        asset_name: str=None, 
        parent_coll=None, 
        rename_coll=True, 
        uniqify_names=False, 
        clean_names=True,
        apply_transforms=True,
        remove_redundant_armatures=True,
        remove_redundant_UVs=True,
    ) -> list[bpy.types.Object]:
    dae_filename = os.path.basename(full_path)
    asset_name = asset_name or os.path.splitext(dae_filename)[0]
    dirname = os.path.basename(os.path.dirname(full_path))

    prefs = get_addon_prefs()

    # Create the collection and set it as active so all the objects get imported there to begin with.
    noext_filename = dae_filename.replace(".dae", "")
    coll_name = asset_name if rename_coll else noext_filename
    collection = ensure_collection(context, coll_name, parent=parent_coll)
    collection.asset_mark()
    collection['dirname'] = dirname
    collection['asset_name'] = asset_name
    collection['file_name'] = noext_filename
    set_active_collection(context, collection)

    with Timer("Import .dae + .fbx", asset_name):
        objs = import_dae(context, full_path, discard_types=('EMPTY'), apply_transforms=apply_transforms)
        objs = import_and_merge_fbx_armature(context, dae_objs=objs, dae_path=full_path, asset_name=asset_name, apply_transforms=apply_transforms)
    if not objs:
        return []

    # Try to load an in-game icon for this asset, 
    # if user has specified an icon dirpath in the add-on preferences.
    prefs = get_addon_prefs(context)
    if prefs.game_icons_folder:
        override = context.copy()
        override["id"] = collection
        icon_filepath = os.path.join(prefs.game_icons_folder, dae_filename.replace(".dae", ""), dae_filename.replace(".dae", ICON_EXTENSION))
        if os.path.exists(icon_filepath):
            with context.temp_override(**override):
                bpy.ops.ed.lib_id_load_custom_preview(filepath=icon_filepath)

    ret_objs = []
    for obj in objs:
        obj = process_object(
            collection, 
            obj, 
            asset_name=asset_name, 
            uniqify_names=uniqify_names, 
            clean_names=clean_names, 
            remove_redundant_armatures=remove_redundant_armatures,
            remove_redundant_UVs=remove_redundant_UVs,
        )
        if obj:
            ret_objs.append(obj)
            hide_obj_if_useless(obj)
            if apply_transforms:
                hack_zfighting_leaves(collection, obj)

    return ret_objs

def process_object(
        collection, 
        obj, 
        *,
        asset_name, 
        uniqify_names=False, 
        clean_names=True, 
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
        if clean_names:
            rename_object(obj)

        if uniqify_names:
            new_name = asset_name + "_" + obj.name
            if len(new_name) < 64:
                obj.name = new_name
            else:
                # This will happen often if `rename_unknown_assets==False` but `rename_ob_mat_unique==True`.
                # That's just not a recommended combination of settings.
                print_later("Couldn't rename due to 63-char limit: ", obj.name, new_name)

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
            json_mat_name = ".".join((collection['dirname'], collection['file_name'], mat['import_name'] + ".json"))
            mat['json_name'] = json_mat_name
            mat_data = get_shader_data(mat)
            if mat_data:
                # Store as string because Blender doesn't let us store 
                # an arbitrary structure of lists/dicts.
                mat['shader_data'] = json.dumps(mat_data)
            else:
                print_later(f"Couldn't find material .json: {json_mat_name}")

            new_name = mat.name
            if "Mt_" in mat.name and clean_names:
                new_name = mat.name.split("Mt_")[1]

            if uniqify_names:
                new_name = asset_name + ": " + new_name
                if new_name != mat.name and new_name in bpy.data.materials:
                    # If the material with this name already exists, overwrite it.
                    # Since material names are unique, this should only happen when trying 
                    # to delete and re-import an asset, and forgetting to purge.
                    existing_mat = bpy.data.materials.get(new_name)
                    existing_mat.user_remap(mat)
                    bpy.data.materials.remove(existing_mat)

            mat.name = new_name

            with Timer("Setup material", mat.name):
                process_material(collection, obj, mat)
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
    trash = PRIMITIVE_NAMES + ["_Model", "_Root", "_lowpoly", "_low", "__abc", "_Mdl"]
    swap = {
        "  " : " ",
        "D L C" : "DLC"
    }

    new_name = name

    for primitive in PRIMITIVE_NAMES:
        if primitive in new_name:
            new_name = new_name.split(primitive)[0]

    # Nuke certain strings
    for word in trash:
        new_name = new_name.replace(word, "")

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

    if "_MT_" in new_name:
        new_name = new_name.split("_MT_")[1]

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

def import_and_merge_fbx_armature(context, *, dae_objs, dae_path, asset_name, apply_transforms=True):
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
        fbx_arm.name = "RIG-"+asset_name
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

def process_material(collection, obj, material):
    """My best effort at setting up materials based on data exported from my custom 
    Switch Toolbox, and included in this add-on inside materials.zip.
    """

    if any([s in material.name for s in GARBAGE_MATS]):
        # This is some sorta gameengine mesh, we don't care.
        obj.hide_viewport, obj.hide_render = True, True
        return

    nodes = material.node_tree.nodes
    if 'BotW Output' in nodes:
        # This material was already processed, don't process it again as that might break stuff.
        return

    for suf in "LR", "RL":
        if material.name.endswith("Eyeball_"+suf[0]):
            existing = bpy.data.materials.get(material.name.replace(suf[0], suf[1]))
            if existing:
                material.user_remap(existing)
                existing.name = existing.name[:-2]
                return

    textures = load_assigned_json_textures(material)
    shader_name = guess_shader(collection, obj, material, textures)
    socket_map = guess_sockets_for_textures(material, textures, shader_name)
    if shader_name == 'BotW: Material Blend':
        more_textures = load_blend_textures(material, socket_map)
        if not more_textures:
            shader_name = 'BotW: Smooth Shade'
        socket_map.update(more_textures)
    elif shader_name == 'BotW: Cel Shade':
        albedo = next((img for img, socket_name in socket_map.items() if socket_name=='Albedo'), None)
        if albedo:
            dye_textures = guess_dye_textures(albedo)
            socket_map.update([(tex, 'Albedo') for tex in dye_textures])
    shader_node = init_nodetree(material, shader_name)

    # Create image nodes, guess UV layer by name, set image color spaces
    with Timer("Hookup tex nodes", material.name):
        spm_has_green = hookup_texture_nodes(collection, obj, material, shader_node, socket_map)
        hookup_rgb_nodes(material, shader_node)

    set_shader_socket_values(collection, obj, material, shader_node, spm_has_green)
    fix_material_viewport_display(material)
    material['hash'] = hash_material(material)

def load_assigned_json_textures(material) -> list[bpy.types.Image]:
    """If a material was assigned a 'shader_data' custom property, that's data
    we extracted from the .bmat using my modified version of Switch Toolbox.
    """

    texture_maps = get_shader_prop_of_mat(material, 'TextureMaps')
    if not texture_maps:
        return []

    missing_tex_from_json = []
    textures = []

    for name, tex_data in texture_maps.items():
        if name in ('MaterialAlb', 'MaterialCmb', 'ForReplace_Lumberjack'):
            continue
        img = ensure_loaded_img(name)
        if not img:
            print_later(f"Couldn't find texture: '{material.name}' -> {name}")
            missing_tex_from_json.append(name)
            continue
        textures.append(img)

    if missing_tex_from_json:
        material['missing_textures'] = str(missing_tex_from_json)

    return textures

def load_blend_textures(material, socket_map) -> OrderedDict[bpy.types.Image, str]:
    """Based on https://github.com/augmero/bmubin/blob/main/scripts/asset/shader_fixer.py"""
    alb_blend_idx = 1
    nrm_blend_idx = 1
    new_socket_map = OrderedDict()
    tex_indicies = material.get('blend_indicies', [])
    for i, tex_index in enumerate(tex_indicies):
        albedo = ensure_loaded_img(f"MaterialAlb_Slice_{tex_index}_.png")
        if albedo:
            if 'Albedo' not in list(socket_map.values()):
                new_socket_map[albedo] = "Albedo"
            else:
                new_socket_map[albedo] = f'Albedo Blend {alb_blend_idx}'
                alb_blend_idx += 1
        normal = ensure_loaded_img(f"MaterialCmb_Slice_{tex_index}_.png")
        if normal:
            if 'Normal Map' not in list(socket_map.values()):
                new_socket_map[normal] = "Normal Map"
            else:
                new_socket_map[normal] = f'Normal Blend {nrm_blend_idx}'
                nrm_blend_idx += 1

    return new_socket_map

def guess_sockets_for_textures(material, textures, shader_name) -> OrderedDict[bpy.types.Image, str]:
    socket_map = OrderedDict()
    tex_types = []
    for img in textures:
        tex_data = get_tex_data(material, img)
        assert tex_data != {}
        type = tex_data['Type'].strip()
        if type == 'Unknown':
            sampler = tex_data['SamplerName']
            # If the material data doesn't give us the texture type, we have some fallbacks to guess.
            if '_Alb' in img.name:
                type = 'Diffuse'
            elif '_Spm' in img.name:
                type = 'Specular'
            elif '_Nrm' in img.name:
                type = 'Normal'
            elif '_Msk' in img.name:
                type = 'Alpha'
            elif sampler in ('_ms0', 'ms0', '_ms1', 'ms1'):
                type = 'Alpha'
            elif sampler in ('_n0', 'n0', '_n1', 'n1'):
                type = 'Normal'
            elif sampler in ('_a0', 'a0', '_a1', 'a1'):
                type = 'Diffuse'
            elif sampler in ('_e0', 'e0', '_e1', 'e1'):
                type = 'Emission'
            elif sampler in ('_ao0', 'ao0', '_ao1', 'ao1'):
                type = 'AO'
            elif sampler in ('_s0', 's0', '_s1', 's1'):
                type = 'Specular'
            elif sampler in ('_mt0', 'mt0', '_mt1', 'mt1'):
                type = 'Metallic'
            elif sampler in ('_gn0'):
                # These sampler names have proved unreliable for determining texture type.
                pass
            else:
                # There may be other useful sampler names for determining texture type.
                pass
        tex_types.append((type, img))

    for type, img in tex_types:
        # NOTE: Can add support for more shader socket names here.
        if type == 'Diffuse':
            if "_Red_Alb" in img.name and shader_name=='BotW: Cel Shade':
                socket_map[img] = "Skin Red Albedo"
            else:
                socket_map[img] = "Albedo"
        elif type == 'Alpha':
            socket_map[img] = "Alpha"
        elif type == 'Specular':
            socket_map[img] = "SPM"
        elif type == 'Normal':
            socket_map[img] = "Normal Map"
        elif type == 'Emission':
            socket_map[img] = "Emission Mask"
        elif type == 'AO':
            socket_map[img] = "AO"
        elif type == 'Metallic':
            socket_map[img] = "Metallic"
        else:
            socket_map[img] = type

    return socket_map

def init_nodetree(material, shader_name) -> bpy.types.ShaderNode:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Nuke the nodes as imported by .fbx, it's easier to build from scratch.
    nodes.clear()

    # Create central shader node by loading node tree from resources.blend.
    shader_node = nodes.new("ShaderNodeGroup")
    shader_node.node_tree = ensure_nodetree(shader_name)
    shader_node.location = (200, 0)
    shader_node.width = 300
    shader_node.name = "Main Shader"

    # Output node
    output_node = nodes.new("ShaderNodeOutputMaterial")
    output_node.location = (600, 0)
    output_node.name = "BotW Output"
    links.new(shader_node.outputs[0], output_node.inputs[0])
    if 'Displacement' in shader_node.outputs:
        links.new(shader_node.outputs['Displacement'], output_node.inputs['Displacement'])

    return shader_node

def guess_colorspace(material, img):
    """This is a dangerously simple guess, but it works surprisingly alright."""
    tex_data = get_tex_data(material, img)
    if tex_data:
        if tex_data['Type'] == 'Diffuse':
            return 'sRGB'
        elif tex_data['Type'] == 'Unknown' and "_Alb" in img.name or "MaterialAlb" in img.name:
            return 'sRGB'

    if "_Alb" in img.name or "MaterialAlb" in img.name:
        return 'sRGB'

    return 'Non-Color'

def guess_shader(collection, obj, material, all_textures):
    lc_obname = obj.name.lower()
    lc_assetname = (collection.get('asset_name') or "").lower()

    fallback_shader = "BotW: Cel Shade"
    for prefix in OBJ_PREFIXES:
        if collection['dirname'].startswith(prefix):
            fallback_shader = "BotW: Smooth Shade"
            break

    if (
        get_shader_prop_of_mat(material, 'shaderassign>options>uking_texcoord_toon_spec_srt') == 3 # Strong correspondance to regular Cel shading. (not 100% perfect, eg. Link's earrings)
        or get_shader_prop_of_mat(material, 'shaderassign>options>uking_specular_hair')==402 # This is the flag for hair Cel shading (3 cels instead of 2 in hair) (I think this is 100%)
    ):
        return "BotW: Cel Shade"
    if get_shader_prop_of_mat(material, 'shaderassign>samplers>_a0') == '_fx0':
        return "BotW: Ancient Weapon Blade"

    if "eye" in lc_obname or "eye" in material['import_name'].lower() and "mask" not in lc_obname and "ravio" not in lc_assetname:
        # TODO: I'm almost sure we can find a consistent way to identify eye materials, just didn't get around to it yet.
        return "BotW: Eye"

    if any(["EmmMsk.1" in img.name for img in all_textures]) and not any([word in material['import_name'].lower() for word in ('handle', '_02')]):
        return "BotW: Elemental Weapon"
    if any(["Emm_Emm" in img.name for img in all_textures]) and 'Divine' in collection['asset_name']:
        return "BotW: Divine Eye"
    elif any(["clrmak" in img.name.lower() or "clrmsk" in img.name.lower() for img in all_textures]):
        return "BotW: Generic NPC"

    albedo = next((img for img in all_textures if img.colorspace_settings.name=='sRGB'), None)
    if albedo:
        wind_enabled = is_blown_by_wind(material, os.path.splitext(albedo.name)[0])
        if wind_enabled:
            # NOTE: We store this property even if we don't think this material uses height-based wind, 
            # since detection for that is unreliable, and if we were to manually enable that checkbox in 
            # a material, we'll need this property to be present.
            obj['wind_height'] = max([bboxpoint[2] for bboxpoint in obj.bound_box])
            if 'custom_normal' in obj.data.attributes:
                # Disable custom normals without deleting them.
                # They tend to make the leaves look a lot worse in Blender.
                obj.data.attributes['custom_normal'].name = 'custom_normal_bkp'
            material.displacement_method = 'BOTH'
            return "BotW: Fauna"
    else:
        material['WARNING: Albedo Missing!'] = True

    blend_indicies = get_indicies_for_material_blend(material)
    if blend_indicies:
        material['blend_indicies'] = blend_indicies
        return "BotW: Material Blend"
    elif len(obj.data.color_attributes) > 0 and len([img for img in all_textures if img.colorspace_settings.name=='sRGB']) > 1:
        if not is_a_tree(material):
            material['WARNING'] = "Using material blend shader because there is a vertex color and >1 albedos."
            return "BotW: Material Blend"

    print_later("Failed to guess shader for material: "+material.name)
    return fallback_shader

def is_a_tree(material):
    return get_shader_prop_of_mat(material, "shaderassign>options>uking_enable_lumberjack") == 1

def is_blown_by_wind(material, albedo_name=""):
    """I couldn't find a reliable indicator for this, which is very frustrating. 
    But there's only a finite number of leaf textures in the game, 
    so I just hard-coded some data."""

    # Other flags I checked, but to no avail:
    # uking_wind_vtx_transform_channel
    # shaderassign>options>uking_enable_wind_vtx_transform_coreinfo     # Most of these are indeed blown by the wind, but not nearly all of them.
    # shaderassign>options>uking_enable_wind_vtx_transform_normal_lock  # Most of these or maybe all of them are NOT blown by the wind. Maybe this indicates that objects that are blown by the wind should collide with this material, but I doubt that.

    wind_enable = get_shader_prop_of_mat(material, "shaderassign>options>uking_enable_wind_vtx_transform")
    wind_enable_lie = get_shader_prop_of_mat(material, "shaderassign>options>uking_enable_wind_vtx_transform_lie")
    wind_enable_height = get_shader_prop_of_mat(material, "shaderassign>options>uking_enable_wind_vtx_transform_height")

    wind_int = get_shader_prop_of_mat(material, "matparam>uking_wind_vtx_transform_intensity>ValueFloat", index=0)
    wind_lie_int = get_shader_prop_of_mat(material, "matparam>uking_wind_vtx_transform_lie_intensity>ValueFloat", index=0)
    wind_height_int = get_shader_prop_of_mat(material, "matparam>uking_wind_vtx_transform_lie_height>ValueFloat", index=0)

    uses_a_windy_albedo = (albedo_name in LEAF_WIND_UV_ROTATIONS or albedo_name in WIND_FORCE_USE_HEIGHT)
    force_no_wind = albedo_name in WIND_FORCE_NOWIND
    wind_enabled = (
        (
            (wind_enable_height and wind_height_int != 0.5) or
            (wind_enable_lie and wind_lie_int != 3.0) or
            (wind_enable and wind_int != 0.1) or
            uses_a_windy_albedo
        ) and
        not is_a_tree(material) and
        not force_no_wind
    )
    return wind_enabled

def get_indicies_for_material_blend(material):
    # texture_array_index has 6 integers between 0-82.
    # These definitely correspond directly to the textures inside content/Terrain,
    # and their order seems to matter too.
    tex_array_index_props = []
    shader_array_index_props = []

    for i in range(5):
        # Skipping last value on purpose because it's the same value across the whole game.
        val = get_shader_prop_of_mat(material, f'matparam>texture_array_index{i}>ValueFloat')
        tex_array_index_props.append(val)
        shader_array_index_props.append(get_shader_prop_of_mat(material, f'shaderassign>options>uking_texture_array_texture{i}'))

    all_default = all([v==-1 for v in shader_array_index_props])
    tex_indicies = []
    for tex_index_value, shader_array_value in zip(tex_array_index_props, shader_array_index_props):
        if tex_index_value in (-1, None):
            continue
        if shader_array_value == -1 and not all_default:
            # If not all ShaderOptions are -1 but this one is,
            # the corresponding terrain texture is not actually used.
            # This most commonly happens for tex_array_prop==0.
            continue

        if tex_index_value in tex_indicies:
            continue
        if tex_index_value == 0 and all_default:
            # Terrain texture index 0 is a grass texture, but if the corresponding 
            # ShaderOptions values are all defaults, it's the same as if it existed with a value of -1;
            # So just like in the above case, this is not actually a reference to that grass texture.
            continue
        tex_indicies.append(int(tex_index_value))

    return tex_indicies

def guess_dye_textures(albedo) -> list[bpy.types.Image]:
    """Find alt textures of an albedo."""
    img = albedo
    dye_textures = []
    next_name = albedo.name
    while img:
        next_name = increment_name(next_name)
        if next_name == albedo.name:
            # No numbers in the name.
            break

        img = ensure_loaded_img(next_name)
        if not img:
            break

        dye_textures.append(img)
    return dye_textures

def hookup_texture_nodes(collection, object, material, shader_node, socket_map) -> bool:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    shader_name = shader_node.node_tree.name
    # Only use dye labels if the number of albedo textures is exactly the number of dyes in the game.
    use_dye_labels = len([img for img, socket in socket_map.items() if socket=='Albedo']) == len(DYES)
    albedo_count = 0
    dye_count = 0
    spm_has_green = False
    for i, (img, socket_name) in enumerate(socket_map.items()):
        img.colorspace_settings.name = guess_colorspace(material, img)

        pixel_image = PixelImage.from_blender_image(img)
        if socket_name != 'Albedo' and pixel_image.is_single_color:
            # If the whole image is just one color, use an RGB node instead.
            img_node = nodes.new(type="ShaderNodeRGB")
            img_node.outputs[0].default_value = list(pixel_image.average_color) + [1]
        else:
            img_node = nodes.new(type="ShaderNodeTexImage")
            img_node.image = img
            img_node.width = 400
        img_node.label = img.name

        if socket_name in ("", "Unknown"):
            socket_name = guess_socket_name(img, shader_name)

        img_node.location = (-300, (i-dye_count)* -300)

        if socket_name == 'Albedo' and shader_name == 'BotW: Cel Shade':
            existing_albedo = get_albedo_img_node(material)
            if existing_albedo and existing_albedo.image and existing_albedo.image.name.split(".")[0] == img_node.image.name.split(".")[0]:
                dye_count += 1
                img_node.label = str(dye_count)
                if use_dye_labels:
                    img_node.label += ": " + DYES[dye_count]
                img_node.location = (-300, dye_count*60)
                img_node.hide = True
            albedo_count += 1

        if socket_name == 'SPM' and pixel_image.has_green and not pixel_image.all_channels_match:
            spm_has_green = True

        create_helper_nodes(collection, object, material, img_node, pixel_image, socket_name, shader_node)

        # Hook up texture to target socket on the shader node group.
        shader_socket = shader_node.inputs.get(socket_name)

        img_node.label = socket_name + " " + img_node.label
        if not shader_socket:
            img_node.label = "No socket: " + socket_name
            print_later(f"Couldn't find shader socket: '{material.name}' -> '{socket_name}'")
            continue

        # # Bit of a hack, re-direct Material Blend socket names that need to know the shader type. 
        # if shader_node.node_tree.name == 'BotW: Material Blend':
        #     # This shader blends up to 3 materials together.
        #     if len(shader_socket.links) > 0:
        #         if socket_name == 'Albedo':
        #             socket_name = 'Albedo Blend 1'
        #         elif socket_name == 'Normal Map':
        #             socket_name = 'Normal Blend 1'
        #         elif socket_name == 'Albedo Blend 1':
        #             socket_name = 'Albedo Blend 2'
        #         elif socket_name == 'Normal Blend 1':
        #             socket_name = 'Normal Blend 2'
        #         shader_socket = shader_node.inputs.get(socket_name)
        #         img_node.label = socket_name + " " + img_node.label

        if socket_name == "Albedo Blend 1":
            set_socket_value(shader_node, f"Blend 1 Factor", 1)

        if len(shader_socket.links) == 0:
            if shader_socket.name == 'Alpha' and get_shader_prop_of_mat(material, 'isTransparent') != 1:
                pass
            else:
                links.new(img_node.outputs['Color'], shader_socket)
        else:
            print_later(f"Shader socket already taken: '{material.name}' -> '{img.name}' ({socket_name})")

        if bool(get_shader_prop_of_mat(material, 'isTransparent')) != False:
            material.surface_render_method = get_alpha_mode(material)
        # Since transparency doesn't (always) get its own texture node, hook up the Alpha of the Albedo.
        alpha_socket = shader_node.inputs.get('Alpha')
        if socket_name in ('Albedo', 'Fx Texture Distorted') and get_shader_prop_of_mat(material, 'isTransparent')==1 and pixel_image.has_alpha:
            if alpha_socket and len(alpha_socket.links) == 0 and 'Alpha' in img_node.outputs:
                links.new(img_node.outputs['Alpha'], alpha_socket)
        # But if after those steps we didn't hook up any alpha, don't set it to Blended, since that will cause sorting issues.
        transparent_edges = shader_node.inputs.get('Transparent Edges')
        if not alpha_socket or len(alpha_socket.links) == 0 and not (transparent_edges and transparent_edges.default_value==True):
            material.surface_render_method = 'DITHERED'

    first_plugged_img = next((s.links[0].from_node for s in shader_node.inputs if len(s.links)>0 and s.links[0].from_node.type == 'TEX_IMAGE'), None)
    if first_plugged_img:
        nodes.active = first_plugged_img

    return spm_has_green

def guess_socket_name(img, shader_name="BotW: Cel Shade") -> str:
    """Guess what shader socket the given image should be plugged into."""

    if type(img) == bpy.types.Image:
        lc_img_name = img.name.lower()
    elif type(img) == str:
        lc_img_name = img.lower()
    else:
        return ""

    if shader_name == 'BotW: Eye' and 'shadow' in lc_img_name:
        return "Eye Shadow"

    if "_alb" in lc_img_name:
        if "_red_alb" in lc_img_name and shader_name=='BotW: Cel Shade':
            return "Skin Red Albedo"
        elif "_damage_alb" in lc_img_name and shader_name=='BotW: Cel Shade':
            return "Skin Damage Albedo"
        return "Albedo"
        
    elif "clrmak_00" in lc_img_name or "clrmsk_00" in lc_img_name:
        return "Tint Mask 0"
    elif "clrmak_01" in lc_img_name or "clrmsk_01" in lc_img_name:
        return "Tint Mask 1"
    elif "clrmak_02" in lc_img_name or "clrmsk_02" in lc_img_name:
        return "Tint Mask 2"
    elif "_spm" in lc_img_name:
        return "SPM"
    elif "_nrm" in lc_img_name:
        return "Normal Map"
    elif "_ao" in lc_img_name:
        return "AO"
    elif "_emm_emm" in lc_img_name:
        return "Emm_Emm"
    elif "_emmmsk_" in lc_img_name:
        # Scrolling textures for the Obliterator only.
        pass
    elif "_emmmsk.2" in lc_img_name:
        # This only happens for elemental weapons and obliterator.
        # Red channel is actual emission mask, green is a gradient for how charged the weapon is,
        # but in the shader I just use a UV gradient instead of the green channel.
        return "Emission Mask"

    elif "_emmmsk.1" in lc_img_name or "_emmmsk" in lc_img_name:
        # It's a scrolling texture for the glow.
        return "Emission Scroll"
    elif "_emmmsk" in lc_img_name:
        # Regular scrolling textures for most of the game.
        return "Emission Scroll"
    elif "_emm" in lc_img_name:
        return "Emission Mask"
    elif shader_name == 'BotW: Ancient Weapon Blade' and "_fx" in lc_img_name:
        return "Fx Texture"
    elif "_mtl" in lc_img_name:
        return "Metallic"
    elif "_msk" in lc_img_name:
        return "Alpha"

    return ""

def create_helper_nodes(collection, object, material, img_node, pixel_image, socket_name, shader_node) -> tuple[int, int]:
    shader_name = shader_node.node_tree.name
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    lc_assetname = (collection.get('asset_name') or "").lower()

    ensure_UV_node(object, material, img_node, shader_name)

    if shader_name == 'BotW: Eye' and socket_name in ('Albedo', 'Emission Color', 'Emission Mask', 'Normal Map') and len(img_node.inputs) > 0:
        eye_rig_node = nodes.get("Eye Rig")
        if not eye_rig_node:
            eye_rig_nt = ensure_nodetree("BotW: Eye Rig")
            eye_rig_node = nodes.new("ShaderNodeGroup")
            eye_rig_node.node_tree = eye_rig_nt
            eye_rig_node.location = img_node.location + Vector((-400, 0))
            eye_rig_node.width = 300
            eye_rig_node.name = "Eye Rig"
        links.new(eye_rig_node.outputs[0], img_node.inputs[0])
    elif socket_name == 'Fx Texture':
        distorted_img = nodes.new("ShaderNodeTexImage")
        distorted_img.image = img_node.image
        distorted_img.width = img_node.width
        distorted_img.location = img_node.location + Vector((0, 300))
        distortion_shader = ensure_nodetree('BotW: Ancient Weapon Blade Heat Distortion')
        distortion_node = nodes.new("ShaderNodeGroup")
        distortion_node.location = distorted_img.location + Vector((-400, 0))
        distortion_node.width = 350
        distortion_node.node_tree = distortion_shader
        links.new(distortion_node.outputs[0], distorted_img.inputs[0])
        links.new(distorted_img.outputs[0], shader_node.inputs['Fx Texture Distorted'])
        links.new(distorted_img.outputs[1], shader_node.inputs['Alpha'])
    elif socket_name == 'Emission Scroll':
        # Only on elemental weapons and obliterator.
        scroll_node = nodes.get("UV Scroll")
        if not scroll_node:
            scroll_shader = ensure_nodetree('BotW: Emission Scroll')
            scroll_node = nodes.new("ShaderNodeGroup")
            scroll_node.location = img_node.location + Vector((-400, 0))
            scroll_node.width = 350
            scroll_node.node_tree = scroll_shader
            scroll_node.name = "UV Scroll"
        if len(img_node.inputs[0].links) > 0:
            # We may have created a UV node earlier. Don't need it.
            link = img_node.inputs[0].links[0]
            uv_node = link.from_node
            links.remove(link)
            if len(uv_node.outputs[0].links) == 0:
                if len(uv_node.inputs[0].links) > 0:
                    from_node = uv_node.inputs[0].links[0].from_node
                    if from_node:
                        nodes.remove(from_node)
                nodes.remove(uv_node)
        links.new(scroll_node.outputs[0], img_node.inputs[0])
        if 'guardian' in lc_assetname or 'ancient' in lc_assetname:
            set_socket_value(shader_node, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    elif socket_name == 'SPM':
        if pixel_image.all_channels_match:
            img_node.label = "(channels match; not metal or rubber)"
        elif pixel_image.has_green:
            img_node.label = "(has green; usually metal mask)"
        else:
            img_node.label = "(no green; sketch highlight mask)"
    elif socket_name == 'Metallic':
        set_socket_value(shader_node, 'Roughness', METAL_ROUGHNESS)

def ensure_UV_node(object, material, img_node, shader_name):
    if img_node.type != 'TEX_IMAGE':
        return

    nodes = material.node_tree.nodes
    links = material.node_tree.links

    img = img_node.image
    tex_data = get_tex_data(material, img)
    if tex_data:
        pong_x = tex_data.get('WrapModeS', "Repeat") == 'Mirror'
        pong_y = tex_data.get('WrapModeT', "Repeat") == 'Mirror'
        if pong_x or pong_y:
            pingpong_node = nodes.get("PingPong UVs")
            if not pingpong_node:
                pingpong_nt = ensure_nodetree("BotW: UMii Face UVs")
                pingpong_node = nodes.new("ShaderNodeGroup")
                pingpong_node.node_tree = pingpong_nt
                pingpong_node.name = "PingPong UVs"
                pingpong_node.location = img_node.location + Vector((-400, 0))
                pingpong_node.width = 300
            if pong_x:
                set_socket_value(pingpong_node, 'PingPong X', True)
            if pong_y:
                set_socket_value(pingpong_node, 'PingPong Y', True)
            links.new(pingpong_node.outputs[0], img_node.inputs[0])
            # I think non-default WrapModes always use the first UV map, so imma just return here.
            return

    lc_img_name = img_node.image.name.lower()
    if len(object.data.uv_layers) > 1:
        uses_first_uvmap = texture_uses_first_uvmap(material, img_node.image)
        if "_alb" in lc_img_name and "damage" in lc_img_name:
            uses_first_uvmap = False
        if shader_name == 'BotW: Generic NPC' and "_ao" in lc_img_name:
            uses_first_uvmap = True
        if "clrmak" in lc_img_name or "clrmsk" in lc_img_name:
            uses_first_uvmap = True

        if not uses_first_uvmap:
            fallback_node = nodes.get("Second UV Channel")
            if not fallback_node:
                fallback_node = nodes.new(type="ShaderNodeGroup")
                fallback_nt = ensure_nodetree("BotW: UV Fallback")
                fallback_node.node_tree = fallback_nt
                fallback_node.location = img_node.location + Vector((-200, 0))
                fallback_node.name = "Second UV Channel"
                uv_node = nodes.new(type="ShaderNodeUVMap")
                uv_node.uv_map = "SPM" # UVs[1].name
                uv_node.location = fallback_node.location + Vector((-200, 0))
                links.new(uv_node.outputs[0], fallback_node.inputs[0])
            links.new(fallback_node.outputs[0], img_node.inputs[0])

def get_shader_data(material) -> dict:
    """Tried to optimize json loading by caching but it's insignificant."""
    if 'json_name' not in material:
        print_later("No shader data: ", material)
        return {}

    cache_ensure_shader_data()

    global CACHE_shader_data
    return CACHE_shader_data.get(material['json_name'], {})

def get_tex_data(material, img) -> dict:
    tex_maps = get_shader_prop_of_mat(material, 'TextureMaps')
    if not tex_maps:
        return {}
    return next((data for name, data in tex_maps.items() if name == Path(img.filepath).stem), {})

def get_alpha_mode(material) -> str:
    """Trying to guess what EEVEE alpha blending mode to use based on the 
    horrendous material data available."""

    alpha_flag = get_shader_prop_of_mat(material, 'MaterialU>RenderState>_flags') or 1

    # NOTE: The keys are all the keys that occur in the game's materials, but the values are my guesses.
    zelda_blend_modes = {
        1: 'Opaque',        # 13553 cases
        2: 'AlphaMask',     # 3785 cases
        16: 'Custom',       # 108 cases
        19: 'Translucent',  # 1249 cases
        None: 'Unknown',    # 165 cases
    }
    blend_mode = zelda_blend_modes.get(alpha_flag, "AlphaMask")

    maybe_translucency_flag = get_shader_prop_of_mat(material, 'shaderassign>options>gsys_gbuffer_xlu')
    if maybe_translucency_flag:
        return 'BLENDED'
    # shaderassign.options.uking_enable_gbuffer_xlu_blend
    # shaderassign.options.gsys_force_zprepass

    return 'BLENDED' if blend_mode == 'Translucent' else 'DITHERED'

def texture_uses_first_uvmap(material, img) -> bool or None:
    """Trying to make an educated guess but I really wish I could find a sure way to tell what texture uses what UVMap."""
    tex_data = get_tex_data(material, img)
    if not tex_data:
        return True
    tex_idx = tex_data['textureUnit'] - 1
    if tex_data['SamplerName'] == "_fx0":
        return True

    # There are some values that sound relevant but I can't find solid correlations...

    # Possible values: None, 1
    # enable_texcoord = get_shader_property(material, f'shaderassign>options>uking_enable_texcoord{<0 to 5>}')

    # Possible values: None, 1, 2, 3, 10, 11, 20, 22, 23, 104, 105, 107 (wtf...?)
    # texcoord_mapping = get_shader_property(material, f'shaderassign>options>uking_texcoord{<0 to 7>}_mapping')

    # NOTE: TotK equivalent is apparently `o_texture{tex_idx}_texcoord`.
    # Index can be from 0 to 7.
    # Values can be None, 1 to 8
    uv_idx = get_shader_prop_of_mat(material, f'shaderassign>options>uking_texture{tex_idx}_texcoord')
    # This sounds like it should refer to what UVMap is used by a texture at the given index in the texturelist
    # but the fact that it works very often is more of a coincidence of the fact that tex_idx of Albedos is usually 0
    # and the default value of uking_texture0_texcoord is usually None. So, we might as well be returning `"_Alb" in img.name`,
    # which is a bit disappointing.
    return uv_idx == None

def hookup_rgb_nodes(material, shader_node):
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    lowest_y = min((node.location.y for node in nodes), default=0)

    color_nodes = []

    for i, color in enumerate(get_color_values(material)):
        col_node = nodes.new(type='ShaderNodeRGB')
        col_node.outputs[0].default_value = color
        col_node.location = (-50, lowest_y - 300*(i+1))
        color_nodes.append(col_node)
    
    if len(color_nodes) > 0:
        # If there's at least one proper color constant, 
        # there's a very solid chance for it to be emmission color.
        # (But only if an emission mask is already plugged in, otherwise it must be somehting else.)
        if 'Emission Color' in shader_node.inputs and len(shader_node.inputs['Emission Mask'].links) > 0:
            is_albedo = False
            if 'Albedo' in shader_node.inputs:
                albedo_socket = shader_node.inputs['Albedo']
                if len(albedo_socket.links) == 0:
                    links.new(color_nodes[0].outputs[0], albedo_socket)
                    is_albedo = True
            if not is_albedo:
                links.new(color_nodes[0].outputs[0], shader_node.inputs['Emission Color'])
                set_socket_value(shader_node, "Emission Strength", 0.1)

def get_color_values(material) -> list[Vector]:
    colors = []
    matparam = get_shader_prop_of_mat(material, 'matparam')
    if not matparam:
        return colors
    for name, data in matparam.items():
        if name.startswith("const_color"):
            vec = Vector((data['ValueFloat']))
            vec.normalize()
            colors.append(vec)
    return colors

def get_shader_prop_of_mat(material, prop_path, index=None):
    shader_data = get_shader_data(material)
    if not shader_data:
        return None
    return get_shader_prop(shader_data, prop_path, index)

def get_shader_prop(shader_data, prop_path, index=None):
    prop = shader_data
    for part in prop_path.split(">"):
        if isinstance(prop, dict):
            # NOTE: "N/A" (Not Available) is used rather than None or 0 or anything else, since all of those are valid and potentially meaningful values.
            prop = prop.get(part, "N/A")
        if prop == "N/A":
            break

    if prop == "N/A":
        prop = CACHE_mat_defaults.get(prop_path, "N/A")
    if prop == "N/A":
        for key, value in CACHE_mat_defaults.items():
            if "*" in key and re.match(key.replace("*", ".*"), prop_path):
                prop = value
                break
    if prop == "N/A":
        return

    if type(prop) == list:
        if index == None and len(prop)==1:
            index = 0
        if index != None:
            return prop[index]

    return prop

def ensure_loaded_img(img_name):
    if not img_name.endswith(TEXTURE_EXTENSION):
        img_name = img_name + TEXTURE_EXTENSION

    real_img_path = get_image_path(img_name)
    if not real_img_path:
        return

    img = bpy.data.images.get(img_name)
    if img:
        img.filepath = real_img_path
    else:
        img = bpy.data.images.load(real_img_path, check_existing=True)

    if img.name in CACHE_tex_info:
        tex_info = CACHE_tex_info[img.name]
        img['is_single_color'] = tex_info['is_single_color']
        img['has_red'] = tex_info['has_red']
        img['has_green'] = tex_info['has_green']
        img['has_blue'] = tex_info['has_blue']
        img['has_alpha'] = tex_info['has_alpha']
        img['average_color'] = tex_info['average_color']
        img['all_channels_match'] = tex_info['all_channels_match']
    else:
        print_later(f"Couldn't find in texture info cache: {img.name}")

    if img.name != img_name:
        try:
            img.name = img_name
        except AttributeError:
            # Sometimes it's read-only, I think it's when it's a linked texture or something?
            print_later(f"Couldn't rename texture: {img.name}")

    return img

def set_shader_socket_values(collection, obj, material, shader_node, spm_has_green):
    lc_matname = material.name.lower()
    lc_obname = obj.name.lower()
    lc_dirname = (collection.get('dirname') or "").lower()
    lc_assetname = (collection.get('asset_name') or "").lower()

    links = material.node_tree.links

    metal, rubber = False, False
    rubbery_words = ['rubber']
    if spm_has_green:
        if any([word in lc_obname for word in rubbery_words]):
            rubber = True
        else:
            # If there's an SPM green channel and it's not for rubber, then it's for metal.
            metal = True
    if "arrow" in lc_dirname:
        metal = True

    # Hardcode some other values.
    if collection['asset_name'] == "Majora's Mask":
        rubber, metal = True, False
        if 'eye' in lc_matname:
            set_socket_value(shader_node, 'Emission Color', [0.026384, 0.485653, 0.003931, 1.000000])
        else:
            set_socket_value(shader_node, 'Emission Color', [0.513624, 0.105036, 0.022513, 1.000000])
    if 'ancient' in lc_assetname:
        set_socket_value(shader_node, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    if material['import_name'] in ('Mt_Lens', 'Mt_Glass'):
        # TODO: Could probably hunt down a more reliable way to catch glass.
        # This catches Tingle's clockface and Hylian glasses. I know there's also some glass outside of one of the tech labs.
        set_socket_value(shader_node, 'Alpha', 0.05)
    if collection['asset_name'] == 'Fierce Deity Mask' and material['import_name'] == 'Mt_Eyeemm':
        set_socket_value(shader_node, 'Emission Color', [0.700000, 0.700000, 0.700000, 1.000000])
        set_socket_value(shader_node, 'Emission Mask', 1.0)
        if shader_node.inputs['Emission Mask'].links:
            links.remove(shader_node.inputs['Emission Mask'].links[0])
    if 'Hylian Hair' in collection['asset_name'] or 'Hylian Child Hair' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo', [0.833908, 0.530669, 0.151620, 1.000000])
    if 'Hylian Beard' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo', [0.314406, 0.314406, 0.314406, 1.000000])
    if 'Hylian Glasses' in collection['asset_name']:
        set_socket_value(shader_node, 'Tint 0 Color', [0.023805, 0.023805, 0.023805, 1.000000])
        set_socket_value(shader_node, 'Metal', True)
    if 'Hylian Nose' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo Tint', [0.291138, 0.190097, 0.088846, 1.000000])

    if shader_node.node_tree.name == 'BotW: Material Blend':
        # Transparent edges are used by meshes that sometimes help blend between different terrain objects.
        # (But idk yet how to detect them. The commented line below had way too many false positives.)
        # set_socket_value(shader_node, "Transparent Edges", get_shader_prop_of_mat(material, 'isTransparent') or False)
        ensure_edge_attribute(bpy.context, obj)
        # Whenever the moss is used it just looks way too much/bad and idk how to fix it, let's just turn it down.
        albedo = get_albedo_img_node(material)
        if albedo.image and 'Moss' in albedo.image.name or 'MaterialAlb_Slice_8' in albedo.image.name:
            set_socket_value(shader_node, "Blend 1 Factor", 0)

    if shader_node.node_tree.name == 'BotW: Fauna':
        # Interpreting `uking_enable_backface_modify` as backface culling seems to do more harm than good.
        # On the leaves it's no longer necessary since I use Displacement to pull apart z-fighting planes,
        # and this value is set on branch materials which are obviously double-sided in-game.
        # material.use_backface_culling = get_shader_property(material, 'shaderassign.options.uking_enable_backface_modify') == 1
        wind_intensity = get_shader_prop_of_mat(material, "matparam>uking_wind_vtx_transform_intensity>ValueFloat")
        if wind_intensity:
            set_socket_value(shader_node, 'Wind Intensity', min(wind_intensity, 0.1))
        wind_use_height = get_shader_prop_of_mat(material, "shaderassign>options>uking_enable_wind_vtx_transform_height")
        if not wind_use_height:
            albedo = get_albedo_img_node(material)
            if albedo and albedo.image and os.path.splitext(albedo.image.name)[0] in WIND_FORCE_USE_HEIGHT:
                wind_use_height = True
        if wind_use_height:
            # Store how high the object reaches above the origin. This value is then used in the Fauna shader.
            set_socket_value(shader_node, 'Wind Use Height', True)
        alb_node = get_albedo_img_node(material)
        if alb_node and alb_node.image:
            img_name = os.path.splitext(alb_node.image.name)[0]
            if img_name in LEAF_WIND_UV_ROTATIONS:
                set_socket_value(shader_node, 'Wind UV Rotation', radians(LEAF_WIND_UV_ROTATIONS[img_name]))

    if get_shader_prop_of_mat(material, 'shaderassign>options>uking_specular_hair')==402:
        set_socket_value(shader_node, "Hair", True)
    for socket_name, value in (('Rubber', rubber), ('Metal', metal)):
        set_socket_value(shader_node, socket_name, value)

def set_socket_value(group_node, socket_name, socket_value, output=False):
    socket = group_node.inputs.get(socket_name)
    if not socket or output:
        socket = group_node.outputs.get(socket_name)
    if socket:
        socket.default_value = socket_value

def ensure_edge_attribute(context, object):
    if 'edge' in object.data.attributes:
        return

    edge_nt = ensure_nodetree("Mark Edges")
    gn_modifier = object.modifiers.new("Store Edge Attribute", "NODES")
    gn_modifier.node_group = edge_nt
    with context.temp_override(active_object=object):
        bpy.ops.object.modifier_apply(modifier=gn_modifier.name)

def ensure_nodetree(nodetree_name) -> bpy.types.NodeTree:
    """Append node tree from resources.blend, unless they already exist in this file.
    Also de-duplicate resulting light objects and nested node trees.
    """
    abs_path = get_resources_blend_path()
    # Check if it already exists locally.
    existing_nt = bpy.data.node_groups.get(nodetree_name)
    if existing_nt:
        # NodeTree exists, so just return it.
        return existing_nt

    # Import NodeTree from resources.blend file.
    prefs = get_addon_prefs()
    link = prefs.resource_append_mode=='LINK'
    with bpy.data.libraries.load(abs_path, link=link, relative=True) as (
        data_from,
        data_to,
    ):
        for nt in data_from.node_groups:
            if nt == nodetree_name:
                data_to.node_groups.append(nt)

    new_nt = bpy.data.node_groups.get(nodetree_name)

    for nt in bpy.data.node_groups[:]:
        if nt.name.startswith("BotW") and nt.name.endswith(".001"):
            other = bpy.data.node_groups.get(nt.name[:-4])
            if other:
                nt.user_remap(other)
                bpy.data.node_groups.remove(nt)

    return new_nt

def refresh_images():
    for m in bpy.data.materials:
        if not m.node_tree:
            continue
        for n in m.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                n.image = n.image

def fix_material_viewport_display(mat):
    if mat.library:
        return
    mat.metallic = 0
    mat.roughness = 0.8
    mat.diffuse_color = [0.8, 0.8, 0.8, 1.0]
    if not mat.use_nodes:
        return
    albedo_node = get_albedo_img_node(mat)
    if albedo_node:
        mat.node_tree.nodes.active = albedo_node
    average_color = get_average_albedo_color(mat)
    if average_color:
        average_color = Color(average_color[:3])
        if average_color.s < 0.4:
            average_color.s = 0.4
        if average_color.v < 0.4:
            average_color.v = 0.4
        mat.diffuse_color = (average_color.r, average_color.g, average_color.b, 1.0)

def set_object_color(obj):
    if obj.type != 'MESH':
        return
    if len(obj.data.materials) == 0:
        return
    mat = obj.data.materials[0]
    if mat:
        obj.color = obj.data.materials[0].diffuse_color
    obj.data.uv_layers.active_index = 0

def get_average_albedo_color(material) -> tuple or None:
    albedo_socket = get_albedo_socket(material)
    if not albedo_socket:
        return material.diffuse_color
    if len(albedo_socket.links) == 0:
        return albedo_socket.default_value
    albedo_node = albedo_socket.links[0].from_node
    if albedo_node.type != 'TEX_IMAGE' or albedo_node.image == None:
        return
    if 'average_color' in albedo_node.image:
        return albedo_node.image['average_color'].to_list()
    pixel_image = PixelImage.from_blender_image(albedo_node.image)
    average_color = pixel_image.average_color
    albedo_node.image['average_color'] = average_color
    return pixel_image.average_color

def get_albedo_socket(material):
    if not material.use_nodes:
        return
    nodes = material.node_tree.nodes
    output_node = next((n for n in nodes if n.type=='OUTPUT_MATERIAL'), None)
    if not output_node:
        return
    if len(output_node.inputs[0].links) == 0:
        return
    shader_node = output_node.inputs[0].links[0].from_node
    albedo_socket = shader_node.inputs.get('Albedo')
    return albedo_socket # can be None.

def get_albedo_img_node(material) -> bpy.types.ShaderNodeTexImage or None:
    if not material.use_nodes:
        return
    albedo_socket = get_albedo_socket(material)
    if not albedo_socket or len(albedo_socket.links) == 0:
        return
    albedo_node = albedo_socket.links[0].from_node
    if albedo_node.type != 'TEX_IMAGE':
        return
    return albedo_node

### Registry

def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="BotW (.dae & .fbx)")

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
