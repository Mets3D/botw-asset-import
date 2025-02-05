import bpy
import os, sys
from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper
import numpy as np
from .asset_names import asset_names
from .collections import ensure_collection
from .widgets import ensure_widget
from math import pi

PRINT_LATER = []

def print_later(*msg):
    PRINT_LATER.append("".join(msg))


class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all FBX files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW assets from folders of .dae and optionally .fbx files (the armature will be taken from the latter if present)"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(name="Folder Path", subtype='DIR_PATH')

    def execute(self, context):
        global PRINT_LATER
        PRINT_LATER = []
        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

        self.ensure_scene_settings(context)

        root_dir_name = self.directory.split(os.sep)[-2]

        # First we walk through the folders and import all images.
        # This has to be done in advance before importing meshes because not all meshes
        # have the necessary textures next to them.
        # For example, Link's hair mesh is in Armor_Default/Armor_Default.fbx,
        # but the textures are in Link/Link_Hair_Alb.png.

        for root, subfolders, files in os.walk(self.directory):
            for dirname in subfolders:
                load_png_images_from_directory(os.path.join(root, dirname))

        for root, dirname, files in os.walk(self.directory):
            dae_files = [f for f in files if f.lower().endswith(".dae")]
            parent_coll = None
            if len(dae_files) > 1:
                parent_coll_name = root.split(os.sep)[-1]
                if root_dir_name != parent_coll_name:
                    parent_coll_name = asset_names.get(parent_coll_name, parent_coll_name)
                    parent_coll = ensure_collection(context, parent_coll_name)
            for dae_file in dae_files:
                without_ext = dae_file.replace(".dae", "")
                asset_name = asset_names.get(without_ext, without_ext)
                if asset_name == without_ext and (without_ext.endswith("_A") or without_ext.endswith("_B")):
                    asset_name = asset_names.get(without_ext[:-2], without_ext[:-2])
                filepath = os.path.join(root, dae_file)
                self.import_and_setup_single_dae(context, filepath, dae_file, asset_name, parent_coll)

        for lateprint in PRINT_LATER:
            print(lateprint)

        return {'FINISHED'}

    def count_files_in_subdirs(self, extension) -> int:
        file_count = 0
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(extension):
                    file_count += 1
        return file_count

    def ensure_scene_settings(self, context):
        # Set sRGB view transform, as that's what the game probably uses.
        context.scene.view_settings.view_transform = 'Standard'

        # Set viewport shading to the BotW MatCap.
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces.active.shading.type = 'SOLID'
                area.spaces.active.shading.light = 'MATCAP'
                area.spaces.active.shading.studio_light = 'botw.exr'
                area.spaces.active.shading.color_type = 'TEXTURE'

    def import_and_setup_single_dae(self, context,  filepath, filename, asset_name, parent_coll):
        objs = self.import_dae(context, filepath, discard_types=('EMPTY'))
        objs = self.import_and_merge_fbx_data(context, dae_objs=objs, dae_path=filepath, asset_name=asset_name)

        collection = ensure_collection(context, asset_name, parent=parent_coll)

        for obj in objs:
            collection.objects.link(obj)
            obj.select_set(True)

            if obj in set(context.scene.collection.objects):
                # This happens for the FBX armatures.
                context.scene.collection.objects.unlink(obj)

            if obj.type == 'ARMATURE':
                if obj.animation_data and obj.animation_data.action:
                    obj.animation_data.action = None
            elif obj.type == 'MESH':
                obj['import_name'] = obj.name
                if "Mt_" in obj.name:
                    split = obj.name.split("_Mt_")
                    obj.name = asset_name + "_" + split[0]
                    if obj.name.endswith("_"):
                        obj.name = obj.name[:-1]
                else:
                    # Shame this print gets lost in collada import spam, sigh.
                    print("Couldn't rename object: ", obj.name)
                self.cleanup_mesh(obj, asset_name)

            obj.data.name = obj.name

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    def import_and_merge_fbx_data(self, context, *, dae_objs, dae_path, asset_name):
        """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
        fbx_path = dae_path.replace(".dae", ".fbx")
        fbx_objects = self.import_fbx(context, fbx_path, discard_types=('EMPTY'))
        fbx_armatures = [o for o in fbx_objects if o.type == 'ARMATURE']

        if not fbx_objects:
            return dae_objs

        ret_objs = dae_objs[:]

        for dae_obj in dae_objs:
            if dae_obj.type != 'MESH':
                continue
            fbx_obj = bpy.data.objects.get(dae_obj.name.replace("_dae", "_fbx"))
            if not fbx_obj:
                continue
            for dae_mat, fbx_mat in zip(dae_obj.data.materials, fbx_obj.data.materials):
                dae_mat.user_remap(fbx_mat)
                fbx_mat.name = fbx_mat.name.replace("_fbx", "")
            bpy.data.objects.remove(fbx_obj)
            dae_obj.name = dae_obj.name.replace("_dae", "")

        dae_armatures = [ob for ob in dae_objs if ob.type=='ARMATURE']
        if len(fbx_armatures) == len(dae_armatures):
            # Well, it does happen, with dungeon walls, for whatever reason.
            f"The .fbx and the .dae have different number of armatures for {dae_path}. This shouldn't happen."

        for fbx_arm, dae_arm in zip(fbx_armatures, dae_armatures):
            dae_arm.user_remap(fbx_arm)
            ret_objs.remove(dae_arm)
            bpy.data.objects.remove(dae_arm)

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

    def cleanup_mesh(self, obj, asset_name):
        for uv_layer, name in zip(obj.data.uv_layers, ("Albedo", "SPM")):
            # TODO: Might need a check here to see if all coordinates are at (0,0) and remove if so.
            uv_layer.name = name
        for m in obj.data.materials:
            if 'Mt' in m.name:
                orig_mat_name = m.name
                obj['orig_mat_name'] = orig_mat_name
                new_mat_name = asset_name + orig_mat_name.replace("Mt_", "_")
                if new_mat_name in bpy.data.materials:
                    m.user_remap(bpy.data.materials.get(new_mat_name))
                else:
                    m.name = new_mat_name
            setup_material(obj, m)

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
        if context.object:
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

def load_png_images_from_directory(directory):
    """
    Loads all PNG images from the directory containing the given file path.
    
    :param file_path: The full path to a file in the target directory.
    """

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for file in os.listdir(directory):
        if file.lower().endswith(".png") and file not in bpy.data.images:
            image_path = os.path.join(directory, file)
            img = bpy.data.images.load(image_path, check_existing=True)
            print("Loaded image: ", img.filepath)

def setup_material(obj, material):
    albedo = None
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Try to find an albedo texture. This usually imports with the fbx material.
    for node in nodes:
        if node.type == 'TEX_IMAGE':
            img_name = os.path.basename(node.image.filepath)
            existing_img = bpy.data.images.get(img_name)
            if existing_img:
                node.image.user_remap(existing_img)
            if "_alb" in node.image.name.lower():
                albedo = node.image

    # Find all other textures with the same base name.
    texture_set = []
    if albedo:
        textureset_name = albedo.name.split("_Alb")[0]
        for img in bpy.data.images:
            if img.name.startswith(textureset_name):
                texture_set.append(img)

    # Nuke the nodes as imported by .fbx, it's easier to built from scratch.
    nodes.clear()

    # Order the textures nicely
    order = ["Alb", "AO", "Spm", "Nrm", "Emm", "Fx"]
    texture_set.sort(key=lambda img: next((i for i, word in enumerate(order) if word in img.name), -1))

    # Create image nodes, guess UV layer by name, set image color spaces
    # (not sure why but I can't set image color space when loading images)
    UVs = obj.data.uv_layers
    for i, img in enumerate(texture_set):
        img_node = nodes.new(type="ShaderNodeTexImage")
        img_node.image = img
        img_node.width = 400
        img_node.location = (-300, i*-300)
        if "alb" not in img.name.lower():
            img.colorspace_settings.name = 'Non-Color'
        elif "damage" not in img.name.lower() and "red_alb" not in img.name.lower():
            nodes.active = img_node
        if len(UVs) > 1:
            uv_node = nodes.new(type="ShaderNodeUVMap")
            links.new(uv_node.outputs[0], img_node.inputs[0])
            uv_index = 1
            if "alb" in img.name.lower() and "damage" not in img.name.lower():
                uv_index = 0
            uv_node.uv_map = UVs[uv_index].name
            uv_node.location = img_node.location
            uv_node.location.x -= 200

    # Load and position all detected relevant textures based on any existing texture nodes, while setting all non-Albedos to Non-Color colorspace.
    # Ensure the appropriate shader nodetree from resource.blend is present, and instance it. To determine what shader to use, we can only guess by names.

    # HAYYAAAA. A single .dae/.fbx file can contain multiple meshes. It still holds true that one mesh is for one material. But get this; The fbx has more material information than the .dae. It has some texture nodes, which have file paths that at least end in a valid filename, while the .dae sometimes has this, but often not.
    # But remember, the .dae file has the UV maps.
    # So we need to decide if we want to transfer the materials from the fbx to the dae, or transfer the UVs from the dae to the fbx.
    # By the way, neither contains as much data as Switch Tools is able to access, so that's sad.
    pass

def enable_print(bool):
    """For suppressing prints from fbx importer and remove_doubles()."""
    if not bool:
        sys.stdout = open(os.devnull, 'w')
    else:
        sys.stdout = sys.__stdout__


# Register the operator
def menu_func_import(self, context):
    self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text=OUTLINER_OT_import_botw_dae_and_fbx.bl_label)

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()