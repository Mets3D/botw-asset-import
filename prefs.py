import bpy, os
from bpy.types import AddonPreferences
from bpy.props import StringProperty, EnumProperty
from . import __package__ as base_package

class BotWImportPreferences(AddonPreferences):
    bl_idname = __package__

    game_models_folder: StringProperty(
        name="Extracted Models",
        subtype='FILE_PATH',
        description="If the path to Link's head texture on your system is this:\nD:\\BotW Extracted\\Models\\Link\\Link_Head_Alb.png\nThen in this box you should browse this:\nD:\\BotW Extracted\\Models\\"
    )
    game_icons_folder: StringProperty(
        name="Extracted Icons",
        subtype='FILE_PATH',
        description="If the path to the Ancient Arrow's inventory icon is this:\nD:\\BotW Extracted\\Icons\\AncientArrow\\AncientArrow.jpg\nThen in this box you should browse this:\nD:\\BotW Extracted\\Icons\\"
    )
    game_anims_folder: StringProperty(
        name="Extracted Animations",
        subtype='FILE_PATH',
        description="If the path to the Bear's Eat animation is this:\nD:\\BotW Extracted\\Animations\\Animal_Bear_Animation\\Eat.seanim\nThen in this box you should browse this:\nD:\\BotW Extracted\\Animations\\"
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
        description="How to load bone widgets and shader nodegroups.\nNote: World and Lights will always be appended, as linking them would be kinda pointless"
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(self, 'game_models_folder')
        layout.prop(self, 'game_icons_folder')
        layout.prop(self, 'game_anims_folder')

        layout.separator()
        layout.row().prop(self, 'resource_append_mode', expand=True)

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

registry = [BotWImportPreferences]
