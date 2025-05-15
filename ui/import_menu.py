import bpy

class BOTW_MT_import(bpy.types.Menu):
    bl_idname = 'BOTW_MT_import'
    bl_label = "BotW Import"

    def draw(self, context):
        self.layout.operator("import_scene.botw_dae_fbx", text="Import Asset (.dae & .fbx)")
        self.layout.separator()
        self.layout.operator("object.botw_build_assetlib_for_map", text="Build Asset Library")
        self.layout.operator("object.botw_import_map_section", text="Import Map Section")
        self.layout.separator()
        self.layout.operator("file.unpack_botw_terrain", text="Unpack Terrain (.sstera)")
        self.layout.operator("scene.botw_import_terrain", text="Import Terrain Section")

def menu_func_import(self, context):
    self.layout.menu(BOTW_MT_import.bl_idname)

def register():
    bpy.utils.register_class(BOTW_MT_import)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(BOTW_MT_import)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
