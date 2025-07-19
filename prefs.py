import bpy, os
from bpy.types import AddonPreferences
from bpy.props import StringProperty, EnumProperty
from . import __package__ as base_package

class BotWImportPreferences(AddonPreferences):
    bl_idname = __package__

    game_models_folder: StringProperty(
        name="Extracted Models",
        subtype='FILE_PATH',
        description="Path to extracted model files of the main game, containing folders of .dae/.fbx/.png. If you are importing mod files, you don't need to merge your folders, nor change this. If the extracted mod files don't contain a texture, a texture from this folder will be used.",
        default="D:\\BotW Extract\\Models\\"
    )
    current_import_folder: StringProperty(
        name="Current Import's Models",
        subtype='FILE_PATH',
        description="Used internally, not exposed to the UI. May differ from game_models_folder when importing mod assets. This will be the primary path to search for materials and images, but we fall back to game_models_folder if a file is not found.",
        default="D:\\BotW Extract\\Models\\"
    )
    game_icons_folder: StringProperty(
        name="Extracted Icons",
        subtype='FILE_PATH',
        description="Path to icons (optional). Should be folders with .jpg files inside, eg. AncientArrow\\AncientArrow.jpg",
        default="D:\\BotW Extract\\Icons\\"
    )
    game_anims_folder: StringProperty(
        name="Extracted Animations",
        subtype='FILE_PATH',
        description="Path to animations (optional). Should be folders with .seanim files, eg. Animal_Bear_Animation\\Eat.seanim",
        default="D:\\BotW Extract\\Animations"
    )
    assets_output_folder: StringProperty(
        name="Assets Folder",
        subtype='FILE_PATH',
        description="Folder to place .blend files of individual imported assets."
    )
    terrain_folder: StringProperty(
        name="Terrain Folder",
        subtype='FILE_PATH',
        description="Folder where the terrain was unpacked using Unpack Terrain operator."
    )

    resource_append_mode: EnumProperty(
        name="Resource Load Mode",
        items=[
            ('APPEND', "Append", "Make a local copy"),
            ('LINK', "Link", "Link from the add-on's resources.blend file"),
        ],
        description="How to load bone widgets and shader nodegroups.\nNote: World and Lights will always be appended"
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        draw_folder_select(layout, self, 'game_models_folder', empty_ok=False)
        draw_folder_select(layout, self, 'game_icons_folder')
        draw_folder_select(layout, self, 'game_anims_folder')

        layout.separator()
        layout.row().prop(self, 'resource_append_mode', expand=True)

def draw_folder_select(layout, owner, prop_name, empty_ok=True):
    row = layout.row()
    path = getattr(owner, prop_name)
    if path or not empty_ok:
        if not os.path.isdir(path):
            row.alert = True
    row.prop(owner, prop_name)

def get_addon_prefs(context=None):
    if not context:
        context = bpy.context
    if base_package.startswith('bl_ext'):
        # 4.2
        return context.preferences.addons[base_package].preferences
    else:
        return context.preferences.addons[base_package.split(".")[0]].preferences

def get_models_folder(context=None):
    prefs = get_addon_prefs(context)
    models_dir = prefs.game_models_folder
    if not os.path.exists(models_dir):
        raise FileNotFoundError("Models Folder must be specified in the add-on's preferences. Read the tooltip!")
    return models_dir

def get_current_folder(context=None):
    prefs = get_addon_prefs(context)
    return prefs.current_import_folder

registry = [BotWImportPreferences]
