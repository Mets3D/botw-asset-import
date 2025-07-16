import bpy, os
from bpy.props import EnumProperty, BoolProperty
from mathutils import Matrix, Euler
from math import radians
from collections import defaultdict
from tqdm import tqdm

from .build_asset_library import map_section_enum_items, load_instance_database
from ..operators.botw_asset_import.prepare_scene import ensure_botw_scene_settings
from ..utils.customprop import copy_property
from ..utils.collections import ensure_collection
from ..utils.resources import ensure_lib_datablock
from ..prefs import get_addon_prefs, draw_folder_select

class OBJECT_OT_botw_import_map_section(bpy.types.Operator):
    """Import one chunk of the overworld"""
    bl_idname = "object.botw_import_map_section"
    bl_label = "BotW: Import Map Section"
    bl_options = {'REGISTER', 'UNDO'}

    map_section: EnumProperty(
        name="Map Section", 
        description="Section of the map to import",
        items=map_section_enum_items(),
        default="B-7",
    )
    ignore_duplicates: BoolProperty(
        name="Ignore Duplicates",
        description="Sometimes the same object is placed in the same location multiple times. This option fixes that.",
        default=True
    )

    def invoke(self, context, _event):
        self.org_pref = context.preferences.view.filebrowser_display_type
        context.preferences.view.filebrowser_display_type = 'WINDOW'
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split=True
        layout.use_property_decorate=False
        draw_folder_select(layout, get_addon_prefs(context), 'assets_output_folder', empty_ok=False)
        layout.prop(self, 'map_section')

    def execute(self, context):
        prefs = get_addon_prefs(context)
        if not os.path.isdir(prefs.assets_output_folder):
            self.report({'ERROR'}, f"Asset output folder does not exist: {prefs.asset_output_folder}")
            return {'CANCELLED'}
        map_data = load_instance_database()[self.map_section+"_instance_cache.json"]

        ensure_botw_scene_settings(context)
        dynamic_assets = map_data[self.map_section+"_Dynamic"]["models"]
        static_assets = map_data[self.map_section+"_Static"]["models"]

        coll_root = ensure_collection(context, self.map_section, context.scene.collection)
        coll_root_temp = ensure_collection(context, self.map_section+"_temp", context.scene.collection)
        object_matrices = defaultdict(list)

        total = len(dynamic_assets) + len(static_assets)
        bar_format = "{n_fmt}/{total_fmt} {bar}"


        with tqdm(total=total, bar_format=bar_format) as pbar:
            for is_dynamic, assets in zip((True, False), (dynamic_assets, static_assets)):
                for asset_name, data in assets.items():
                    asset_blend = os.path.join(prefs.assets_output_folder, asset_name+".blend")
                    coll_linked_asset = None
                    if os.path.isfile(asset_blend):
                        coll_linked_asset = ensure_lib_datablock('collections', asset_name, blend_path=asset_blend, link=True)
                    if not coll_linked_asset:
                        coll_missing = ensure_collection(context, self.map_section + " Missing Assets", coll_root)
                        coll_asset = ensure_collection(context, asset_name, coll_missing)
                    else:
                        coll_asset = ensure_collection(context, asset_name, coll_root_temp)
                    for transforms in data['positions']:
                        loc = transforms['location']
                        rot = transforms['rotate']
                        scale = transforms['scale']
                        # this is a bit complicated, but it works
                        # useful link for explaining order of matrix operations
                        # https://blender.stackexchange.com/questions/44760/rotate-objects-around-their-origin-along-a-global-axis-scripted-without-bpy-op
                        r_m0 = Matrix.Rotation(radians(-90), 4, 'X')
                        t_m = Matrix.Translation(loc)
                        r_m1 = Matrix.Rotation(radians(90), 4, 'X')
                        r_m2 = Euler(rot).to_matrix().to_4x4()
                        matrix = r_m1 @ t_m @ r_m2 @ r_m0
                        existing_copies = object_matrices[asset_name]
                        if self.ignore_duplicates and matrix in existing_copies:
                            continue
                        existing_copies.append(matrix)
                        empty = bpy.data.objects.new(name=asset_name, object_data=None)
                        empty.matrix_world = matrix
                        empty.scale = scale
                        empty['is_dynamic'] = is_dynamic
                        empty.empty_display_size = 0.01
                        empty.instance_type = 'COLLECTION'
                        empty.instance_collection = coll_linked_asset
                        if empty.instance_collection:
                            # We can copy the material control properties to the instancer and it will still work. Neat!
                            # (In the material, the Attribute nodes have to be set to "Instancer" for this.)
                            for obj in empty.instance_collection.all_objects:
                                for prop_name in ('flow_speed', 'flow_axis'):
                                    if prop_name in obj:
                                        copy_property(obj, empty, prop_name)
                        coll_asset.objects.link(empty)
                    pbar.update(1)

        # Sort the asset collections alphabetically and organize by type.
        for coll in sorted(coll_root_temp.children, key=lambda c: c.name):
            parent = coll_root
            asset_type = get_asset_type(coll)
            if asset_type in ("Npc", "Animal", "Enemy"):
                parent = ensure_collection(context, self.map_section + " NPCs", coll_root)
            elif asset_type == "Far":
                parent = ensure_collection(context, self.map_section + " Far", coll_root)
            else:
                parent = ensure_collection(context, self.map_section + " Assets", coll_root)
            parent.children.link(coll)
            coll_root_temp.children.unlink(coll)
        bpy.data.collections.remove(coll_root_temp)

        context.preferences.view.filebrowser_display_type = self.org_pref

        return {'FINISHED'}


def get_asset_type(coll):
    first_obj = coll.objects[0]
    linked_coll = first_obj.instance_collection
    if not linked_coll:
        return "Missing"
    dirname = linked_coll['dirname']
    if "Far" in dirname:
        return "Far"
    elif "Npc" in dirname:
        return 'Npc'
    elif "Animal_" in dirname:
        return 'Animal'
    elif "Enemy_" in dirname:
        return 'Enemy'
    elif dirname in ("Link", "WLlink"):
        return 'Link'
    elif "Armor_" in dirname:
        return 'Armor'
    
    return 'Env'

registry = [
    OBJECT_OT_botw_import_map_section,
]