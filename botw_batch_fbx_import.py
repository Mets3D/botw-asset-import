import bpy, os, re, json
import math
from collections import OrderedDict
from math import pi
from pathlib import Path

from mathutils import Vector
from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from .asset_names import asset_names
from .collections import ensure_collection, set_active_collection
from .widgets import ensure_widget, get_resources_blend_path
from .prefs import get_addon_prefs

PRINT_LATER = []

# These things are case-sensitive but it shouldn't matter.
ICON_EXTENSION = ".jpg"
TEXTURE_EXTENSION = ".png"

DYES = ["Default", "Blue", "Red", "Yellow", "White", "Black", "Purple", "Green", "Light Blue", "Navy", "Orange", "Peach", "Crimson", "Light Yellow", "Brown", "Gray"]

OBJ_PREFIXES = ["Obj_", "TwnObj_", "TwnObjVillage_", "FldObj_", "DgnObj_", "DgnMrgPrt_"]
PRIMITIVE_NAMES = ["_polySurface", "_pCylinder", "_pSphere", "_pCube", "_pCone", "_pPlane", "pSolid"]


def print_later(*msg):
    PRINT_LATER.append("".join(str(msg)))

def camel_to_spaces(str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str)

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all .dae & .fbx files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW .dae + .fbx"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(name="Folder Path", subtype='DIR_PATH')

    def execute(self, context):
        global PRINT_LATER
        PRINT_LATER = []
        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

        prefs = get_addon_prefs(context)

        ensure_botw_scene_settings(context)

        root_dir_name = self.directory.split(os.sep)[-2]

        # First we walk through the folders and make a mapping of all images from 
        # their name to their filepath in the Models directory.
        # This has to be done in advance before importing meshes because many meshes
        # don't have the necessary textures next to them.
        # Hopefully the user has specified a folder with an extracted Models folder in the add-on prefs, 
        # otherwise we just use the selected folder and hope for the best.
        image_map = dict()
        for root, _subfolders, files in os.walk(prefs.game_models_folder or self.directory):
            image_map.update(map_img_filename_to_path(root, files))

        counter = 0
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
                import_and_setup_single_dae(context, filepath, dae_file, asset_name, parent_coll, counter, image_map)
            counter += 1

        for lateprint in PRINT_LATER:
            print(lateprint)

        bpy.ops.outliner.orphans_purge()

        deduplicate_materials()
        refresh_images()

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

def import_and_setup_single_dae(context,  filepath, filename, asset_name, parent_coll, counter=0, image_map={}):
    dirname = os.path.basename(os.path.dirname(filepath))

    # Create the collection and set it as active so all the objects get imported there to begin with.
    collection = ensure_collection(context, asset_name, parent=parent_coll)
    collection.asset_mark()
    collection['dirname'] = dirname
    collection['asset_name'] = asset_name
    collection['file_name'] = filename.replace(".dae", "")
    set_active_collection(context, collection)

    objs = import_dae(context, filepath, discard_types=('EMPTY'))
    objs = import_and_merge_fbx_data(context, dae_objs=objs, dae_path=filepath, asset_name=asset_name)
    if not objs:
        return

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
            if obj.name[-4] == ".":
                orig_name = obj.name[:-4]
            obj['import_name'] = orig_name
            if "_Mt_" in obj.name:
                split = obj.name.split("_Mt_")
                obj.name = asset_name + "_" + split[0]
                for primitive in PRIMITIVE_NAMES:
                    if primitive in obj.name:
                        obj.name = asset_name + "_" + split[1]
                if obj.name.endswith("_"):
                    obj.name = obj.name[:-1]
            else:
                print_later("Couldn't rename object: ", obj.name)
            for primitive in PRIMITIVE_NAMES:
                if primitive in obj.name:
                    obj.name = obj.name.split(primitive)[0]
            if obj.name.endswith("_Root"):
                obj.name = obj.name[:-5]

            for m in obj.modifiers:
                if m.type == 'ARMATURE' and not m.object:
                    obj.modifiers.remove(m)
            for m in obj.data.materials:
                json_filepath = os.path.join(json_base_path, collection['file_name'] + "_" + m['import_name'] + ".json")
                if os.path.isfile(json_filepath):
                    with open(json_filepath, 'r') as json_file:
                        json_data = json.load(json_file)
                        json_data = process_json_for_blender(json_data)
                        # Store as string because Blender doesn't let us store an arbitrary structure 
                        # of lists nested inside dicts or something like that.
                        m['shader_data'] = json.dumps(json_data)
                else:
                    print_later("json file not found: ", json_filepath)

            cleanup_mesh(collection, obj, asset_name, image_map)

        obj.data.name = obj.name

def import_and_merge_fbx_data(context, *, dae_objs, dae_path, asset_name):
    """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
    fbx_path = dae_path.replace(".dae", ".fbx")
    fbx_objects = import_fbx(context, fbx_path, discard_types=('EMPTY'))
    if not fbx_objects:
        return
    fbx_armatures = [o for o in fbx_objects if o.type == 'ARMATURE']

    if not fbx_objects:
        print_later("No fbx objects imported for ", asset_name)
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
        for pb in fbx_arm.pose.bones:
            pb.custom_shape = ensure_widget('Bone')
            if pb.name in ("Face_Root"):
                for child_pb in pb.children_recursive:
                    child_pb.custom_shape_scale_xyz *= 0.1
            if any([pb.name.endswith(suf) for suf in ("_R", "_FR", "_BR", "_R_1", "_R_2")]):
                pb.custom_shape_rotation_euler.z = pi/2
            else:
                pb.custom_shape_rotation_euler.z = -pi/2
            if "Root" in pb.name:
                pb.custom_shape = ensure_widget('Root')
                pb.use_custom_shape_bone_size = False
                pb.custom_shape_rotation_euler = (-pi/2, 0, 0)

    ret_objs += fbx_armatures
    
    return ret_objs

def import_fbx(context, filepath, discard_types=('MESH', 'EMPTY')):
    return import_dae_or_fbx(context, is_dae=False, filepath=filepath, discard_types=discard_types)

def import_dae(context, filepath, discard_types=('EMPTY')):
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
                    if orig_name[-4] == ".":
                        orig_name = orig_name[:-4]
                    m['import_name'] = orig_name
                m.name += suffix
    return context.selected_objects[:]

def map_img_filename_to_path(dirpath, files):
    """Loads all PNG images which are directly in the directory."""

    images = {}
    prefs = get_addon_prefs()

    for file in files:
        if prefs.game_models_folder:
            dirpath = os.path.join(prefs.game_models_folder, os.path.basename(dirpath))
            # print_later("Directory path: ", dirpath)
        else:
            print_later("Game models folder not specified.")
        filepath = os.path.join(dirpath, file)
        if not os.path.exists(filepath):
            print_later("File does not exist: ", filepath)
            continue

        if file.lower().endswith(TEXTURE_EXTENSION):
            images[file] = filepath

    return images

def cleanup_mesh(collection, obj, asset_name, image_map):
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

        setup_material(collection, obj, mat, image_map)

def setup_material(collection, obj, material, image_map):
    """A giant function that tries to set up complete materials based on nothing but the single
    Albedo texture that (usually) gets imported with the .fbx, relying entirely on naming conventions and hardcoding."""

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

    socket_map = load_assigned_textures(material, image_map)
    assigned_textures = [img for img in list(socket_map.keys())]
    material['assigned_textures'] = str(assigned_textures)
    shader_name, guessed_textures = guess_shader_and_textures(collection, obj, material, socket_map, image_map)
    shader_node = init_nodetree(material, shader_name)

    # Create image nodes, guess UV layer by name, set image color spaces
    all_textures = assigned_textures + guessed_textures
    spm_has_green = hookup_texture_nodes(collection, material, shader_node, all_textures, socket_map)
    hookup_rgb_nodes(material, shader_node)

    set_shader_socket_values(collection, obj, material, shader_node, spm_has_green)

def load_assigned_textures(material, image_map) -> OrderedDict:
    missing_textures = []
    assigned_textures = []
    if 'shader_data' in material:
        shader_data = json.loads(material['shader_data'])
        texture_maps = shader_data["TextureMaps"]
        for tex_data in texture_maps:
            img = ensure_loaded_img(tex_data['Name'], image_map)
            if not img:
                print_later("Missing texture: ", material.name, tex_data['Name'])
                missing_textures.append(tex_data['Name'])
                continue
            if any([tup[0] == tex_data['Type'] for tup in assigned_textures]):
                # Happens sometimes, especially with "Unknown" types (which are sometimes just regular Alb/Nrm/etc...).
                print_later("Duplicate assigned texture: ", material.name, tex_data['Type'], tex_data['Name'])
            type = tex_data['Type']
            if type == 'Unknown':
                sampler = tex_data['SamplerName']
                # If the material data doesn't give us the texture type, we have some fallbacks to guess.
                if '_Alb' in img.name:
                    type = 'Diffuse'
                elif '_Spm' in img.name:
                    type = 'Specular'
                elif '_Nrm' in img.name:
                    type = 'Normal'
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
            assigned_textures.append((type, img))

    if missing_textures:
        material['missing_textures'] = str(missing_textures)

    socket_map = OrderedDict()
    for type, img in assigned_textures:
        if type == 'Diffuse':
            socket_map[img] = "Albedo"
        elif type == 'Specular':
            socket_map[img] = "SPM"
        elif type == 'Normal':
            socket_map[img] = "Normal"
        elif type == 'Emission':
            socket_map[img] = "Emission Mask"
        elif type == 'AO':
            socket_map[img] = "AO"
        elif type == 'Metallic':
            socket_map[img] = "Metallic"
        else:
            # TODO: add more tex types.
            pass

    # NOTE: Don't order textures that were read from the shader data .json.
    # They might not be perfectly ordered, but they sometimes have bogus albedos, 
    # which we don't want to bring to the top.

    return socket_map

def init_nodetree(material, shader_name) -> bpy.types.ShaderNode:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Nuke the nodes as imported by .fbx, it's easier to build from scratch.
    nodes.clear()

    # Create central shader node by loading node tree from resources.blend.
    shader_node = nodes.new("ShaderNodeGroup")
    shader_node.node_tree = ensure_shader(shader_name)
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

def guess_shader_and_textures(collection, obj, material, socket_map, image_map) -> tuple[str, list[bpy.types.Image]]:
    """Guess shader type and textures based on the albedo, the object name, and so on."""
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
                if img_name not in image_map:
                    continue
                img = ensure_loaded_img(img_name, image_map)
                if img and img != node.image:
                    img.user_remap(img)
                if img and "_alb" in img.name.lower():
                    albedo = img

    # Find all other textures with the same base name.
    guessed_textures = []
    if albedo:
        textureset_name = albedo.name.split("_Alb")[0]
    else:
        textureset_name = collection['dirname']
    material['textureset_name'] = textureset_name
    for img_name, _filepath in image_map.items():
        if img_name.startswith(textureset_name):
            if "eye" in img_name.lower() and "eye" not in textureset_name.lower():
                # This avoids eg. animals using their eye textures for the body material.
                continue
            img = bpy.data.images.get(img_name)
            if img_name in image_map:
                real_img_path = image_map[img_name]
                if not img:
                    img = bpy.data.images.load(real_img_path, check_existing=True)
                img.filepath = real_img_path
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

    if any(["Blade_Fx" in img.name for img in all_textures]):
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
    for prefix in OBJ_PREFIXES:
        if collection['dirname'].startswith(prefix):
            shader_name = "BotW: Smooth Shade"

    # Order the textures nicely
    guessed_textures = order_texture_list(guessed_textures)
    return shader_name, guessed_textures

def order_texture_list(imgs: list[bpy.types.Image]) -> list[bpy.types.Image]:
    order = ["Alb", "AO", "Spm", "Nrm", "Emm", "Fx"]
    return sorted(imgs,
        key=lambda img: 
        [
            int(c) if c.isdigit() else c for c in re.split(r'(\d+)',
            str(next((i for i, word in enumerate(order) if word in img.name), -1)) + img.name)
        ]
    )

def hookup_texture_nodes(collection, material, shader_node, all_textures, socket_map) -> bool:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    shader_name = shader_node.node_tree.name
    albedo_count = 0
    dye_count = 0
    spm_has_green = False
    for i, img in enumerate(all_textures):
        img.colorspace_settings.name = guess_colorspace(material, img)

        socket_name = ""
        if img.name in socket_map:
            socket_name = socket_map[img.name]
        else:
            socket_name = guess_socket_name(img, shader_name)

        # TODO: This could be more optimized by only calculating this once per image, after loading them. But meh, it's fast enough.
        pixel_image = PixelImage.from_blender_image(img)
        if pixel_image.is_single_color and socket_name != 'Albedo':
            # If the whole image is just one color, use an RGB node instead.
            img_node = nodes.new(type="ShaderNodeRGB")
            img_node.outputs[0].default_value = pixel_image.pixels_rgba[0]
            img_node.label = img.name
        else:
            img_node = nodes.new(type="ShaderNodeTexImage")
            img_node.image = img
            img_node.width = 400

        img_node.location = (-300, (i-dye_count)*-300)

        if socket_name == 'SPM' and pixel_image.has_green and not pixel_image.all_channels_match:
            spm_has_green = True

        albedo_count, dye_count = create_helper_nodes(collection, material, img_node, pixel_image, socket_name, shader_node, albedo_count, dye_count)

        # Hook up texture to target socket on the shader node group.
        shader_socket = shader_node.inputs.get(socket_name)
        img_node.label = socket_name + " " + img_node.label
        if shader_socket:
            if len(shader_socket.links) == 0:
                links.new(img_node.outputs['Color'], shader_socket)
                if socket_name == 'Albedo':
                    nodes.active = img_node
            # Since transparency doesn't (always) get its own texture node, implicitly hook up the Alpha of the Albedo.
            if socket_name in ('Albedo', 'Fx Texture Distorted') and pixel_image.has_alpha:
                alpha_socket = shader_node.inputs.get('Alpha')
                if alpha_socket and len(alpha_socket.links) == 0 and 'Alpha' in img_node.outputs:
                    links.new(img_node.outputs['Alpha'], alpha_socket)

    return spm_has_green

def guess_socket_name(img, shader_name) -> str:
    lc_img_name = img.name.lower()
    # Guess target socket by the image name.
    
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

def create_helper_nodes(collection, material, img_node, pixel_image, socket_name, shader_node, albedo_count, dye_count):
    shader_name = shader_node.node_tree.name
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    lc_assetname = (collection.get('asset_name') or "").lower()

    ensure_UV_node(material, img_node, shader_name)

    if 'Hylian Nose' in collection['asset_name']:
        UMii_node = nodes.get("PingPong UVs")
        if not UMii_node:
            UMii_nt = ensure_shader("BotW: UMii Face UVs")
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
            eye_rig_nt = ensure_shader("BotW: Eye Rig")
            eye_rig_node = nodes.new("ShaderNodeGroup")
            eye_rig_node.node_tree = eye_rig_nt
            eye_rig_node.location = img_node.location + Vector((-400, 0))
            eye_rig_node.width = 300
            eye_rig_node.name = "Eye Rig"
        links.new(eye_rig_node.outputs[0], img_node.inputs[0])
    elif socket_name == 'Albedo' and shader_name == 'BotW: Cel Shade':
        # You can dye armors in the game, and those have different albedo textures.
        # Let's stack them above the default one, in a compact way.
        if albedo_count > 0:
            dye_count += 1
            img_node.label = str(albedo_count)# + ": " + DYES[albedo_count]
            img_node.location = (-300, dye_count*60)
            img_node.hide = True
        albedo_count += 1
    elif socket_name == 'Fx Texture':
        distorted_img = nodes.new("ShaderNodeTexImage")
        distorted_img.image = img_node.image
        distorted_img.width = img_node.width
        distorted_img.location = img_node.location + Vector((0, -300))
        distortion_shader = ensure_shader('BotW: Ancient Weapon Blade Heat Distortion')
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
            scroll_shader = ensure_shader('BotW: Emission Scroll')
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
                from_node = uv_node.outputs[0].links[0].from_node
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
        set_socket_value(shader_node, 'Roughness', 0.6)

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
                fallback_nt = ensure_shader("BotW: UV Fallback")
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
                pingpong_nt = ensure_shader("BotW: UMii Face UVs")
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

def get_tex_data(material, img) -> dict:
    if 'shader_data' in material:
        shader_data = json.loads(material['shader_data'])
        if 'TextureMaps' in shader_data:
            tex_maps = shader_data['TextureMaps']
            return next((t for t in tex_maps if t['Name'] == Path(img.filepath).stem), {})
    return {}

def texture_uses_first_uvmap(material, img) -> bool or None:
    """So, there's no guaranteed way to easily guess if a texture uses the 2nd UVMap,
    but there is a solid bet to guess if it is using the first UVMap.
    So if this function returns False, it will either use 2nd UVMap, or some procedural UVMap,
    such as scrolling UVs.
    """
    if 'shader_data' in material:
        shader_data = json.loads(material['shader_data'])
        tex_maps = shader_data['TextureMaps']
        tex_idx = 0
        for tex_info in tex_maps:
            if tex_info['Name'] == Path(img.filepath).stem:
                tex_idx = tex_info['textureUnit'] - 1
                break

        shader_options = shader_data['shaderassign']['options']
        # For TotK, this might have to be o_texture{tex_idx}_texcoord, but I never tried.
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
        if 'Emission Color' in shader_node.inputs:
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
    if 'shader_data' in material:
        shader_data = json.loads(material['shader_data'])
        for name, data in shader_data['matparam'].items():
            if name.startswith("const_color"):
                vec = Vector((data['ValueFloat']))
                vec.normalize()
                if vec[0] != vec[1] != vec[2]:
                    colors.append(vec)
    return colors

def ensure_loaded_img(img_name, image_map):
    if not img_name.endswith(TEXTURE_EXTENSION):
        img_name = img_name + TEXTURE_EXTENSION

    if img_name not in image_map:
        return

    real_img_path = image_map[img_name]

    existing_img = bpy.data.images.get(img_name)
    if existing_img:
        existing_img.filepath = real_img_path
    else:
        existing_img = bpy.data.images.load(real_img_path, check_existing=True)
    
    existing_img.name = img_name

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

    for socket_name, value in (('Rubber', rubber), ('Metal', metal), ('Hair', hair)):
        set_socket_value(shader_node, socket_name, value)

def set_socket_value(group_node, socket_name, socket_value, output=False):
    socket = group_node.inputs.get(socket_name)
    if not socket or output:
        socket = group_node.outputs.get(socket_name)
    if socket:
        socket.default_value = socket_value

def ensure_shader(nodetree_name) -> bpy.types.NodeTree:
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

def deduplicate_materials():
    """Crunch relevant data into a hash, then user remap if this hash already existed."""

    mat_hashes = {}
    copy_counter = {}
    for mat in bpy.data.materials:
        if not mat.use_nodes:
            continue
        out_node = next((n for n in mat.node_tree.nodes if n.type == 'GROUP_OUTPUT'), None)
        if not out_node:
            continue
        str_data = node_inputs_to_hashable(out_node)

        mat_hash = hash(str_data)
        if mat_hash in mat_hashes:
            print_later("Duplicate material: ", mat.name, mat_hashes[mat_hash].name)
            if len(mat.node_tree.nodes) < 3:
                # print_later("Fewer than 3 nodes. Won't de-duplicate.")
                pass
            mat.user_remap(mat_hashes[mat_hash])
            if mat_hash not in copy_counter:
                copy_counter[mat_hash] = 0
            copy_counter[mat_hash] += 1
        else:
            mat_hashes[mat_hash] = mat

    for mat_hash, count in copy_counter.items():
        print_later(mat_hashes[mat_hash].name, "had", count, "duplicates.")

def node_inputs_to_hashable(node) -> str:
    """Recursively collect some data towards the left of the node-tree, 
    resulting in a string that uniquely represents this node and its dependencies.
    Useful for de-duplicating node set-ups.

    Not meant for fringe cases:
    - Re-routes contribute to uniqueness
    - Node positions don't contribute to uniqueness
    - Only checks what's connected to the passed node on the left side
    - Does not check node properties that are not sockets
    """
    str_data = node.type
    if node.type == 'GROUP' and node.node_tree:
        str_data += node.node_tree.name
    elif node.type == 'TEX_IMAGE' and node.image:
        str_data += node.image.filepath

    for in_socket in node.inputs:
        str_data += in_socket.name + str(in_socket.default_value)
        for link in in_socket.links:
            str_data += "->" + node_inputs_to_hashable(link.from_node)

    return str_data

def refresh_images():
    for m in bpy.data.materials:
        if not m.node_tree:
            continue
        for n in m.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                n.image = n.image

class PixelImage:
    # Extract some very specific info about the pixel contents of a Blender image texture.

    @classmethod
    def from_blender_image(cls, bpy_img: bpy.types.Image):
        # NOTE: Careful! Accessing bpy_img.pixels many times is very slow! Copying all of it once is fast!
        pixels = bpy_img.pixels[:]
        width = bpy_img.size[0]
        height = bpy_img.size[1]

        return cls(width, height, pixels)

    def __init__(self, width, height, pixels):
        pixels = pixels[:]
        self.width = width
        self.height = height
        self.pixels_rgba = [tuple(pixels[i:i+4]) for i in range(0, len(pixels), 4)]

    def crop_to_square_content(self):
        """
        Crops the image to a square by removing empty rows/columns while 
        ensuring the final image remains square. Useful for asset thumbnails.
        """
        if not self.pixels_rgba:
            return  # No pixels to process
        
        w, h = self.width, self.height

        # Convert 1D pixel list into a 2D list (rows of pixels)
        pixel_rows = [self.pixels_rgba[i * w:(i + 1) * w] for i in range(h)]

        # Find the bounding box of non-transparent pixels
        min_x, max_x = w, 0
        min_y, max_y = h, 0

        for y, row in enumerate(pixel_rows):
            for x, pixel in enumerate(row):
                if pixel[3] > 0:  # If alpha > 0 (not transparent)
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

        # If the image is fully transparent, return an empty square
        if max_x < min_x or max_y < min_y:
            self.width = self.height = 0
            self.pixels_rgba = []
            return

        # Calculate the bounding box width and height
        content_width = max_x - min_x + 1
        content_height = max_y - min_y + 1

        # Determine the square size
        square_size = max(content_width, content_height)

        # Expand the bounding box to make it square
        extra_w = (square_size - content_width) // 2
        extra_h = (square_size - content_height) // 2

        start_x = max(0, min_x - extra_w)
        end_x = min(w, start_x + square_size)

        start_y = max(0, min_y - extra_h)
        end_y = min(h, start_y + square_size)

        # Extract the square pixels
        cropped_grid = [row[start_x:end_x] for row in pixel_rows[start_y:end_y]]

        # Update image data
        self.width = square_size
        self.height = square_size
        pixels_rgba = [pixel for row in cropped_grid for pixel in row]
        if len(pixels_rgba) < square_size*square_size:
            # Pad empty pixels if we're missing any to fill out the full square with data.
            pixels_rgba += [(0, 0, 0, 0)] * (square_size*square_size - len(pixels_rgba))
        self.pixels_rgba = pixels_rgba

    def downscale_to_fit(self, max_size=256):
        """
        Downscale the image so that its width and height do not exceed max_size.
        The aspect ratio is preserved.
        """
        if self.width <= max_size and self.height <= max_size:
            return  # No need to downscale

        # Compute scale factor (preserving aspect ratio)
        scale_factor = min(max_size / self.width, max_size / self.height)
        new_width = max(1, math.floor(self.width * scale_factor))
        new_height = max(1, math.floor(self.height * scale_factor))

        # Downscale using nearest-neighbor sampling
        downsampled_pixels = []
        for y in range(new_height):
            orig_y = int(y / scale_factor)
            for x in range(new_width):
                orig_x = int(x / scale_factor)
                downsampled_pixels.append(self.pixels_rgba[orig_y * self.width + orig_x])

        # Update image properties
        self.width = new_width
        self.height = new_height
        self.pixels_rgba = downsampled_pixels

    @property
    def pixels(self):
        return [channel for pixel in self.pixels_rgba for channel in pixel]

    @property
    def pixels_rgba(self):
        return self._pixels_rgba

    @pixels_rgba.setter
    def pixels_rgba(self, value):
        # If we change the pixels, reset all the cached values.
        self._is_single_color = None
        self._has_green = None
        self._has_blue = None
        self._has_alpha = None
        self._all_channels_match = None

        self._pixels_rgba = value

    @property
    def is_single_color(self):
        if self._is_single_color == None:
            self._is_single_color = all([p==self.pixels_rgba[0] for p in self.pixels_rgba])
        return self._is_single_color

    @property
    def has_red(self):
        if self._has_red == None:
            self._has_red = any([p[0] for p in self.pixels_rgba])
        return self._has_red

    @property
    def has_green(self):
        if self._has_green == None:
            self._has_green = any([p[1] for p in self.pixels_rgba])
        return self._has_green

    @property
    def has_blue(self):
        if self._has_blue == None:
            self._has_blue = any([p[2] for p in self.pixels_rgba])
        return self._has_blue

    @property
    def has_alpha(self):
        if self._has_alpha == None:
            self._has_alpha = any([p[3] for p in self.pixels_rgba])
        return self._has_alpha

    @property
    def all_channels_match(self):
        if self._all_channels_match == None:
            self._all_channels_match = all([p[0]==p[1]==p[2]==p[3] for p in self.pixels_rgba])
        return self._all_channels_match

def process_json_for_blender(data):
    """Recursively processes JSON data for Blender ID properties:
    - Converts string numbers to integers where possible.
    - Converts large integers (outside int32 range) to strings.
    - Replaces None (JSON null) with empty string.
    - Ensures lists contain only valid Blender types.
    """
    if isinstance(data, dict):
        return {str(key): process_json_for_blender(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [process_json_for_blender(item) for item in data]
    elif isinstance(data, str):
        if data.isdigit() or (data.startswith('-') and data[1:].isdigit()):
            num = int(data)
            return num
        return data
    elif isinstance(data, int):
        return str(data) if data > 2**31 - 1 or data < -2**31 else data
    elif isinstance(data, float) or isinstance(data, bool):
        return data  # Floats & bools are fine
    elif data is None:
        return ""  # Blender does not allow None; replace with empty string
    else:
        return str(data)  # Convert anything unexpected to a string

# Register the operator
def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="BotW (.dae & .fbx)")

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
