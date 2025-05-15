import bpy
from ..operators.botw_asset_import import OUTLINER_OT_import_botw_dae_and_fbx
from ..map_data_import.build_asset_library import OBJECT_OT_botw_build_assetlib_for_map
from ..map_data_import.load_map_section import OBJECT_OT_botw_import_map_section
from ..map_data_import.unpack_map_sstera import FILE_OT_unpack_terrain

class BOTW_MT_import(bpy.types.Menu):
    bl_idname = 'BOTW_MT_import'
    bl_label = "BotW Import"

    def draw(self, context):
        self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="Import Asset (.dae & .fbx)")
        self.layout.separator()
        self.layout.operator(FILE_OT_unpack_terrain.bl_idname, text="Unpack Terrain .sstera")
        self.layout.operator(OBJECT_OT_botw_build_assetlib_for_map.bl_idname, text="Build Asset Library")
        self.layout.operator(OBJECT_OT_botw_import_map_section.bl_idname, text="Import Map Section")


def menu_func_import(self, context):
    self.layout.menu(BOTW_MT_import.bl_idname)

def register():
    bpy.utils.register_class(BOTW_MT_import)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(BOTW_MT_import)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
