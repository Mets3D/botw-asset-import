import bpy, os, sys, re
from math import pi

from mathutils import Vector
from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from .asset_names import asset_names
from .collections import ensure_collection, set_active_collection
from .widgets import ensure_widget, get_resources_blend_path
from .prefs import get_addon_prefs

PRINT_LATER = []

ICON_EXTENSION = ".jpg"

DYES = ["Default", "Blue", "Red", "Yellow", "White", "Black", "Purple", "Green", "Light Blue", "Navy", "Orange", "Peach", "Crimson", "Light Yellow", "Brown", "Gray"]

OBJ_PREFIXES = ["Obj_", "TwnObj_", "FldObj_", "DgnObj_", "DgnMrgPrt_"]
PRIMITIVE_NAMES = ["_polySurface", "_pCylinder", "_pSphere", "_pCube", "_pCone", "_pPlane", "pSolid"]

"""
    Notes on animations:
    Data can get lost on the way both from Switch Toolbox and to Blender. Both import and export processes require a skeleton, and if it's missing any bones that have animation data, that data will be discarded.
    It's not really possible to get around this and get the animation data directly, I mean I'm sure it's possible, but the data is stored in an extremely confusing way.
    Trust me, it is best to find the appropriate skeleton and use it for exporting and importins.

    We've added a batch animation export to Switch Toolbox. Hopefully in most cases, animation files contain a perfect skeleton. I know this is not the case for Master Cycle Zero, at least.
    TODO: add prints when an animation file does not have an ideal skeleton, and in this case, manually browse models. Although even then, it won't really work, since if an animation affects multiple armatures, I won't be able to merge the armatures in Switch Toolbox. The animation will have to be exported once for each affected rig. Maybe this is never done this way but I think it might be.

    In Blender, we've added prints to the SEAnim importer to let us know when we're importing with an armature that doesn't have all the necessary bones.
    And we have an operator to merge armatures. But this still needs a functionality to add a root bone. Or we have to go over everything with a script to add a Root bone.
"""


"""
    TODO:
    TwnObj
    FldObj
    DgnObj
    consider the DgnMrgPrt and MergedGrudge stuff but probably ignore them.

    Things I had to fix manually:
        Korok albedo colors since they're procedurally done
        Some eye materials that didn't get detected as eye materials at first (now they should, but I didn't want to re-import.)
        Barbarian set skin paint
        Moblin Mask's mesh actually exports slightly borked, some pieces are on the floor, huh.
        Similar deal with one of the generic Zora children, they had their body jewelry on the floor.
        For generic NPC meshes, set albedo tints for the materials.
        A lot of work on assembly of Hylian NPC heads.
        A lot of work on enemy materials, and setting up re-skins as separate assets with shared mesh data.
        Some animals had the wrong textures hooked up. Could've been improved in the import code, but cba.

    Things to do with final cleanup script or manual:
        Make sure resources.blend is linked from the same directory and with a relative path.
        Make sure lighting set-up is good, since we cut overall cel shaded lighting strength by 2/3rds
        Check for any image nodes with no image.

        Try to remove "A", "B" and numbers from asset names.
        Remove pointless "_Model" from obnames.
        Rename obdatas to obname
        Rename materials to the albedo name with _Alb ending, and numbering if necessary.
        Remove unnecessary .001 material name endings.
        Remove any "_###" regex match from material names.

        Make sure any uses of the Ancient Weapon Blade shader have the Alpha hooked up from the same node as the Fx Texture Distorted input rather than anything else.
        Make sure to apply transforms (first check if anything is un-applied and check if it's correct)
        Maybe remove 1-bone armatures, especially if the bone's name is just "Root" (that's a .dae importer thing, not real data from the game)
            Also remove Armature modifiers without a target.
        Re-ensure that active texture is most ideal; Albedo, or Emission, or SPM, or Normal.
        Could fairly easily de-duplicate SPM UVMap nodes
        Could try hashing pixel data to de-duplicate textures. Otherwise, compare their average color and if it falls within a threshold, list them out.
        Everything has this awful metallic viewport material from the fbx import...
        Make sure armature bone positions are reset. Plenty of cases where they imported with pose data.
        Make sure SPM and Nrm textures are non-color and Alb are sRGB (although check first). Some Emm are sRGB and some aren't, so leave those alone.
"""

def print_later(*msg):
    PRINT_LATER.append("".join(msg))

def camel_to_spaces(str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str)

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all FBX files from a selected folder recursively"""
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

        self.ensure_scene_settings(context)

        root_dir_name = self.directory.split(os.sep)[-2]

        # First we walk through the folders and make a mapping of all images from 
        # their name to their filepath in the Models directory.
        # This has to be done in advance before importing meshes because not all meshes
        # have the necessary textures next to them.
        # For example, Link's hair mesh is in Armor_Default/Armor_Default.fbx,
        # but the textures are in Link/Link_Hair_Alb.png.
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
                asset_name = figure_out_asset_name(dae_file, dirname, len(dae_files)==1)
                
                if 'Animation' in asset_name:
                    continue
                filepath = os.path.join(root, dae_file)
                self.import_and_setup_single_dae(context, filepath, dae_file, asset_name, parent_coll, counter, image_map)
            counter += 1

        for lateprint in PRINT_LATER:
            print(lateprint)

        bpy.ops.outliner.orphans_purge()
        text = bpy.data.texts.get('ensure_botw_shading_props.py')
        if text:
            exec(text.as_string())

        deduplicate_materials(context)
        unfuck_texture_references()

        return {'FINISHED'}

    def count_files_in_subdirs(self, extension) -> int:
        file_count = 0
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(extension):
                    file_count += 1
        return file_count

    def ensure_scene_settings(self, context):
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

    def import_and_setup_single_dae(self, context,  filepath, filename, asset_name, parent_coll, counter=0, image_map={}):
        dirname = os.path.basename(os.path.dirname(filepath))

        # Create the collection and set it as active so all the objects get imported there to begin with.
        collection = ensure_collection(context, asset_name, parent=parent_coll)
        set_active_collection(context, collection)

        objs = self.import_dae(context, filepath, discard_types=('EMPTY'))
        objs = self.import_and_merge_fbx_data(context, dae_objs=objs, dae_path=filepath, asset_name=asset_name)
        if not objs:
            return

        prefs = get_addon_prefs(context)

        collection.asset_mark()

        # Try to load an in-game icon for this asset, 
        # if user has specified an icon dirpath in the add-on preferences.
        if prefs.game_icons_folder:
            override = context.copy()
            override["id"] = collection
            icon_filepath = os.path.join(prefs.game_icons_folder, filename.replace(".dae", ""), filename.replace(".dae", ICON_EXTENSION))
            if os.path.exists(icon_filepath):
                with context.temp_override(**override):
                    bpy.ops.ed.lib_id_load_custom_preview(filepath=icon_filepath)

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
                obj['import_name'] = obj.name
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

                obj['dirname'] = dirname
                obj['asset_name'] = asset_name

                # Fix rotations.
                if ("UMii" in obj['dirname'] and 'hair' in obj['dirname'].lower()) or 'Backpack' in asset_name:
                    # Generic NPC hair objects are weirdly transformed...
                    obj.rotation_euler.y -= pi/2
                    obj.rotation_euler.z -= pi/2
                    if obj.parent:
                        obj.location.x = -obj.parent.location.z
                    obj.location.z = 0
                else:
                    obj.rotation_euler = (0, 0, 0)
                    for prefix in OBJ_PREFIXES:
                        if obj['dirname'].startswith(prefix):
                            obj.rotation_euler = (pi/2, 0, 0)

                self.cleanup_mesh(context, obj, asset_name, image_map)

            obj.data.name = obj.name

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        # for obj, offset in offsets:
        #     obj.location.x += offset

    def import_and_merge_fbx_data(self, context, *, dae_objs, dae_path, asset_name):
        """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
        fbx_path = dae_path.replace(".dae", ".fbx")
        fbx_objects = self.import_fbx(context, fbx_path, discard_types=('EMPTY'))
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

    def cleanup_mesh(self, context, obj, asset_name, image_map):
        assert obj.type == 'MESH'
        for uv_layer, name in zip(obj.data.uv_layers, ("Albedo", "SPM")):
            # TODO: Might need a check here to see if all coordinates are at (0,0) and remove if so.
            uv_layer.name = name
        for mat in obj.data.materials:
            orig_mat_name = mat.name
            if 'Mt_' in mat.name:
                new_mat_name = asset_name + ": " + orig_mat_name.split("Mt_")[1]
                if new_mat_name in bpy.data.materials:
                    new_mat = bpy.data.materials.get(new_mat_name)

                    mat.user_remap(new_mat)
                    mat = new_mat
                    continue
                else:
                    mat.name = new_mat_name
            obj['orig_mat_name'] = orig_mat_name

            setup_material(context, obj, mat, image_map)

    def import_fbx(self, context, filepath, discard_types=('MESH', 'EMPTY')):
        return self.import_dae_or_fbx(context, is_dae=False, filepath=filepath, discard_types=discard_types)

    def import_dae(self, context, filepath, discard_types=('EMPTY')):
        return self.import_dae_or_fbx(context, is_dae=True, filepath=filepath, discard_types=discard_types)

    def import_dae_or_fbx(self, context, *, is_dae: bool, filepath: str, discard_types = ('EMPTY')):
        suffix = "_dae" if is_dae else "_fbx"

        # Both of these functions take a "filepath" property, 
        # and both load the contents to the active collection and select all objects.
        import_func = bpy.ops.wm.collada_import if is_dae else bpy.ops.import_scene.fbx

        if not os.path.exists(filepath):
            return False
        if context.active_object:
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        enable_print(False)
        # Can't seem to suppress prints on collada, hmm.
        import_func(filepath=filepath)
        for ob in context.selected_objects[:]:
            if ob.type in discard_types:
                bpy.data.objects.remove(ob)
                continue
            ob.name += suffix
            if ob.type == 'MESH':
                for m in ob.data.materials:
                    m.name += suffix
        enable_print(True)
        return context.selected_objects[:]

def map_img_filename_to_path(dirpath, files):
    """Loads all PNG images which are directly in the directory."""

    images = {}
    prefs = get_addon_prefs()

    for file in files:
        if prefs.game_models_folder:
            dirpath = os.path.join(prefs.game_models_folder, os.path.basename(dirpath))
            print_later("Directory path: ", dirpath)
        else:
            print_later("no game models folder, yo.")
        filepath = os.path.join(dirpath, file)
        if not os.path.exists(filepath):
            print_later("File does not exist: ", filepath)
            continue

        if file.lower().endswith(".png"):
            images[file] = filepath

    return images

def figure_out_asset_name(dae_filename: str, dirname: str, is_single_file: bool):
    without_ext = dae_filename.replace(".dae", "")
    asset_name = asset_names.get(without_ext, without_ext)

    # If the asset name wasn't in the dictionary, try without any _A, _B suffixes.
    if asset_name == without_ext and (without_ext.endswith("_A") or without_ext.endswith("_B")):
        asset_name = asset_names.get(without_ext[:-2], without_ext[:-2])

    # If an asset directory only has one .dae file and its name wasn't in the asset dictionary, try the dictionary's name instead.
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

    # Most "Obj_" prefix meshes won't be in the dictionary, since they don't have any in-game strings that are exposed to the player. (non-cel shaded environment meshes)
    # So to avoid having to add all of these to the dictionary, just do some string operations.
    for prefix in OBJ_PREFIXES:
        if asset_name.startswith(prefix):
            asset_name = asset_name[len(prefix):]

    asset_name = camel_to_spaces(asset_name.replace("_", " "))

    return asset_name

def setup_material(context, obj, material, image_map):
    """A giant function that tries to set up complete materials based on nothing but the single
    Albedo texture that (usually) gets imported with the .fbx, relying entirely on naming conventions and hardcoding."""

    albedo = None
    nodes = material.node_tree.nodes
    if 'BotW Output' in nodes:
        # This material was already processed, don't process it again as that might break stuff.
        return
    links = material.node_tree.links

    lc_matname = material.name.lower()
    lc_obname = obj.name.lower()
    lc_dirname = (obj.get('dirname') or "").lower()
    lc_assetname = (obj.get('asset_name') or "").lower()
    metal, rubber, hair = False, False, False

    for suf in "LR", "RL":
        if material.name.endswith("Eyeball_"+suf[0]):
            existing = bpy.data.materials.get(material.name.replace(suf[0], suf[1]))
            if existing:
                material.user_remap(existing)
                existing.name = existing.name[:-2]
                return

    # Try to find an albedo texture. This usually imports with the fbx material.
    for node in nodes:
        if node.type == 'TEX_IMAGE':
            img_name = os.path.basename(node.image.filepath)
            if img_name not in image_map:
                continue
            real_img_path = image_map[img_name]
            existing_img = bpy.data.images.get(img_name)
            if existing_img and existing_img != node.image:
                node.image.user_remap(existing_img)
            else:
                node.image = bpy.data.images.load(real_img_path, check_existing=True)
            node.image.filepath = real_img_path
            if "_alb" in node.image.name.lower():
                albedo = node.image

    # Find all other textures with the same base name.
    texture_set = []
    if albedo:
        textureset_name = albedo.name.split("_Alb")[0]
        obj['textureset_name'] = textureset_name
    else:
        textureset_name = obj['dirname']
    for img_name, filepath in image_map.items():
        real_img_path = image_map[img_name]
        if img_name.startswith(textureset_name):
            if "eye" in img_name.lower() and "eye" not in textureset_name.lower():
                # This avoids eg. animals using their eye textures for the body material.
                continue
            img = bpy.data.images.get(img_name)
            if not img:
                img = bpy.data.images.load(real_img_path, check_existing=True)
            img.filepath = real_img_path
            texture_set.append(img)

    # Nuke the nodes as imported by .fbx, it's easier to built from scratch.
    nodes.clear()

    # Determine main shader type and filter textures based on whatever string data we have.
    main_shader = nodes.new("ShaderNodeGroup")
    shader_name = "BotW: Cel Shade"
    if "eye" in lc_obname or "eye" in obj['orig_mat_name'].lower() and "mask" not in lc_obname and "ravio" not in lc_assetname:
        shader_name = "BotW: Eye"
    if "arrow" in lc_dirname:
        if lc_dirname.endswith("_a"):
            # arrow bundles.
            if "Stone" in obj['dirname'] + obj['import_name']:
                texture_set = [img for img in texture_set if "_A_Stone" in img.name]
            else:
                texture_set = [img for img in texture_set if "_A_" in img.name and "stone" not in img.name.lower()]
        elif "Stone" in obj['dirname'] + obj['import_name']:
            texture_set = [img for img in texture_set if "stone" in img.name.lower()]
        else:
            texture_set = [img for img in texture_set if ("stone" not in img.name.lower()) and ("_A_" not in img.name)]

        metal = True

    if any(["Blade_Fx" in img.name for img in texture_set]):
        if "blade" in material.name.lower():
            shader_name = "BotW: Ancient Weapon Blade"
            texture_set = [img for img in texture_set if "Blade_Fx" in img.name]
        else:
            texture_set = [img for img in texture_set if "Blade_Fx" not in img.name]
    if any(["EmmMsk.1" in img.name for img in texture_set]) and not any([word in obj['orig_mat_name'].lower() for word in ('handle', '_02')]):
        shader_name = "BotW: Elemental Weapon"
    if any(["Emm_Emm" in img.name for img in texture_set]):
        shader_name = "BotW: Divine Eye"
    if any(["clrmak" in img.name.lower() or "clrmsk" in img.name.lower() for img in texture_set]):
        shader_name = "BotW: Generic NPC"
    for prefix in OBJ_PREFIXES:
        if obj['dirname'].startswith(prefix):
            shader_name = "BotW: Smooth Shade"

    node_tree = ensure_shader(context, shader_name)
    main_shader.node_tree = node_tree
    main_shader.location = (200, 0)
    main_shader.width = 300

    # Output node
    output_node = nodes.new("ShaderNodeOutputMaterial")
    output_node.location = (600, 0)
    output_node.name = "BotW Output"
    links.new(main_shader.outputs[0], output_node.inputs[0])

    # Order the textures nicely
    order = ["Alb", "AO", "Spm", "Nrm", "Emm", "Fx"]
    texture_set.sort(
        key=lambda img: [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', str(next((i for i, word in enumerate(order) if word in img.name), -1)) + img.name)]
    )

    # Create image nodes, guess UV layer by name, set image color spaces
    # (not sure why but I can't set image color space when loading images)
    UVs = obj.data.uv_layers
    albedo_count = 0
    dye_count = 0
    spm_has_green = False
    for i, img in enumerate(texture_set):
        # TODO: This could be more optimized by only calculating this once per image, after loading them. But meh, it's fast enough.
        pixel_image = PixelImage(img)
        if pixel_image.is_single_color:
            # If the whole image is just one color, use an RGB node instead.
            img_node = nodes.new(type="ShaderNodeRGB")
            img_node.outputs[0].default_value = pixel_image[0]
            img_node.label = img.name
        else:
            img_node = nodes.new(type="ShaderNodeTexImage")
            img_node.image = img
            img_node.width = 400

        img_node.location = (-300, (i-dye_count)*-300)
        lc_img_name = img.name.lower()

        if "alb" not in lc_img_name:
            img.colorspace_settings.name = 'Non-Color'
        if len(UVs) > 1 and len(img_node.inputs) > 0:
            use_second_uvmap = False
            if "alb" not in lc_img_name or "damage" in lc_img_name:
                use_second_uvmap = True
            if shader_name == 'BotW: Generic NPC' and "_ao" in lc_img_name:
                use_second_uvmap = False
            if "clrmak" in lc_img_name or "clrmsk" in lc_img_name:
                use_second_uvmap = False

            if use_second_uvmap:
                uv_node = nodes.get("Second UV Channel")
                if not uv_node:
                    uv_node = nodes.new(type="ShaderNodeUVMap")
                    uv_node.uv_map = UVs[1].name
                    uv_node.name = "Second UV Channel"
                    uv_node.location = img_node.location + Vector((-200, 0))
                if len(img_node.inputs) > 0:
                    links.new(uv_node.outputs[0], img_node.inputs[0])

        socket_name = ""
        # Guess target socket by names, and create helper shader nodes if needed.
        if "_alb" in lc_img_name:
            socket_name = "Albedo"
            if "_red_alb" in lc_img_name:
                socket_name = "Skin Red Albedo"
            elif "_damage_alb" in lc_img_name:
                socket_name = "Skin Damage Albedo"
            elif shader_name == 'BotW: Eye':
                # This is just here to not catch eye shadow albedo texture as a dye.
                pass
            else:
                # You can dye armors in the game, and those have different albedo textures.
                # Let's stack them above the default one, in a compact way.
                if albedo_count > 0:
                    dye_count += 1
                    img_node.label = str(albedo_count)# + ": " + DYES[albedo_count]
                    img_node.location = (-300, dye_count*60)
                    img_node.hide = True
                albedo_count += 1

        if shader_name == 'BotW: Eye':
            if "_alb" in lc_img_name or "_emm" in lc_img_name:
                if 'shadow' in lc_img_name:
                    socket_name = "Eye Shadow"
                else:
                    if len(img_node.inputs) > 0:
                        eye_rig_node = nodes.get("Eye Rig")
                        if not eye_rig_node:
                            eye_rig_nt = ensure_shader(context, "BotW: Eye Rig")
                            eye_rig_node = nodes.new("ShaderNodeGroup")
                            eye_rig_node.node_tree = eye_rig_nt
                            eye_rig_node.location = img_node.location + Vector((-400, 0))
                            eye_rig_node.width = 300
                            eye_rig_node.name = "Eye Rig"
                        links.new(eye_rig_node.outputs[0], img_node.inputs[0])
        elif "clrmak_00" in lc_img_name or "clrmsk_00" in lc_img_name:
            img_node.label = "Tint Mask 0"
            socket_name = "Tint Mask 0"
        elif "clrmak_01" in lc_img_name or "clrmsk_01" in lc_img_name:
            img_node.label = "Tint Mask 1"
            socket_name = "Tint Mask 1"
        elif "clrmak_02" in lc_img_name or "clrmsk_02" in lc_img_name:
            img_node.label = "Tint Mask 2"
            socket_name = "Tint Mask 2"
        elif "_spm" in lc_img_name:
            # TODO: Differentiate Spm, Spm.1 and Spm.2?
            socket_name = "SPM"
            if pixel_image.all_channels_match:
                img_node.label = "(channels match; not metal or rubber)"
            elif pixel_image.has_green:
                spm_has_green = True
                img_node.label = "(has green; usually metal mask)"
            else:
                img_node.label = "(no green; sketch highlight mask)"
        elif "_nrm" in lc_img_name:
            socket_name = "Normal Map"
        elif "_ao" in lc_img_name:
            socket_name = "AO"
        elif "_emm_emm" in lc_img_name:
            socket_name = "Emm_Emm"
        elif "_emmmsk_" in lc_img_name:
            # Scrolling textures for the obliterator only.
            pass
        elif "_emmmsk.2" in lc_img_name:
            # This only happens for elemental weapons and obliterator.
            # Red channel is actual emission mask, green is a gradient for how charged the weapon is,
            # but in the shader I just use a UV gradient instead of the green channel.
            socket_name = "Emission Mask"
            if 'thunder' in lc_obname:
                set_socket_value(main_shader, 'Emission Color', [0.307774, 0.416501, 0.067050, 1.000000])
            if 'frost' in lc_obname:
                set_socket_value(main_shader, 'Emission Color', [0.133354, 0.280308, 0.418654, 1.000000])

        elif "_emmmsk.1" in lc_img_name or "_emmmsk" in lc_img_name:
            # It's a scrolling texture for the glow.
            socket_name = "Emission Scroll"
            # Only on elemental weapons and obliterator.
            scroll_shader = ensure_shader(context, 'BotW: Emission Scroll')
            scroll_node = nodes.new("ShaderNodeGroup")
            scroll_node.location = img_node.location + Vector((-400, 0))
            scroll_node.width = 350
            scroll_node.node_tree = scroll_shader
            if len(img_node.inputs[0].links) > 0:
                # We may have created a UV node earlier. Don't need it.
                nodes.remove(img_node.inputs[0].links[0].from_node)
            links.new(scroll_node.outputs[0], img_node.inputs[0])
            if 'guardian' in lc_assetname or 'ancient' in lc_assetname:
                set_socket_value(main_shader, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
        elif "_emmmsk" in lc_img_name:
            # Regular scrolling textures for most of the game.
            socket_name = "Emission Scroll"
        elif "_emm" in lc_img_name:
            socket_name = "Emission Mask"
            if not pixel_image.all_channels_match:
                # If the Emm texture has colors, it can be used as the emission color as well. (eg. Ancient Arrow)
                emission_color = main_shader.inputs.get('Emission Color')
                if emission_color:
                    links.new(img_node.outputs[0], emission_color)
        elif "blade_fx" in lc_img_name:
            socket_name = "Fx Texture"
            distorted_img = nodes.new("ShaderNodeTexImage")
            distorted_img.image = img_node.image
            distorted_img.width = img_node.width
            distorted_img.location = img_node.location + Vector((0, -300))
            distortion_shader = ensure_shader(context, 'BotW: Ancient Weapon Blade Heat Distortion')
            distortion_node = nodes.new("ShaderNodeGroup")
            distortion_node.location = distorted_img.location + Vector((-400, 0))
            distortion_node.width = 350
            distortion_node.node_tree = distortion_shader
            links.new(distortion_node.outputs[0], distorted_img.inputs[0])
            links.new(distorted_img.outputs[0], main_shader.inputs['Fx Texture Distorted'])
        elif "_mtl" in lc_img_name:
            socket_name = "Metallic"
            set_socket_value(main_shader, 'Roughness', 0.6)
        elif "_msk" in lc_img_name:
            socket_name = "Alpha"

        # Hook up texture to target socket on the shader node group.
        shader_socket = main_shader.inputs.get(socket_name)
        img_node.label = socket_name + " " + img_node.label
        if shader_socket:
            if len(shader_socket.links) == 0:
                links.new(img_node.outputs['Color'], shader_socket)
                if socket_name == 'Albedo':
                    nodes.active = img_node
            if socket_name in ('Albedo', 'Fx Texture Distorted') and pixel_image.has_alpha:
                alpha_socket = main_shader.inputs.get('Alpha')
                if alpha_socket and len(alpha_socket.links) == 0:
                    links.new(img_node.outputs['Alpha'], alpha_socket)

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

    if obj['asset_name'] == "Majora's Mask":
        rubber, hair, metal = True, True, False
        if 'eye' in lc_matname:
            main_shader.inputs['Emission Color'].default_value = [0.026384, 0.485653, 0.003931, 1.000000]
        else:
            main_shader.inputs['Emission Color'].default_value = [0.513624, 0.105036, 0.022513, 1.000000]

    for socket_name, value in (('Rubber', rubber), ('Metal', metal), ('Hair', hair)):
        socket = main_shader.inputs.get(socket_name)
        if socket:
            socket.default_value = value

    # Hardcode some other values.
    if 'ancient' in lc_assetname:
        set_socket_value(main_shader, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    if 'orig_mat_name' in obj:
        if obj['orig_mat_name'] == 'Mt_Lens':
            set_socket_value(main_shader, 'Alpha', 0.05)
        if obj['asset_name'] == 'Fierce Deity Mask' and obj['orig_mat_name'] == 'Mt_Eyeemm':
            set_socket_value(main_shader, 'Emission Color', [0.700000, 0.700000, 0.700000, 1.000000])
            set_socket_value(main_shader, 'Emission Mask', 1.0)
            if main_shader.inputs['Emission Mask'].links:
                links.remove(main_shader.inputs['Emission Mask'].links[0])
    if 'Hylian Nose' in obj['asset_name']:
        img_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
        UMii_nt = ensure_shader(context, "BotW: UMii Face UVs")
        UMii_node = nodes.new("ShaderNodeGroup")
        UMii_node.node_tree = UMii_nt
        UMii_node.location = img_nodes[0].location + Vector((-400, 0))
        UMii_node.width = 300
        set_socket_value(main_shader, 'Albedo Tint', [0.291138, 0.190097, 0.088846, 1.000000])
        for img_node in img_nodes:
            links.new(UMii_node.outputs[0], img_node.inputs[0])
    if 'Hylian Hair' in obj['asset_name'] or 'Hylian Child Hair' in obj['asset_name']:
        set_socket_value(main_shader, 'Albedo', [0.039014, 0.028126, 0.006496, 1.000000])
    if 'Hylian Beard' in obj['asset_name']:
        set_socket_value(main_shader, 'Albedo', [0.314406, 0.314406, 0.314406, 1.000000])
    if 'Hylian Glasses' in obj['asset_name']:
        set_socket_value(main_shader, 'Tint 0 Color', [0.023805, 0.023805, 0.023805, 1.000000])
        set_socket_value(main_shader, 'Metal', True)

def set_socket_value(group_node, socket_name, socket_value, output=False):
    socket = group_node.inputs.get(socket_name)
    if not socket or output:
        socket = group_node.outputs.get(socket_name)
    if socket:
        socket.default_value = socket_value

def ensure_world_and_lights(context) -> bpy.types.NodeTree:
    """Append node tree from resources.blend, unless they already exist in this file.
    Also de-duplicate resulting light objects and nested node trees.
    """
    abs_path = get_resources_blend_path()
    # Check if it already exists locally.
    world = bpy.data.worlds.get('BotW Lights')
    if world:
        # NodeTree exists, so just return it.
        return world

    # Import NodeTree from resources.blend file.
    with bpy.data.libraries.load(abs_path, link=False, relative=False) as (
        data_from,
        data_to,
    ):
        for world in data_from.worlds:
            if world == 'BotW Lights':
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
    
    world = bpy.data.worlds.get('BotW Lights')
    return world

def ensure_shader(context, nodetree_name) -> bpy.types.NodeTree:
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

def deduplicate_materials(context):
    """Crunch relevant data into a hash, then user remap if this hash already existed."""

    mat_hashes = {}
    copy_counter = {}
    for mat in bpy.data.materials:
        str_data = ""
        if not mat.use_nodes:
            continue
        group = mat.node_tree.nodes.get("Group")
        if not group:
            continue
        str_data += group.node_tree.name
        for in_socket in group.inputs:
            str_data += str(in_socket.default_value)
            for link in in_socket.links:
                if link.from_node.type == 'TEX_IMAGE' and link.from_node.image:
                    str_data += link.from_node.image.filepath

        mat_hash = hash(str_data)
        if mat_hash in mat_hashes:
            print("Duplicate material: ", mat.name, mat_hashes[mat_hash].name)
            mat.user_remap(mat_hashes[mat_hash])
            if mat_hash not in copy_counter:
                copy_counter[mat_hash] = 0
            copy_counter[mat_hash] += 1
        else:
            mat_hashes[mat_hash] = mat

    for mat_hash, count in copy_counter.items():
        print(mat_hashes[mat_hash].name, "had", count, "duplicates.")

def unfuck_texture_references():
    for m in bpy.data.materials:
        if not m.node_tree:
            continue
        for n in m.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                n.image = n.image


class PixelImage(list):
    # Extract some very specific info about the pixel contents of a Blender image texture.
    def __init__(self, bpy_img: bpy.types.Image):
        # NOTE: Careful! Accessing bpy_img.pixels many times is very slow! Copying all of it once is fast!
        pixels = bpy_img.pixels[:]
        pixels = [tuple(pixels[i:i+4]) for i in range(0, len(pixels), 4)]
        super().__init__(pixels)

        self.is_single_color = all([p==self[0] for p in self])
        self.has_green = any([p[1] for p in self])
        self.has_blue = any([p[2] for p in self])
        self.has_alpha = any([p[3]!=1 for p in self])
        self.all_channels_match = all([p[0]==p[1]==p[2]==p[3] for p in self])


def enable_print(bool):
    """For suppressing prints from fbx importer and remove_doubles()."""
    if not bool:
        sys.stdout = open(os.devnull, 'w')
    else:
        sys.stdout = sys.__stdout__


# Register the operator
def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="BotW (.dae & .fbx)")

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()