import bpy
from ..operators.botw_asset_import import OUTLINER_OT_import_botw_dae_and_fbx
from ..map_data_import.build_asset_library import OBJECT_OT_botw_build_assetlib_for_map
from ..map_data_import.load_map_section import OBJECT_OT_botw_import_map_section

class MENU_botw_import(bpy.types.Menu):
    bl_idname = 'MENU_botw_import'
    bl_label = "BotW Import"

    def draw(self, context):
        self.layout.operator(OUTLINER_OT_import_botw_dae_and_fbx.bl_idname, text="Import Asset (.dae & .fbx)")
        self.layout.operator(OBJECT_OT_botw_build_assetlib_for_map.bl_idname, text="Build Asset Library")
        self.layout.operator(OBJECT_OT_botw_import_map_section.bl_idname, text="Import Map Section")


def menu_func_import(self, context):
    self.layout.menu(MENU_botw_import.bl_idname)

def register():
    bpy.utils.register_class(MENU_botw_import)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(MENU_botw_import)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
