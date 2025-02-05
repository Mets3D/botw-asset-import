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

        file_count = 0
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(".dae"):
                    file_count += 1

        imported_files = 1
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(".dae"):
                    without_ext = file.replace(".dae", "")
                    asset_name = asset_names.get(without_ext, without_ext)
                    dae_path = os.path.join(root, file)
                    print(f"Importing {imported_files}/{file_count}: {file} ({asset_name})")

                    fbx_path = dae_path.replace(".dae", ".fbx")
                    fbx_armatures = self.import_fbx(context, fbx_path, discard_types=('MESH', 'EMPTY'))

                    dae_objs = self.import_dae(context, dae_path, discard_types=('EMPTY'))

                    # Replace the armature with the one from the .fbx, if it existed.
                    if fbx_armatures:
                        dae_armatures = [ob for ob in dae_objs if ob.type=='ARMATURE']
                        assert len(fbx_armatures) == len(dae_armatures), f"The .fbx and the .dae have different number of armatures for {file}. This shouldn't happen."
                        for fbx_arm, dae_arm in zip(fbx_armatures, dae_armatures):
                            dae_arm.user_remap(fbx_arm)
                            dae_objs.remove(dae_arm)
                            bpy.data.objects.remove(dae_arm)
                        dae_objs += fbx_armatures

                    for obj in dae_objs:
                        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                        collection = ensure_collection(context, asset_name)
                        collection.objects.link(obj)
                        context.scene.collection.objects.unlink(obj)
                        if obj.type == 'ARMATURE':
                            obj.name = "Armature_"+asset_name
                            if obj.animation_data and obj.animation_data.action:
                                obj.animation_data.action = None
                            for pb in obj.pose.bones:
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
                        if obj.type == 'MESH':
                            obj['import_name'] = obj.name
                            split = obj.name.split("Mt_")
                            obj.name = asset_name + "_" + split[1]
                            for m in obj.data.materials:
                                orig_mat_name = m.name
                                m.name = asset_name + orig_mat_name.replace("Mt_", "_")
                                obj['orig_mat_name'] = orig_mat_name
                            shift_uv_layer(obj)
                        if obj.type == 'EMPTY':
                            bpy.data.objects.remove(obj)
                            continue
                        obj.data.name = obj.name

                    imported_files += 1
                    
        self.report({'INFO'}, f"Imported {imported_files} FBX files")
        return {'FINISHED'}

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


def enable_print(bool):
    """For suppressing prints from fbx importer and remove_doubles()."""
    if not bool:
        sys.stdout = open(os.devnull, 'w')
    else:
        sys.stdout = sys.__stdout__


def shift_uv_layer(obj, shift_y=-1.0):
    """Shifts the active UV layer of the given object down by 1 unit using foreach_get and foreach_set."""
    
    if obj.type != 'MESH':
        print("Selected object is not a mesh.")
        return
    
    mesh = obj.data
    
    # Ensure the mesh has UV layers
    if not mesh.uv_layers.active:
        print("No active UV layer found.")
        return
    
    uv_layer = mesh.uv_layers.active.data

    # Efficiently retrieve all UV coordinates
    uv_count = len(uv_layer)
    uv_data = np.empty(uv_count * 2, dtype=np.float32)
    uv_layer.foreach_get("uv", uv_data)

    # Reshape into Nx2 array (U, V) and shift V (index 1)
    uv_data = uv_data.reshape(-1, 2)
    uv_data[:, 1] += shift_y  # Move all UVs down by 1 unit

    # Set the modified UV data back
    uv_layer.foreach_set("uv", uv_data.ravel())

    # Update the mesh
    mesh.update()
    # print(f"Shifted {uv_count} UV points down by {shift_y} unit.")

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