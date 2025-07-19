import bpy, os, glob
from bpy.props import BoolProperty, StringProperty
from math import pi
from pathlib import Path

from mathutils import Vector, Euler
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from ...databases.asset_names import asset_names
from ...utils.collections import ensure_collection, set_active_collection
from ...utils.resources import ensure_widget
from ...prefs import get_addon_prefs
from ...utils.material import deduplicate_materials, refresh_images
from ...utils.timer import Timer
from ...utils.pixel_image import PixelImage
from ...utils.dae_fixer import fix_dae_uvmaps_in_place

# This is just here to make Reload Scripts work... at least when I run it twice...?
from . import constants, process_material, process_object, prepare_scene, names
modules = [constants, process_material, process_object, prepare_scene, names]

from .prepare_scene import ensure_botw_scene_settings
from .names import derive_asset_name
from .process_object import process_obj
from .constants import ICON_EXTENSION, ensure_caches

class OUTLINER_OT_import_botw_dae_and_fbx(Operator, ImportHelper):
    """Import all .dae & .fbx files from a selected folder recursively"""
    bl_idname = "import_scene.botw_dae_fbx"
    bl_label = "Import BotW .dae + .fbx"
    bl_options = {'REGISTER', 'UNDO'}

    directory: StringProperty(subtype='DIR_PATH', options={'SKIP_SAVE', 'HIDDEN'})

    rename_collections: BoolProperty(name="Rename Collections", description="Rename collections to their asset name.", default=True)
    rename_ob_mat: BoolProperty(name="Rename Objects & Materials", description="Prepend asset name to object and material names, and remove garbage strings. Useful when importing many assets into a single file to keep names unique, but can also result in exceeding the 63-character limit (those cases will not be renamed.).", default=True)

    apply_transforms: BoolProperty(name="Apply Transforms", description="Necessary for wind shader effects to work, and in some cases also necessary for correct armature replacement from .fbx files if you have them.", default=True)
    remove_redundant_armatures: BoolProperty(name="Remove Redundant Armatures", description="If an armature has only 1 bone and it's at the world origin, or if it doesn't deform any objects with any of its bones, remove it", default=True)
    remove_redundant_UVs: BoolProperty(name="Remove Redundant UVs", description="If a UVMap is the same as a previous one, or if it's empty, remove it", default=True)

    create_parent_collections: BoolProperty(name="Create Parent Collections", description="When a directory has more than 1 file, create a parent collection that represents that directory", default=True)

    deduplicate_materials: BoolProperty(name="Deduplicate Materials", description="If two materials end up with identical nodetrees, merge them into one. It's difficult to verify that this doesn't break anything, so be careful. It's not a big deal if some materials are duplicates anyways", default=False)

    force_update_caches: BoolProperty(default=False)

    def invoke(self, context, _event):
        model_dir = get_addon_prefs(context).game_models_folder
        if os.path.exists(model_dir):
            self.directory = model_dir
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

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
        if not self.directory:
            self.report({'WARNING'}, "No folder selected")
            return {'CANCELLED'}

        prefs = get_addon_prefs(context)
        direct_dae_files = dae_files = glob.glob(f"{self.directory}/*.dae", recursive=False)
        models_dir = prefs.game_models_folder
        if direct_dae_files:
            models_dir = Path(self.directory).parent.as_posix()
            if not os.path.exists(prefs.game_models_folder):
                # User didn't select the folder in user prefs, but let's assume they are at least selecting an asset dir right now.
                prefs.game_models_folder = models_dir

        any_dae_files = dae_files = glob.glob(f"{self.directory}/**/*.dae", recursive=True)
        if not any_dae_files:
            self.report({'WARNING'}, "No .dae files were found anywhere in this folder or its sub-folders.")
            return {'CANCELLED'}

        if any_dae_files:
            models_dir = Path(self.directory).as_posix()
            if not os.path.exists(prefs.game_models_folder):
                # User didn't select the folder in user prefs, but apparently ther are in the Models dir right now.
                prefs.game_models_folder = models_dir

        if models_dir and models_dir != prefs.current_import_folder:
            self.force_update_caches = True

        prefs.current_import_folder = models_dir

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
                    if not imported_coll:
                        continue
                    imported_objects += imported_coll.all_objects
                    if self.rename_collections:
                        imported_coll.name = imported_coll['asset_name']
            counter += 1

        if self.deduplicate_materials:
            deduplicate_materials(imported_objects)
        bpy.ops.outliner.orphans_purge()
        refresh_images()

        # Dump cache, in case the garbage collector doesn't. (it should, but this makes extra sure.)
        PixelImage.cache = {}
        Timer.summarize()

        prefs.current_import_folder = ""
        return {'FINISHED'}

def import_and_process_dae(
        context, 
        full_path: str, 
        parent_coll=None, 
        rename_objects=False, 
        apply_transforms=True,
        remove_redundant_armatures=True,
        remove_redundant_UVs=True,
    ) -> bpy.types.Collection or None:
    dae_filename = os.path.basename(full_path)
    dirpath = os.path.dirname(full_path)
    dirname = os.path.basename(dirpath)

    asset_name = dae_filename.replace(".dae", "")
    asset_name = derive_asset_name(dae_filename, dirname)

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
        try:
            objs = import_dae(context, full_path, discard_types=('EMPTY'), apply_transforms=apply_transforms)
        except RuntimeError:
            # No idea why but on at least 1 asset, the .dae importer claims "parsing errors".
            # We can fall back on the .fbx file. The only downside of this is that if the .dae 
            # would've had a 2nd UVMap, the .fbx will not have that.
            objs = import_fbx(context, full_path.replace(".dae", ".fbx"), discard_types=('EMPTY'), apply_transforms=apply_transforms)
        rig_name = "RIG-"+asset_name if rename_objects else ""
        objs = import_and_merge_fbx_armature(
            context,
            dae_objs=objs,
            dae_path=full_path,
            rig_name=rig_name,
            apply_transforms=apply_transforms
        )
    if not objs:
        return

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
        obj = process_obj(
            collection, 
            obj, 
            rename_ob_mat=rename_objects, 
            remove_redundant_armatures=remove_redundant_armatures,
            remove_redundant_UVs=remove_redundant_UVs,
            do_leaf_z_hack=apply_transforms,
        )

    return collection

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
    if bpy.app.version <= (4, 4, 0):
        return import_whatever(
            context, 
            import_func=bpy.ops.import_scene.fbx,
            filepath=filepath, 
            discard_types=discard_types, 
            apply_transforms=apply_transforms
        )
    else:
        return import_whatever(
            context, 
            import_func=bpy.ops.wm.fbx_import,
            filepath=filepath, 
            discard_types=discard_types, 
            apply_transforms=apply_transforms,
        )

def import_dae(context, filepath, discard_types=('EMPTY'), apply_transforms=True):
    fix_dae_uvmaps_in_place(filepath)
    return import_whatever(
        context, 
        import_func=bpy.ops.wm.collada_import,
        filepath=filepath, 
        discard_types=discard_types, 
        apply_transforms=apply_transforms
    )

def import_whatever(context, *, import_func, filepath: str, discard_types=('EMPTY'), apply_transforms=True, **kwargs):
    """import_func can be any function that takes a "filepath" property.
    (Okay, it should also load the contents to the active collection and select all objects.)
    Basically any Blender import function. But this function is here just to share code between .dae/.fbx import.
    """

    if not os.path.exists(filepath):
        return False
    if context.active_object:
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    # I've tried a million ways to suppress the .dae importer prints but it can't be done without a PR to Blender.
    # (Or by Popen()ing another blender instance to import and then appending from that, which would be too silly.)
    import_func(filepath=filepath, **kwargs)

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
                    mat['import_name'] = mat.name[:-4] if len(mat.name)>3 and mat.name[-4]=="." and mat.name[-3:].isdigit() else mat.name
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

### Registry

def register():
    bpy.utils.register_class(OUTLINER_OT_import_botw_dae_and_fbx)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_import_botw_dae_and_fbx)
