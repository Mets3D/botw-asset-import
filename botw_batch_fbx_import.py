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

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all FBX files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW assets from folders of .dae and optionally .fbx files (the armature will be taken from the latter if present)"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(name="Folder Path", subtype='DIR_PATH')

    def execute(self, context):
        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

        self.ensure_scene_settings(context)

        num_files = self.count_files_in_subdirs('.dae')

        imported_files = 0
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(".dae"):
                    without_ext = file.replace(".dae", "")
                    asset_name = asset_names.get(without_ext, without_ext)
                    filepath = os.path.join(root, file)
                    print(f"Importing {imported_files}/{num_files}: {file} ({asset_name})")
                    self.import_and_setup_single_dae(context, filepath, file, asset_name)
                    imported_files += 1

        self.report({'INFO'}, f"Imported {imported_files} FBX files")
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
                area.spaces.active.shading.light = 'MATCAP'
                area.spaces.active.shading.studio_light = 'botw.exr'
                area.spaces.active.shading.color_type = 'TEXTURE'

    def import_and_setup_single_dae(self, context,  filepath, filename, asset_name):
        objs = self.import_dae(context, filepath, discard_types=('EMPTY'))
        objs = self.replace_dae_with_fbx_armature(context, dae_objs=objs, dae_path=filepath, asset_name=asset_name)

        collection = ensure_collection(context, asset_name)

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
                self.cleanup_mesh(obj, asset_name)

            obj.data.name = obj.name

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    def replace_dae_with_fbx_armature(self, context, *, dae_objs, dae_path, asset_name):
        """Replace the armature from the dae_objs list with one from an .fbx, if we can find one with the same name next to it."""
        fbx_path = dae_path.replace(".dae", ".fbx")
        fbx_armatures = self.import_fbx(context, fbx_path, discard_types=('MESH', 'EMPTY'))

        if not fbx_armatures:
            return dae_objs

        ret_objs = dae_objs[:]

        dae_armatures = [ob for ob in dae_objs if ob.type=='ARMATURE']
        assert len(fbx_armatures) == len(dae_armatures), f"The .fbx and the .dae have different number of armatures for {dae_path}. This shouldn't happen."
        for fbx_arm, dae_arm in zip(fbx_armatures, dae_armatures):
            dae_arm.user_remap(fbx_arm)
            ret_objs.remove(dae_arm)
            bpy.data.objects.remove(dae_arm)

            fbx_arm.name = "Armature_"+asset_name
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
            uv_layer.name = name
        assert len(obj.data.uv_layers) < 3, f"Found an object with >2 UV layers: {obj.name}"
        obj['import_name'] = obj.name
        split = obj.name.split("Mt_")
        obj.name = asset_name + "_" + split[1]
        for m in obj.data.materials:
            orig_mat_name = m.name
            new_mat_name = asset_name + orig_mat_name.replace("Mt_", "_")
            if new_mat_name in bpy.data.materials:
                m.user_remap(bpy.data.materials.get(new_mat_name))
            else:
                m.name = new_mat_name
                setup_material(m)
            obj['orig_mat_name'] = orig_mat_name

    def import_fbx(self, context, filepath, discard_types=('MESH', 'EMPTY')):
        if not os.path.exists(filepath):
            return False
        if context.object:
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        enable_print(False)
        bpy.ops.import_scene.fbx(filepath=filepath)
        for ob in context.selected_objects[:]:
            if ob.type in discard_types:
                bpy.data.objects.remove(ob)
        bpy.ops.outliner.orphans_purge()
        enable_print(True)
        return context.selected_objects[:]

    def import_dae(self, context, filepath, discard_types=('EMPTY')):
        if not os.path.exists(filepath):
            return False
        if context.object:
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        enable_print(False)
        # Can't seem to suppress these prints, wow.
        bpy.ops.wm.collada_import(filepath=filepath)
        for ob in context.selected_objects[:]:
            if ob.type in discard_types:
                bpy.data.objects.remove(ob)
        enable_print(True)
        return context.selected_objects[:]


def setup_material(material):
    # Load and position all detected relevant textures based on any existing texture nodes, while setting all non-Albedos to Non-Color colorspace.
    # Ensure the appropriate shader nodetree from resource.blend is present, and instance it. To determine what shader to use, we can only guess by names.
    # Connect noodles.
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