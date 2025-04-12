import bpy, os
from bpy.props import StringProperty, EnumProperty, BoolProperty
from mathutils import Matrix, Euler
from math import radians
from collections import defaultdict

from .build_asset_library import ALL_MAP_SECTIONS, BLEND_DIR, load_instance_database
from ..operators.botw_asset_import.prepare_scene import ensure_botw_scene_settings
from ..utils.customprop import copy_property
from ..utils.collections import ensure_collection
from ..utils.resources import ensure_lib_datablock

class OBJECT_OT_botw_import_map_section(bpy.types.Operator):
    """Import one chunk of the overworld"""
    bl_idname = "object.botw_import_map_section"
    bl_label = "BotW: Import Map Section"
    bl_options = {'REGISTER', 'UNDO'}

    blend_dir: StringProperty(
        name="Asset Folder", 
        subtype='DIR_PATH', 
        description="Folder where the .blend files containing the map's assets can be found. Missing assets will be printed to the system console.", 
        default=BLEND_DIR, 
    )
    map_section: EnumProperty(
        name="Map Section", 
        description="Section of the map to import",
        items=[(s, s, "Map Section "+s) for s in ALL_MAP_SECTIONS],
        default="B-7",
    )
    ignore_duplicates: BoolProperty(
        name="Ignore Duplicates",
        description="Sometimes the same object is placed in the same location multiple times. This option fixes that.",
        default=True
    )

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split=True
        layout.use_property_decorate=False
        layout.prop(self, 'blend_dir')
        layout.prop(self, 'map_section')

    def execute(self, context):
        map_data = load_instance_database()[self.map_section+"_instance_cache.json"]

        ensure_botw_scene_settings(context)
        dynamic_assets = map_data[self.map_section+"_Dynamic"]["models"]
        static_assets = map_data[self.map_section+"_Static"]["models"]

        coll_root = ensure_collection(context, self.map_section, context.scene.collection)
        coll_root_temp = ensure_collection(context, self.map_section+"_temp", context.scene.collection)
        object_matrices = defaultdict(list)
        for is_dynamic, assets in zip((True, False), (dynamic_assets, static_assets)):
            for asset_name, data in assets.items():
                asset_blend = os.path.join(self.blend_dir, asset_name+".blend")
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

        # Sort the asset collections alphabetically.
        for coll in sorted(coll_root_temp.children, key=lambda c: c.name):
            coll_root.children.link(coll)
            coll_root_temp.children.unlink(coll)
        bpy.data.collections.remove(coll_root_temp)

        return {'FINISHED'}


registry = [
    OBJECT_OT_botw_import_map_section,
]