import bpy, os, hashlib
from bpy.props import BoolProperty

from mathutils import Euler
from math import pi

from .botw_batch_asset_import import get_albedo_img_node
from ..databases.asset_names import asset_names

from ..utils.action import remove_redundant_keyframes, remove_negative_frames, fix_groups
from ..utils.catalogs import asset_catalogs_to_scene_collection
from ..utils.pixel_image import PixelImage

class OBJECT_OT_botw_cleanup(bpy.types.Operator):
    """Some clean-up operations to catch up assets that were imported with WIP versions of the importer. You'll probably never need to use this."""

    bl_idname = "object.botw_cleanup"
    bl_label = "BotW: Cleanup"
    bl_options = {'REGISTER', 'UNDO'}

    link_bone_widgets: BoolProperty(name="Link Bone Widgets")
    remove_single_bones: BoolProperty(name="Remove 1-Bone Armatures")

    clean_animations: BoolProperty(name="Clean Animations")

    organize_by_catalogs: BoolProperty(name="Organize Scene By Asset Catalogs")

    deduplicate_images: BoolProperty(name="Deduplicate Images")

    report_issues: BoolProperty(name="Report Issues", description="Report issues that may need manual checking. This is always safe to enable.", default=True)
    reveal_asset_collections: BoolProperty(name="Ensure Visible Asset Collections", default=True)

    rename_actions: BoolProperty(name="Rename Actions", description="Rename Actions to have better names. Changes will be printed to terminal.")
    rename_materials: BoolProperty(name="Rename Materials", description="Rename materials to the name of their albedo texture if available.")

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        header, panel = layout.panel(idname="Cleanup (Safe)")
        header.label(text="Safe (ish)")
        if panel:
            panel.prop(self, 'report_issues')
            panel.prop(self, 'reveal_asset_collections')
            panel.prop(self, 'link_bone_widgets')
            panel.prop(self, 'organize_by_catalogs')

        header, panel = layout.panel(idname="Cleanup (Destructive")
        header.label(text="Destructive")
        if panel:
            panel.prop(self, 'deduplicate_images')
            panel.prop(self, 'clean_animations')
            panel.prop(self, 'remove_single_bones')

        header, panel = layout.panel(idname="Cleanup (Rename)")
        header.label(text="Rename")
        if panel:
            panel.prop(self, 'rename_actions')
            panel.prop(self, 'rename_materials')

    def execute(self, context):
        if self.link_bone_widgets:
            link_bone_widgets()
        if self.clean_animations:
            for a in bpy.data.actions:
                removed_count = remove_negative_frames(a)
                removed_count += remove_redundant_keyframes(a)
                fixed = fix_groups(a)
                msg = ""
                if removed_count:
                    msg += f"Removed {removed_count} keyframes."
                if fixed:
                    msg += f"fixed {fixed} missing groups."
                if msg:
                    print(f"Cleaned {a.name}: {msg}")
        if self.organize_by_catalogs:
            asset_catalogs_to_scene_collection(context)
        if self.rename_actions:
            rename_actions()
        if self.deduplicate_images:
            print("Deduplicating textures...")
            deduplicate_textures()

        if self.report_issues or self.remove_single_bones:
            report_useless_armatures(remove=self.remove_single_bones)
        if self.report_issues:
            report_empty_image_nodes()
            report_bad_image_paths()
            report_bad_colorspace()
            report_libraries()
            report_texts()
            report_local_nodegroups()

        if self.reveal_asset_collections:
            for coll in bpy.data.collections:
                if coll.asset_data:
                    coll.hide_viewport = coll.hide_render = False

        remove_custom_props()
        ensure_lighting()

        if self.rename_materials:
            rename_materials_to_albedo()

        self.report({'INFO'}, "Cleanup complete.")
        return {'FINISHED'}

def rename_materials_to_albedo():
    for mat in bpy.data.materials:
        if mat.library:
            continue
        albedo_node = get_albedo_img_node(mat)
        if not albedo_node or albedo_node.type != 'TEX_IMAGE' or not albedo_node.image:
            continue
        albedo = albedo_node.image
        org_name = mat.name
        if "_Alb" in albedo.name:
            mat.name = albedo.name.split("_Alb")[0]
        elif "." in albedo.name:
            mat.name = albedo.name.split(".")[0]

        if mat.name in asset_names:
            mat.name = asset_names[mat.name]

        if mat.name != org_name:
            print(f"Renamed material by albedo tex: {org_name} -> {mat.name}")

def report_local_nodegroups():
    for ng in bpy.data.node_groups:
        if not ng.library:
            print("Local nodegroup: ", ng.name)

def rename_actions():
    # TODO: This should move to the batch .seanim import operator.
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

def remove_custom_props():
    # TODO: Move this to the import operator.
    bad_props = ['cloudrig', 'cloudrig_prefs', 'cycles', 'cloudrig_component', 'existing_img']
    for obj in bpy.data.objects:
        things = [obj]
        if obj.type == 'ARMATURE':
            things += obj.pose.bones
        for thing in things:
            for bad_prop in bad_props:
                if bad_prop in thing:
                    del thing[bad_prop]
    for prop in list(bpy.context.scene.keys()):
        del bpy.context.scene[prop]

def link_bone_widgets():
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

def report_bad_colorspace():
    alb_exceptions = ["Horse_Link_Body", "Armor_048_Skin_Paint"]
    for img in bpy.data.images:
        if img.name == "Render Result":
            continue
        if "_Alb" in img.name or "MaterialAlb" in img.name and not any([exc in img.name for exc in alb_exceptions]):
            if img.colorspace_settings.name != 'sRGB':
                print("Should be sRGB?", img.name, img.colorspace_settings.name)
                # img.colorspace_settings.name = 'sRGB'
        elif "_Emm" in img.name or "_AO" in img.name:
            # In a lot of cases, these were manually switched to sRGB. 
            # For _Emm, we could check pixel data to see if all_channels_match, but meh.
            pass
        else:
            if img.colorspace_settings.name != 'Non-Color':
                print("Should be non-color?", img.name, img.colorspace_settings.name)

def hash_image_pixels(image) -> str:
    pixel_image = PixelImage.from_blender_image(image)
    img_hash = hashlib.md5(str(pixel_image.pixels_rgba).encode("utf-8")).hexdigest()
    # Dump the pixel cache in this case, otherwise it's easy to run out of memory when deduplicating textures.
    pixel_image.pixels_rgba = []
    return img_hash

def deduplicate_textures():
    img_hashes = {}
    copy_counter = {}
    for img in bpy.data.images:
        if img.library:
            continue
        if 'hash' not in img:
            img['hash'] = hash_image_pixels(img)
        img_hash = img['hash']
        if img_hash in img_hashes:
            print(f"Duplicate Image: '{img.name}' -> {img_hashes[img_hash].name}")
            img.user_remap(img_hashes[img_hash])
            if img_hash not in copy_counter:
                copy_counter[img_hash] = 0
            copy_counter[img_hash] += 1
        else:
            img_hashes[img_hash] = img

    for img_hash, count in copy_counter.items():
        print(f"Image {img_hashes[img_hash].name} had {count} duplicates.")

registry = [OBJECT_OT_botw_cleanup]