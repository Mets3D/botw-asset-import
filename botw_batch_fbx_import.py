import bpy, os, re, json
from collections import OrderedDict
from math import pi
from pathlib import Path

from mathutils import Vector, Color
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from .asset_names import asset_names
from .utils.collections import ensure_collection, set_active_collection
from .widgets import ensure_widget, get_resources_blend_path
from .prefs import get_addon_prefs
from .utils.deduplicate_materials import deduplicate_materials, hash_material
from .utils.timer import Timer
from .utils.pixel_image import PixelImage
from .dae_fixer import fix_dae_uvmaps_in_place

PRINT_LATER = []

# These things are case-sensitive but it shouldn't matter.
ICON_EXTENSION = ".jpg"
TEXTURE_EXTENSION = ".png"

DYES = ["Default", "Blue", "Red", "Yellow", "White", "Black", "Purple", "Green", "Light Blue", "Navy", "Orange", "Peach", "Crimson", "Light Yellow", "Brown", "Gray"]
OBJ_PREFIXES = ["Obj_", "TwnObj_", "TwnObjVillage_", "FldObj_", "DgnObj_", "DgnMrgPrt_"]
PRIMITIVE_NAMES = ["_polySurface", "_pCylinder", "_pSphere", "_pCube", "_pCone", "_pPlane", "pSolid", "_plantroot", "_pPipe"]
GARBAGE_MATS = ["InsideArea", "InsideMat"]
TEX_SUFFIXES = ["_Alb", "_Spm", "_Nrm", "_Emm", "_Emm", "_Clr", "_Mtl"]

METAL_ROUGHNESS = 0.6

_shader_data_cache = {}
_image_path_cache = {}
def cache_image_paths() -> dict[str, str]:
    """Create a mapping from image names to full filepaths in the Game Models folder."""

    global _image_path_cache
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
                _image_path_cache[file[:-len(TEXTURE_EXTENSION)]] = filepath

    return _image_path_cache

def get_image_path(image_name: str) -> str:
    if not _image_path_cache:
        with Timer("Image path cache"):
            cache_image_paths()
    # Allow passing a full path, why not.
    image_name = Path(image_name).stem
    return _image_path_cache.get(image_name, "")

def print_later(*msg):
    PRINT_LATER.append("".join([str(m) for m in msg]))

def camel_to_spaces(str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str)

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all .dae & .fbx files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW .dae + .fbx"
    bl_options = {'REGISTER', 'UNDO'}

    directory: bpy.props.StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE', 'HIDDEN'})

    def execute(self, context):
        global PRINT_LATER
        PRINT_LATER = []

        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

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
            if len(dae_files) > 1:
                parent_coll_name = root.split(os.sep)[-1]
                if root_dir_name != parent_coll_name:
                    parent_coll_name = asset_names.get(parent_coll_name, parent_coll_name)
                    parent_coll = ensure_collection(context, parent_coll_name)
            for dae_file in dae_files:
                asset_name = derive_asset_name(dae_file, dirname, len(dae_files)==1)

                if 'Animation' in asset_name:
                    continue
                filepath = os.path.join(root, dae_file)
                with Timer("Full Import", dae_file):
                    imported_objects += import_and_setup_single_dae(context, filepath, dae_file, asset_name, parent_coll, counter)
            counter += 1

        for lateprint in PRINT_LATER:
            print(lateprint)

        deduplicate_materials(imported_objects)
        bpy.ops.outliner.orphans_purge()
        refresh_images()

        # Dump cache, otherwise it's easy to run out of RAM on subsequent imports.
        PixelImage.cache = {}
        Timer.summarize()

        return {'FINISHED'}

def derive_asset_name(dae_filename: str, dirname: str, is_single_file: bool) -> str:
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

    # Most "Obj_" prefix meshes won't be in the dictionary, since they don't have any in-game strings 
    # that are exposed to the player. (non-cel shaded environment meshes)
    # So to avoid having to add all of these to the dictionary, just do some string operations.
    for prefix in OBJ_PREFIXES:
        if asset_name.startswith(prefix):
            asset_name = asset_name[len(prefix):]

    asset_name = camel_to_spaces(asset_name.replace("_", " "))
    asset_name = asset_name.replace("  ", " ").replace("D L C", "DLC")

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
    for ob in bpy.data.objects[:]:
        if 'LGT-botw' in ob.name:
            if ob.name.endswith(".001"):
                existing = bpy.data.objects.get(ob.name[:-4])
                ob.user_remap(existing)
                bpy.data.objects.remove(ob)
                ob = existing
            if ob not in set(context.scene.collection.all_objects):
                context.scene.collection.objects.link(ob)
    
    world = bpy.data.worlds.get(WORLD_NAME)
    return world

def import_and_setup_single_dae(context,  filepath, filename, asset_name, parent_coll, counter=0) -> list[bpy.types.Object]:
    dirname = os.path.basename(os.path.dirname(filepath))

    prefs = get_addon_prefs()

    # Create the collection and set it as active so all the objects get imported there to begin with.
    collection = ensure_collection(context, asset_name, parent=parent_coll)
    collection.asset_mark()
    collection['dirname'] = dirname
    collection['asset_name'] = asset_name
    collection['file_name'] = filename.replace(".dae", "")
    if not prefs.rename_collections:
        collection.name = collection['file_name']
    set_active_collection(context, collection)

    with Timer("Import .dae + .fbx", asset_name):
        objs = import_dae(context, filepath, discard_types=('EMPTY'))
        objs = import_and_merge_fbx_data(context, dae_objs=objs, dae_path=filepath, asset_name=asset_name)
    if not objs:
        return []

    # Try to load an in-game icon for this asset, 
    # if user has specified an icon dirpath in the add-on preferences.
    prefs = get_addon_prefs(context)
    if prefs.game_icons_folder:
        override = context.copy()
        override["id"] = collection
        icon_filepath = os.path.join(prefs.game_icons_folder, filename.replace(".dae", ""), filename.replace(".dae", ICON_EXTENSION))
        if os.path.exists(icon_filepath):
            with context.temp_override(**override):
                bpy.ops.ed.lib_id_load_custom_preview(filepath=icon_filepath)

    json_base_path = os.path.dirname(filepath)
    if prefs.game_models_folder:
        json_base_path = os.path.join(prefs.game_models_folder, dirname)

    offsets = {}
    dae_textures = get_textures_used_by_dae(filepath)
    for obj in context.selected_objects:
        if obj.type == 'ARMATURE':
            offsets[obj] = counter
            if obj.animation_data and obj.animation_data.action:
                obj.animation_data.action = None
            if len(obj.data.bones) < 2:
                bpy.data.objects.remove(obj)
                continue
        elif obj.type == 'MESH':
            orig_name = obj.name
            obj['import_name'] = orig_name
            if prefs.rename_objects:
                if obj.name[-4] == ".":
                    orig_name = obj.name[:-4]
                if "_Mt_" in obj.name:
                    split = obj.name.split("_Mt_")
                    obj.name = asset_name + "_" + split[0]
                    for primitive in PRIMITIVE_NAMES:
                        if primitive in obj.name:
                            obj.name = asset_name + "_" + split[1]
                    if obj.name.endswith("_"):
                        obj.name = obj.name[:-1]
                else:
                    print_later(f"Couldn't rename object: {obj.name}")
                for primitive in PRIMITIVE_NAMES:
                    if primitive in obj.name:
                        obj.name = obj.name.split(primitive)[0]
                if obj.name.endswith("_Root"):
                    obj.name = obj.name[:-5]

            for m in obj.modifiers:
                if m.type == 'ARMATURE' and not m.object:
                    obj.modifiers.remove(m)

            for m in obj.data.materials:
                m['dae_textures'] = dae_textures.get(m['import_name'], [])
                json_filepath = os.path.join(json_base_path, collection['file_name'] + "_" + m['import_name'] + ".json")
                if os.path.isfile(json_filepath):
                    with open(json_filepath, 'r') as json_file:
                        json_data = json.load(json_file)
                        json_data = tweak_material_json(json_data)
                        # Store as string because Blender doesn't let us store 
                        # an arbitrary structure of lists/dicts.
                        m['shader_data'] = json.dumps(json_data)
                else:
                    print_later(f"Couldn't find material .json: {json_filepath}")

            cleanup_mesh(collection, obj, asset_name)

            if any([s in obj.name for s in GARBAGE_MATS]):
                obj.hide_viewport, obj.hide_render = True, True

        obj.data.name = obj.name

    return context.selected_objects[:]

def import_and_merge_fbx_data(context, *, dae_objs, dae_path, asset_name):
    """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
    fbx_path = dae_path.replace(".dae", ".fbx")
    fbx_objects = import_fbx(context, fbx_path, discard_types=('EMPTY'))
    if not fbx_objects:
        return
    fbx_armatures = [o for o in fbx_objects if o.type == 'ARMATURE']

    if not fbx_objects:
        print_later(f"Couldn't find .fbx file for {dae_path}")
        return dae_objs

    ret_objs = dae_objs[:]

    for dae_obj in dae_objs:
        dae_obj.select_set(True)
        if dae_obj.type != 'MESH':
            continue
        fbx_obj = bpy.data.objects.get(dae_obj.name.replace("_dae", "_fbx"))
        if not fbx_obj:
            continue
        for dae_mat, fbx_mat in zip(dae_obj.data.materials, fbx_obj.data.materials):
            dae_mat.user_remap(fbx_mat)
            fbx_mat.name = fbx_mat.name.replace("_fbx", "")
        dae_obj.name = dae_obj.name.replace("_dae", "")
        bpy.data.objects.remove(fbx_obj)

    dae_armatures = [ob for ob in context.selected_objects if ob.type=='ARMATURE']

    for fbx_arm, dae_arm in zip(fbx_armatures, dae_armatures):
        dae_arm.user_remap(fbx_arm)
        ret_objs.remove(dae_arm)
        bpy.data.objects.remove(dae_arm)

    for fbx_arm in fbx_armatures:
        fbx_arm.name = "RIG-"+asset_name

        if 'Root' not in fbx_arm.data.bones:
            # Root bone needs to exist for animations to work.
            context.view_layer.objects.active = fbx_arm
            bpy.ops.object.mode_set(mode='EDIT')
            root = fbx_arm.data.edit_bones.new(name="Root")
            root.tail.y = 1
            for eb in fbx_arm.data.edit_bones:
                if not eb.parent and eb != root:
                    eb.parent = root
            bpy.ops.object.mode_set(mode='OBJECT')

        for pb in fbx_arm.pose.bones:
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

    ret_objs += fbx_armatures
    
    return ret_objs

def import_fbx(context, filepath, discard_types=('MESH', 'EMPTY')):
    return import_dae_or_fbx(context, is_dae=False, filepath=filepath, discard_types=discard_types)

def import_dae(context, filepath, discard_types=('EMPTY')):
    fix_dae_uvmaps_in_place(filepath)
    return import_dae_or_fbx(context, is_dae=True, filepath=filepath, discard_types=discard_types)

def import_dae_or_fbx(context, *, is_dae: bool, filepath: str, discard_types = ('EMPTY')):
    suffix = "_dae" if is_dae else "_fbx"

    # Both of these functions take a "filepath" property, 
    # and both load the contents to the active collection and select all objects.
    import_func = bpy.ops.wm.collada_import if is_dae else bpy.ops.import_scene.fbx

    if not os.path.exists(filepath):
        return False
    if context.active_object:
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    # Can't seem to suppress prints on collada, hmm.
    import_func(filepath=filepath)
    bpy.ops.transform.translate()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    for ob in context.selected_objects[:]:
        if ob.type in discard_types:
            bpy.data.objects.remove(ob)
            continue
        ob.name += suffix
        if ob.type == 'MESH':
            for m in ob.data.materials:
                if 'import_name' not in m:
                    orig_name = m.name
                    if len(orig_name) > 4 and orig_name[-4] == ".":
                        orig_name = orig_name[:-4]
                    m['import_name'] = orig_name
                m.name += suffix
    return context.selected_objects[:]

def get_textures_used_by_dae(filepath) -> dict[str, list[str]]:
    content = ""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    if not content:
        return {}

    mat_pattern = re.finditer(r'<effect id="Effect_(.*?)">.*?</effect>', content, re.DOTALL)

    image_map = {}

    for mat in mat_pattern:
        mat_name = mat.group(1)
        mat_content = mat.group(0)

        images = re.findall(r'<init_from>(.*?)</init_from>', mat_content)

        image_map[mat_name] = images

    return image_map

def cleanup_mesh(collection, obj, asset_name):
    assert obj.type == 'MESH'
    for uv_layer, name in zip(obj.data.uv_layers, ("Albedo", "SPM")):
        # TODO: Might need a check here to see if all coordinates are at (0,0) and remove if so.
        uv_layer.name = name
    for mat in obj.data.materials:
        if 'Mt_' in mat.name:
            new_mat_name = asset_name + ": " + mat.name.split("Mt_")[1]
            if new_mat_name in bpy.data.materials:
                new_mat = bpy.data.materials.get(new_mat_name)

                mat.user_remap(new_mat)
                mat = new_mat
                continue
            else:
                mat.name = new_mat_name

        with Timer("Setup material", mat.name):
            setup_material(collection, obj, mat)
            set_object_color(obj)

def setup_material(collection, obj, material):
    """A giant function that tries to set up complete materials based on nothing but the single
    Albedo texture that (usually) gets imported with the .fbx, relying entirely on naming conventions and hardcoding."""

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

    socket_map = load_assigned_textures(material)
    shader_name, socket_map = guess_shader_and_textures(collection, obj, material, socket_map)
    shader_node = init_nodetree(material, shader_name)

    # if shader_name != 'BotW: Material Blend' and len(obj.data.color_attributes) > 0:
    #     material['WARNING'] = "Unused vertex color. This material should probably use Terrain textures blended using the vertex color info."
    #     print_later(f"UNUSED VERTEX COLOR: {obj.name}")

    # Create image nodes, guess UV layer by name, set image color spaces
    with Timer("Hookup tex nodes", material.name):
        spm_has_green = hookup_texture_nodes(collection, material, shader_node, socket_map)
        hookup_rgb_nodes(material, shader_node)

    set_shader_socket_values(collection, obj, material, shader_node, spm_has_green)
    fix_material_settings(material)
    material['hash'] = hash_material(material)

def load_assigned_textures(material) -> OrderedDict[bpy.types.Image, str]:
    socket_map = load_assigned_json_textures(material)
    socket_map.update(load_assigned_dae_textures(material))
    socket_map.update(load_assigned_tile_textures(material))

    # NOTE: The order of this dictionary matters, as the first entry for each socket will win.

    return socket_map

def load_assigned_json_textures(material) -> OrderedDict[bpy.types.Image, str]:
    """If a material was assigned a 'shader_data' custom property, that's data
    we extracted from the .bmat using my modified version of Switch Toolbox.
    """
    socket_map = OrderedDict()

    missing_tex_from_json = []
    tex_from_json = []
    shader_data = get_shader_data(material)
    if not shader_data:
        return socket_map
    texture_maps = shader_data["TextureMaps"]
    for tex_data in texture_maps:
        name = tex_data['Name']
        if name in ('MaterialAlb', 'MaterialCmb'):
            continue
        img = ensure_loaded_img(name)
        if not img:
            print_later(f"Couldn't find texture: '{material.name}' -> {name}")
            missing_tex_from_json.append(name)
            continue
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
        tex_from_json.append((type, img))

    if missing_tex_from_json:
        material['missing_textures'] = str(missing_tex_from_json)

    for type, img in tex_from_json:
        # NOTE: Can add support for more shader socket names here.
        if type == 'Diffuse':
            if "_Red_Alb" in img.name:
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

def load_assigned_dae_textures(material) -> OrderedDict[bpy.types.Image, str]:
    dae_tex_names = material.get('dae_textures', [])
    tex_from_dae = [ensure_loaded_img(img_name) for img_name in dae_tex_names]
    return OrderedDict([(img, guess_socket_name(img)) for img in tex_from_dae if img])

def load_assigned_tile_textures(material) -> OrderedDict[bpy.types.Image, str]:
    """Based on https://github.com/augmero/bmubin/blob/main/scripts/asset/shader_fixer.py"""
    socket_map = OrderedDict()
    shader_data = get_shader_data(material)
    if not shader_data:
        return socket_map

    # texture_array_index has 6 integers between 0-82.
    # These definitely correspond directly to the textures inside content/Terrain,
    # and their order seems to matter too.
    matparam = shader_data.get('matparam')
    tex_array_index_props = []

    shaderoptions = shader_data['shaderassign']['options']
    shader_array_index_props = []

    for i in range(5):
        # Skipping last value on purpose because it's the same value across the whole game.
        tex_array_index_props.append(int(matparam[f'texture_array_index{i}']['ValueFloat'][0]))
        shader_array_index_props.append(shaderoptions[f'uking_texture_array_texture{i}'])

    all_default = all([v==-1 for v in shader_array_index_props])
    tex_indicies = []
    for tex_index_value, shader_array_value in zip(tex_array_index_props, shader_array_index_props):
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
        tex_indicies.append(tex_index_value)

    if not tex_indicies:
        return socket_map

    material['tile_textures'] = tex_indicies

    alb_offset = 1
    nrm_offset = 1
    for i, tex_index in enumerate(tex_indicies):
        albedo = ensure_loaded_img(f"MaterialAlb_Slice_{tex_index}_.png")
        if albedo:
            if 'Albedo' not in list(socket_map.values()):
                socket_map[albedo] = "Albedo"
                alb_offset = 0
            else:
                socket_map[albedo] = f'Albedo Blend {i+alb_offset}'
        normal = ensure_loaded_img(f"MaterialCmb_Slice_{tex_index}_.png")
        if normal:
            if 'Normal Map' not in list(socket_map.values()):
                socket_map[normal] = "Normal Map"
                nrm_offset = 0
            else:
                socket_map[normal] = f'Normal Blend {i+nrm_offset}'

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

    return shader_node

def guess_colorspace(material, img):
    """This is a dangerously simple guess, but it works surprisingly alright."""
    tex_data = get_tex_data(material, img)
    if tex_data:
        return 'Non-Color' if tex_data['Type'] != 'Diffuse' else 'sRGB'
    return 'Non-Color' if "alb" not in img.name.lower() else 'sRGB'

def guess_shader_and_textures(collection, obj, material, socket_map: OrderedDict) -> tuple[str, OrderedDict[bpy.types.Image, str]]:
    """Guess shader type and textures based on the albedo, the object name, and so on."""
    socket_map = socket_map.copy()
    lc_obname = obj.name.lower()
    lc_matname = material.name.lower()
    lc_dirname = (collection.get('dirname') or "").lower()
    lc_assetname = (collection.get('asset_name') or "").lower()

    albedo = next((img for img, socket_name in socket_map.items() if socket_name=='Albedo'), None)
    if not albedo:
        # Try to find an albedo texture that imported from the .fbx.
        nodes = material.node_tree.nodes
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                img = node.image
                if not img:
                    continue
                img_name = os.path.basename(img.filepath)
                img.name = img_name
                img = ensure_loaded_img(img_name)
                if not img:
                    continue
                if img != node.image:
                    img.user_remap(img)
                if "_alb" in img.name.lower():
                    albedo = img

    def increment_name(name: str, increment=1, default_zfill=1) -> str:
        # Increment LAST number in the name.
        # Negative numbers will be clamped to 0.
        # Digit length will be preserved, so 10 will decrement to 09.
        # 99 will increment to 100, not 00.

        # If no number was found, one will be added at the end of the base name.
        # The length of this in digits is set with the `default_zfill` param.

        numbers_in_name = re.findall(r'\d+', name)
        if not numbers_in_name:
            return name + str(max(0, increment)).zfill(default_zfill)

        last = numbers_in_name[-1]
        incremented = str(max(0, int(last) + increment)).zfill(len(last))
        split = name.rsplit(last, 1)
        return incremented.join(split)

    # Find all other textures with the same base name.
    guessed_textures = []
    if albedo:
        textureset_name = albedo.name.split("_Alb")[0]
    else:
        textureset_name = collection['dirname']
    for img_name, _filepath in _image_path_cache.items():
        if img_name.startswith(textureset_name):
            extra_name_part = img_name[len(textureset_name):]
            if not any([extra_name_part.startswith(suf) for suf in TEX_SUFFIXES]):
                # This avoids things like "Bear" ending up with textures of "Beard" and such mis-matches.
                continue
            if "eye" in img_name.lower() and "eye" not in textureset_name.lower():
                # This avoids eg. animals using their eye textures for the body material.
                continue
            img = bpy.data.images.get(img_name) or ensure_loaded_img(img_name)
            if img and img not in socket_map:
                guessed_textures.append(img)

    all_textures = list(socket_map.keys())+guessed_textures

    shader_name = "BotW: Cel Shade"
    if "eye" in lc_obname or "eye" in material['import_name'].lower() and "mask" not in lc_obname and "ravio" not in lc_assetname:
        shader_name = "BotW: Eye"
    if "arrow" in lc_dirname:
        if lc_dirname.endswith("_a"):
            # arrow bundles.
            if "Stone" in collection['dirname'] + obj['import_name']:
                guessed_textures = [img for img in guessed_textures if "_A_Stone" in img.name]
            else:
                guessed_textures = [img for img in guessed_textures if "_A_" in img.name and "stone" not in img.name.lower()]
        elif "Stone" in collection['dirname'] + obj['import_name']:
            guessed_textures = [img for img in guessed_textures if "stone" in img.name.lower()]
        else:
            guessed_textures = [img for img in guessed_textures if ("stone" not in img.name.lower()) and ("_A_" not in img.name)]
    for prefix in OBJ_PREFIXES:
        if collection['dirname'].startswith(prefix):
            shader_name = "BotW: Smooth Shade"
    if 'tile_textures' in material:
        shader_name = "BotW: Material Blend"
    elif any(["Blade_Fx" in img.name for img in all_textures]):
        if "blade" in lc_matname:
            shader_name = "BotW: Ancient Weapon Blade"
            guessed_textures = [img for img in guessed_textures if "Blade_Fx" in img.name]
        else:
            guessed_textures = [img for img in guessed_textures if "Blade_Fx" not in img.name]
    elif any(["EmmMsk.1" in img.name for img in all_textures]) and not any([word in material['import_name'].lower() for word in ('handle', '_02')]):
        shader_name = "BotW: Elemental Weapon"
    elif any(["Emm_Emm" in img.name for img in all_textures]) and 'Divine' in collection['asset_name']:
        shader_name = "BotW: Divine Eye"
    elif any(["clrmak" in img.name.lower() or "clrmsk" in img.name.lower() for img in all_textures]):
        shader_name = "BotW: Generic NPC"

    if len(obj.data.color_attributes) > 0 and shader_name != "BotW: Material Blend" and len([socket for socket in socket_map.keys() if 'Albedo' in socket]) > 1:
        shader_name = "BotW: Material Blend"
        material['WARNING'] = "Using material blend shader because there is a vertex color and >1 albedos."

    def order_texture_list(imgs: list[bpy.types.Image]) -> list[bpy.types.Image]:
        order = ["Alb", "AO", "Spm", "Nrm", "Emm", "Fx"]
        return sorted(imgs,
            key=lambda img: 
            [
                int(c) if c.isdigit() else c for c in re.split(r'(\d+)',
                str(next((i for i, word in enumerate(order) if word in img.name), -1)) + img.name)
            ]
        )

    # Order the textures nicely
    guessed_textures = order_texture_list(guessed_textures)
    if guessed_textures:
        material['guessed_textures'] = [img.name for img in guessed_textures]

    socket_map.update({img:guess_socket_name(img, shader_name) for img in guessed_textures})

    return shader_name, socket_map

def hookup_texture_nodes(collection, material, shader_node, socket_map) -> bool:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    shader_name = shader_node.node_tree.name
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
            print(img.name)
            img_node.outputs[0].default_value = pixel_image.pixels_rgba[0]
        else:
            img_node = nodes.new(type="ShaderNodeTexImage")
            img_node.image = img
            img_node.width = 400
        img_node.label = img.name

        if socket_name in ("", "Unknown"):
            socket_name = guess_socket_name(img, shader_name)

        img_node.location = (-300, i* -300)

        if socket_name == 'SPM' and pixel_image.has_green and not pixel_image.all_channels_match:
            spm_has_green = True

        albedo_count, dye_count = create_helper_nodes(collection, material, img_node, pixel_image, socket_name, shader_node, albedo_count, dye_count, use_dye_labels)

        # Hook up texture to target socket on the shader node group.
        shader_socket = shader_node.inputs.get(socket_name)

        img_node.label = socket_name + " " + img_node.label
        if not shader_socket:
            img_node.label = "No socket: " + socket_name
            print_later(f"Couldn't find shader socket: '{material.name}' -> '{socket_name}'")
            continue

        # Bit of a hack, re-direct Material Blend socket names that need to know the shader type. 
        # Could do this in load_assigned_textures, but I cba to re-organize the code to already know the shader type by the time that function runs.
        if shader_node.node_tree.name == 'BotW: Material Blend':
            # This shader blends up to 3 materials together.
            if len(shader_socket.links) > 0:
                if socket_name == 'Albedo':
                    socket_name = 'Albedo Blend 1'
                elif socket_name == 'Normal Map':
                    socket_name = 'Normal Blend 1'
                elif socket_name == 'Albedo Blend 1':
                    socket_name = 'Albedo Blend 2'
                elif socket_name == 'Normal Blend 1':
                    socket_name = 'Normal Blend 2'
                shader_socket = shader_node.inputs.get(socket_name)
                img_node.label = socket_name + " " + img_node.label

        if socket_name == "Albedo Blend 1":
            set_socket_value(shader_node, f"Blend 1 Factor", 1)

        if len(shader_socket.links) == 0:
            if shader_socket.name == 'Alpha' and not is_transparent(material):
                pass
            else:
                links.new(img_node.outputs['Color'], shader_socket)
        else:
            print_later(f"Shader socket already taken: '{material.name}' -> '{img.name}' ({socket_name})")

        if is_transparent(material) != False:
            material.surface_render_method = 'BLENDED'
        # Since transparency doesn't (always) get its own texture node, hook up the Alpha of the Albedo.
        if socket_name in ('Albedo', 'Fx Texture Distorted') and is_transparent(material) and pixel_image.has_alpha:
            alpha_socket = shader_node.inputs.get('Alpha')
            if alpha_socket and len(alpha_socket.links) == 0 and 'Alpha' in img_node.outputs:
                links.new(img_node.outputs['Alpha'], alpha_socket)

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
        if "_red_alb" in lc_img_name:
            return "Skin Red Albedo"
        elif "_damage_alb" in lc_img_name:
            return "Skin Damage Albedo"
        return "Albedo"
        
    elif "clrmak_00" in lc_img_name or "clrmsk_00" in lc_img_name:
        return "Tint Mask 0"
    elif "clrmak_01" in lc_img_name or "clrmsk_01" in lc_img_name:
        return "Tint Mask 1"
    elif "clrmak_02" in lc_img_name or "clrmsk_02" in lc_img_name:
        return "Tint Mask 2"
    elif "_spm" in lc_img_name:
        # TODO: Differentiate Spm, Spm.1 and Spm.2?
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
    elif "blade_fx" in lc_img_name:
        return "Fx Texture"
    elif "_mtl" in lc_img_name:
        return "Metallic"
    elif "_msk" in lc_img_name:
        return "Alpha"

    return ""

def create_helper_nodes(collection, material, img_node, pixel_image, socket_name, shader_node, albedo_count=0, dye_count=0, use_dye_labels=False) -> tuple[int, int]:
    shader_name = shader_node.node_tree.name
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    lc_assetname = (collection.get('asset_name') or "").lower()

    ensure_UV_node(material, img_node, shader_name)

    if 'Hylian Nose' in collection['asset_name']:
        # TODO: Test this again, this special case should no longer be necessary since we implemented .json material data.
        UMii_node = nodes.get("PingPong UVs")
        if not UMii_node:
            UMii_nt = ensure_nodetree("BotW: UMii Face UVs")
            UMii_node = nodes.new("ShaderNodeGroup")
            UMii_node.node_tree = UMii_nt
            UMii_node.name = "PingPong UVs"
            UMii_node.location = img_node.location + Vector((-400, 0))
            UMii_node.width = 300
        set_socket_value(shader_node, 'Albedo Tint', [0.291138, 0.190097, 0.088846, 1.000000])
        links.new(UMii_node.outputs[0], img_node.inputs[0])

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
    elif socket_name == 'Albedo' and shader_name == 'BotW: Cel Shade':
        if albedo_count > 0:
            dye_count += 1
            img_node.label = str(albedo_count)
            if use_dye_labels:
                img_node.label += ": " + DYES[albedo_count]
            img_node.location = (-300, dye_count*60)
            img_node.hide = True
        albedo_count += 1
    elif socket_name == 'Fx Texture':
        distorted_img = nodes.new("ShaderNodeTexImage")
        distorted_img.image = img_node.image
        distorted_img.width = img_node.width
        distorted_img.location = img_node.location + Vector((0, -300))
        distortion_shader = ensure_nodetree('BotW: Ancient Weapon Blade Heat Distortion')
        distortion_node = nodes.new("ShaderNodeGroup")
        distortion_node.location = distorted_img.location + Vector((-400, 0))
        distortion_node.width = 350
        distortion_node.node_tree = distortion_shader
        links.new(distortion_node.outputs[0], distorted_img.inputs[0])
        links.new(distorted_img.outputs[0], shader_node.inputs['Fx Texture Distorted'])
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

    return albedo_count, dye_count

def ensure_UV_node(material, img_node, shader_name):
    if img_node.type != 'TEX_IMAGE':
        return

    nodes = material.node_tree.nodes
    links = material.node_tree.links

    lc_img_name = img_node.image.name.lower()
    if len(img_node.inputs) > 0:
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

    img = img_node.image
    tex_data = get_tex_data(material, img)
    if tex_data:
        pong_x = tex_data['WrapModeS'] == 'Mirror'
        pong_y = tex_data['WrapModeT'] == 'Mirror'
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

def get_shader_data(material) -> dict:
    """Tried to optimize json loading by caching but it's insignificant."""
    if 'shader_data' not in material:
        print_later("No shader data: ", material)
        return {}
    global _shader_data_cache
    if material.name not in _shader_data_cache:
        _shader_data_cache[material.name] = json.loads(material['shader_data'])
    return _shader_data_cache[material.name]

def get_tex_data(material, img) -> dict:
    shader_data = get_shader_data(material)
    if not shader_data:
        return {}
    tex_maps = shader_data['TextureMaps']
    return next((t for t in tex_maps if t['Name'] == Path(img.filepath).stem), {})

def get_alpha_mode(material) -> str:
    """This is unfortunately not useful.
    The game uses the same Alpha blend mode for decals and objects with transparent edges; AlphaMask.
    But in Blender, decals must be set to Blended, and other objects to Dithered, otherwise decals would 
    get black z-fighting artifacts, and other objects would be weirdly translucent.

    I just go with BLENDED because decals are more common. :(
    """
    shader_data = get_shader_data(material)
    if not shader_data:
        return 'DITHERED'
    alpha_flag = shader_data['MaterialU']['RenderState']['_flags']
    
    zelda_blend_modes = ['Custom', 'Opaque', 'AlphaMask', 'Translucent']
    blend_mode = zelda_blend_modes[alpha_flag]

    return 'BLENDED' if blend_mode == 'Translucent' else 'DITHERED'

def texture_uses_first_uvmap(material, img) -> bool or None:
    """So, there's no guaranteed way to easily guess if a texture uses the 2nd UVMap,
    but there is a solid bet to guess if it is using the first UVMap.
    So if this function returns False, it will either use 2nd UVMap, or some procedural UVMap,
    such as scrolling UVs.
    """
    tex_data = get_tex_data(material, img)
    if not tex_data:
        return True
    tex_idx = tex_data['textureUnit'] - 1
    shader_data = get_shader_data(material)
    if not shader_data:
        return None
    shader_options = shader_data['shaderassign']['options']
    # For TotK, this might have to be `o_texture{tex_idx}_texcoord``, but I never tried.
    uv_idx = shader_options.get(f'uking_texture{tex_idx}_texcoord')
    return uv_idx == 0

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
    shader_data = get_shader_data(material)
    if not shader_data:
        return colors
    for name, data in shader_data['matparam'].items():
        if name.startswith("const_color"):
            vec = Vector((data['ValueFloat']))
            vec.normalize()
            if vec[0] != vec[1] != vec[2]:
                colors.append(vec)
    return colors

def is_transparent(material) -> bool or None:
    shader_data = get_shader_data(material)
    if not shader_data:
        return None
    return shader_data['isTransparent']

def ensure_loaded_img(img_name):
    if not img_name.endswith(TEXTURE_EXTENSION):
        img_name = img_name + TEXTURE_EXTENSION

    real_img_path = get_image_path(img_name)
    if not real_img_path:
        return

    existing_img = bpy.data.images.get(img_name)
    if existing_img:
        existing_img.filepath = real_img_path
    else:
        existing_img = bpy.data.images.load(real_img_path, check_existing=True)
    
    if existing_img.name != img_name:
        try:
            existing_img.name = img_name
        except AttributeError:
            # Sometimes it's read-only, I think it's when it's a linked texture or something?
            print_later(f"Couldn't rename texture: {existing_img.name}")

    return existing_img

def set_shader_socket_values(collection, obj, material, shader_node, spm_has_green):
    lc_matname = material.name.lower()
    lc_obname = obj.name.lower()
    lc_dirname = (collection.get('dirname') or "").lower()
    lc_assetname = (collection.get('asset_name') or "").lower()
    metal, rubber, hair = False, False, False

    links = material.node_tree.links

    # Set the Metal/Rubber/Hair checkboxes
    rubbery_words = ['rubber']
    hairy_words = ['hair', 'hari', 'fur', 'mane']
    if spm_has_green:
        if any([word in lc_obname for word in rubbery_words]):
            rubber = True
        else:
            # If there's an SPM green channel and it's not for rubber, then it's for metal.
            metal = True
    if any([word in lc_obname+obj['import_name'].lower() for word in hairy_words]):
        hair = True
    if "arrow" in lc_dirname:
        metal = True

    # Hardcode some other values.
    if collection['asset_name'] == "Majora's Mask":
        rubber, hair, metal = True, True, False
        if 'eye' in lc_matname:
            set_socket_value(shader_node, 'Emission Color', [0.026384, 0.485653, 0.003931, 1.000000])
        else:
            set_socket_value(shader_node, 'Emission Color', [0.513624, 0.105036, 0.022513, 1.000000])
    if 'ancient' in lc_assetname:
        set_socket_value(shader_node, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    if 'import_name' in material:
        if material['import_name'] == 'Mt_Lens':
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

    if shader_node.node_tree.name == 'BotW: Material Blend':
        set_socket_value(shader_node, "Transparent Edges", is_transparent(material))
        ensure_edge_attribute(bpy.context, obj)

    for socket_name, value in (('Rubber', rubber), ('Metal', metal), ('Hair', hair)):
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
    with bpy.data.libraries.load(abs_path, link=True, relative=True) as (
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

def tweak_material_json(data):
    """Recursively convert string numbers to integers where possible."""
    if isinstance(data, dict):
        return {str(key): tweak_material_json(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [tweak_material_json(item) for item in data]
    elif isinstance(data, str) and (data.isdigit() or (data.startswith('-') and data[1:].isdigit())):
        num = int(data)
        return num

    return data

def fix_material_settings(m):
    if m.library:
        return
    m.metallic = 0
    m.roughness = 0.8
    m.diffuse_color = [0.8, 0.8, 0.8, 1.0]
    if not m.use_nodes:
        return
    albedo_node = get_albedo_img_node(m)
    if albedo_node:
        m.node_tree.nodes.active = albedo_node
    average_color = get_average_albedo_color(m)
    if average_color:
        average_color = Color(average_color[:3])
        if average_color.s < 0.4:
            average_color.s = 0.4
        if average_color.v < 0.4:
            average_color.v = 0.4
        m.diffuse_color = (average_color.r, average_color.g, average_color.b, 1.0)

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
    albedo_node.image['average_color'] = pixel_image.average_color
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

# Register the operator
def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="BotW (.dae & .fbx)")

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
