import bpy, os
from bpy.props import BoolProperty

from mathutils import Matrix, Vector, Euler
from math import pi

from .widgets import ensure_widget
from .op_thumbnail_from_viewport import crop_asset_preview
from .botw_batch_fbx_import import GARBAGE_MATS

from .utils.collections import find_layer_collection_by_collection
from .utils.action import remove_redundant_keyframes, remove_negative_frames, fix_groups
from .utils.catalogs import asset_catalogs_to_scene_collection

class OBJECT_OT_botw_cleanup(bpy.types.Operator):
    """Some clean-up operations to catch up assets that were imported with WIP versions of the importer."""

    bl_idname = "object.botw_cleanup"
    bl_label = "BotW: Cleanup"
    bl_options = {'REGISTER', 'UNDO'}

    apply_transforms: BoolProperty(name="Apply Transforms")

    ensure_root_bones: BoolProperty(name="Ensure Root Bones")
    reset_bone_transforms: BoolProperty(name="Reset Bone Transforms")
    link_bone_widgets: BoolProperty(name="Link Bone Widgets")
    remove_single_bones: BoolProperty(name="Remove 1-Bone Armatures")

    clean_animations: BoolProperty(name="Clean Animations")
    rename_actions: BoolProperty(name="Rename Actions")

    organize_by_catalogs: BoolProperty(name="Organize Scene By Asset Catalogs")
    crop_asset_previews: BoolProperty(name="Crop Transparent Asset Previews")

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if self.apply_transforms or self.ensure_root_bones:
            reveal_all_collections(context)

        if self.apply_transforms:
            apply_transforms(context)
            context.view_layer.update()
        if self.ensure_root_bones:
            ensure_root_bones(context)
        if self.reset_bone_transforms:
            reset_bone_transforms(context)
        if self.link_bone_widgets:
            link_bone_widgets(context)
        if self.clean_animations:
            for a in bpy.data.actions:
                remove_negative_frames(a)
                remove_redundant_keyframes(a)
                fix_groups(a)
        if self.organize_by_catalogs:
            asset_catalogs_to_scene_collection(context)
        if self.rename_actions:
            rename_actions()
        if self.crop_asset_previews:
            crop_asset_previews()
        

        report_useless_armatures(remove=self.remove_single_bones)
        report_empty_image_nodes()
        report_bad_image_paths()
        report_libraries()
        report_texts()

        for coll in bpy.data.collections:
            if coll.asset_data:
                coll.hide_viewport = coll.hide_render = False
        remove_custom_props()
        hide_garbage_mats()
        ensure_lighting()
        rename_ids()

        self.report({'INFO'}, "Cleanup complete.")
        return {'FINISHED'}

def crop_asset_previews():
    for container in (bpy.data.collections, bpy.data.actions):
        for asset in container:
            if not asset.asset_data:
                continue
            if not asset.library and not asset.override_library and asset.asset_data:
                print("Crop: ", asset.name)
                crop_asset_preview(asset)

def rename_actions():
    REMOVE = ["Default_", "Demo_", "Act_", "Normal_", "Common_", "Gd_General_", "GdQueen_", "Npc_TripMaster_", "Npc_Hylia_Johnny_", "Npc_Escort_", "Npc_King_Vagrant_", "UC_M_", "Npc_Shiekah_Heir_", "Npc_Shiekah_Artist_", "AncientDoctor_Hateno_", "Npc_Rito_Teba_", "Minister_", "UR_M_", "Move_", "Test_"]

    SWAPS = {
        'SitGround' : 'Ground',
        'SitChair' : 'Chair',
        'Negative_' : 'Neg_'
    }

    for a in bpy.data.actions:
        new_name = a.name
        for word in REMOVE:
            if word in new_name:
                new_name = new_name.replace(word, "")
        
        for find, replace in SWAPS.items():
            if find in new_name:
                new_name = new_name.replace(find, replace)

        if a.name != new_name:
            counter = 1
            while new_name in bpy.data.actions:
                new_name = new_name + str(counter)
                counter += 1
            print(a.name, " -> ", new_name)
            a.name = new_name

def report_texts():
    for t in bpy.data.texts:
        print("Text: ", t.name)

def report_libraries():
    for lib in bpy.data.libraries:
        if not lib.filepath.startswith("//") or ".." in lib.filepath:
            print("Suspicious library: ", lib.filepath)

def rename_ids():
    trash = ["_Model"]
    swap = {
        "  " : " ",
        "D L C" : "DLC"
    }
    for container in (bpy.data.objects, bpy.data.collections, bpy.data.materials):
        for id in container:
            if id.library or id.override_library:
                continue
            new_name = id.name
            for word in trash:
                new_name = new_name.replace(word, "")
            for find, replace in swap.items():
                if find in new_name:
                    new_name = new_name.replace(find, replace)
            if "  " in new_name:
                new_name = new_name.replace("  ", " ")
            if id.name != new_name:
                print("Rename ", id.name, " -> ", new_name)
                id.name = new_name
            
    for obj in bpy.data.objects:
        if obj.data:
            obj.data.name = obj.name
        if hasattr(obj.data, 'shape_keys'):
            obj.data.shape_keys.name = obj.name

def ensure_lighting():
    sun = bpy.data.objects['LGT-botw-sun']
    sun.data.energy = 5
    sun.data.angle = pi
    sun.data.color = [0.981166, 1.000000, 0.843266]
    sun.rotation_euler = Euler((0.8955193161964417, 0.44753706455230713, 0.2860877215862274), 'XYZ')
    sun.location = (2, -2, 2)
    sphere = bpy.data.objects['LGT-botw-sphere_light']
    sphere.data.energy = 0
    sphere.data.shadow_soft_size = 1
    sphere.data.color = [1.000000, 0.210270, 0.087245]
    sphere.location = (0, -1, 1)

def hide_garbage_mats():
    for garb in GARBAGE_MATS:
        for obj in bpy.data.objects:
            if garb in obj.name:
                obj.hide_viewport = obj.hide_render = True
                obj.data.materials.clear()

def remove_custom_props():
    bad_props = ['cloudrig', 'cloudrig_prefs', 'cycles', 'cloudrig_component', 'existing_img']
    for obj in bpy.data.objects:
        things = [obj]
        if obj.type == 'ARMATURE':
            things += obj.pose.bones
        for thing in things:
            for bad_prop in bad_props:
                if bad_prop in thing:
                    del thing[bad_prop]

def reveal_all_collections(context):
    for c in bpy.data.collections:
        c.hide_viewport = False
        layer_coll = find_layer_collection_by_collection(context.view_layer.layer_collection, c)
        if layer_coll:
            layer_coll.hide_viewport = False

    bpy.ops.object.hide_view_clear()
    bpy.ops.object.select_all(action='SELECT')

def apply_transforms(context):
    for o in bpy.data.objects:
        if o.type not in ('MESH', 'ARMATURE'):
            o.select_set(False)
            continue
        if o.matrix_world == Matrix.Identity((4)):
            o.select_set(False)
            continue
        o.select_set(True)
    bpy.ops.object.transform_apply()

def ensure_root_bones(context):
    print("Ensure root bones")
    for o in bpy.data.objects:
        if o.type != 'ARMATURE':
            continue
        root = o.data.bones.get("Root")
        if not root or root.tail_local != Vector((0, 1, 0)):
            with context.temp_override(object=o, active_object=o):
                bpy.context.view_layer.objects.active = o
                bpy.ops.object.mode_set(mode='EDIT')

                root = o.data.edit_bones.get("Root")
                if not root:
                    root = o.data.edit_bones.new(name="Root")
                    root.tail.y = 1
                    print("Created root bone for ", o.name)
                if root.tail != Vector((0, 1, 0)):
                    root.head = Vector((0, 0, 0))
                    root.tail = Vector((0, 1, 0))
                    root.roll = 0
                    print("Rotated root bone: ", o.name)

                for eb in o.data.edit_bones:
                    if not eb.parent and eb != root:
                        eb.parent = root

                bpy.ops.object.mode_set(mode='OBJECT')

        root = o.pose.bones['Root']
        root.custom_shape = ensure_widget('Root')
        root.use_custom_shape_bone_size = False
        root.custom_shape_scale_xyz = [max(o.dimensions)/2]*3
        root.custom_shape_rotation_euler = Euler()

def reset_bone_transforms(context):
    for o in bpy.data.objects:
        if o.type != 'ARMATURE':
            continue
        o.show_in_front = False
        if o.animation_data and o.animation_data.action:
            o.animation_data.action = None
            print("Cleared action: ", o.name)
        for pb in o.pose.bones:
            pb.matrix_basis.identity()
            if any([pb.name.endswith(suf) for suf in ("_R", "_FR", "_BR", "_R_1", "_R_2")]):
                pb.custom_shape_rotation_euler.z = 0
            else:
                pb.custom_shape_rotation_euler.z = -pi

def link_bone_widgets(context):
    blend_path = bpy.data.filepath
    res_path = os.path.join(os.path.dirname(blend_path), "resources.blend")
    rel_path = bpy.path.relpath(res_path)
    if not os.path.isfile(res_path):
        return

    with bpy.data.libraries.load(res_path, link=True, relative=True) as (
        data_from,
        data_to,
    ):
        for wgt in [o for o in bpy.data.objects if o.name.startswith("WGT-")]:
            if wgt.library and wgt.library.filepath == rel_path:
                continue
            if wgt.name in data_from.objects:
                data_to.objects.append(wgt.name)

    for wgt in [o for o in bpy.data.objects if o.name.startswith("WGT-")]:
        if wgt.library and wgt.library.filepath == rel_path:
            continue
        linked_wgt = bpy.data.objects.get((wgt.name, rel_path))
        if linked_wgt:
            wgt.user_remap(linked_wgt)

def report_useless_armatures(remove=False):
    for obj in bpy.data.objects[:]:
        if obj.type != 'ARMATURE':
            continue
        if len(obj.pose.bones) == 1 and obj.pose.bones[0].name == "Root":
            if remove:
                print("Remove single bone armature: ", obj.name)
                bpy.data.objects.remove(obj)
            else:
                print("Single bone armature: ", obj.name)

def report_empty_image_nodes():
    for m in bpy.data.materials:
        if m.library:
            continue
        if not m.use_nodes:
            continue
        for n in m.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                n.image=n.image
                if not n.image:
                    print("Empty image node in: ", m.name)

def report_bad_image_paths():
    for i in bpy.data.images:
        if i.library:
            continue
        if i.name in ("Render Result"):
            continue
        if not i.filepath.startswith("//textures"):
            print("Image not in //textures: ", i.name)
        abs_path = bpy.path.abspath(i.filepath)
        if not os.path.isfile(abs_path):
            print("Image missing: ", i.name)

registry = [OBJECT_OT_botw_cleanup]