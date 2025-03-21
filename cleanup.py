import bpy, os
from bpy.props import BoolProperty

from mathutils import Matrix, Vector, Euler
from math import pi

from .widgets import ensure_widget
from .utils.collections import find_layer_collection_by_collection
from .io_anim_seanim.import_seanim import remove_redundant_keyframes
from .utils.catalogs import asset_catalogs_to_scene_collection
from .op_thumbnail_from_viewport import crop_asset_preview

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
    organize_by_catalogs: BoolProperty(name="Organize Scene By Asset Catalogs")
    crop_asset_previews: BoolProperty(name="Crop Transparent Asset Previews")

    remove_redundant_keyframes: BoolProperty(name="Clean Redundant Keyframes")

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
        if self.remove_redundant_keyframes:
            for a in bpy.data.actions:
                remove_redundant_keyframes(a)
        if self.organize_by_catalogs:
            asset_catalogs_to_scene_collection(context)
        if self.crop_asset_previews:
            for coll in bpy.data.collections:
                if not coll.library and not coll.override_library and coll.asset_data:
                    crop_asset_preview(coll)
            for action in bpy.data.actions:
                if not action.library and not action.override_library and action.asset_data:
                    crop_asset_preview(action)

        report_useless_armatures(remove=self.remove_single_bones)
        report_empty_image_nodes()
        report_bad_image_paths()

        self.report({'INFO'}, "Cleanup complete.")
        return {'FINISHED'}

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
        if not m.use_nodes:
            continue
        for n in m.node_tree.nodes:
            if n.type == 'TEX_IMAGE':
                n.image=n.image
                if not n.image:
                    print("Empty image node in: ", m.name)

def report_bad_image_paths():
    for i in bpy.data.images:
        if i.name in ("Render Result"):
            continue
        if not i.filepath.startswith("//textures"):
            print("Image not in //textures: ", i.name)
        abs_path = bpy.path.abspath(i.filepath)
        if not os.path.isfile(abs_path):
            print("Image missing: ", i.name)

registry = [OBJECT_OT_botw_cleanup]