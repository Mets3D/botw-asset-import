from bpy.types import AddonPreferences
from bpy.props import StringProperty

class BotWImportPreferences(AddonPreferences):
    bl_idname = __package__

    game_models_folder: StringProperty(
        name="Textures Folder",
        subtype='FILE_PATH',
        description="If the path to Link's head texture on your system is this:\nD:\\BotW Extracted\\Models\\Link\\Link_Head_Alb.png\nThen in this box you should browse this:\nD:\\BotW Extracted\\Models\\"
    )
    game_icons_folder: StringProperty(
        name="Icons Folder",
        subtype='FILE_PATH',
        description="If the path to the Ancient Arrow's inventory icon is this:\nD:\\BotW Extracted\\Icons\\AncientArrow\\AncientArrow.jpg\nThen in this box you should browse this:\nD:\\BotW Extracted\\Icons\\"
    )
    game_anims_folder: StringProperty(
        name="Animations Folder",
        subtype='FILE_PATH',
        description="If the path to the Bear's Eat animation is this:\nD:\\BotW Extracted\\Animations\\Animal_Bear_Animation\\Eat.seanim\nThen in this box you should browse this:\nD:\\BotW Extracted\\Animations\\"
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(self, 'game_models_folder')
        layout.prop(self, 'game_icons_folder')
        layout.prop(self, 'game_anims_folder')

registry = [BotWImportPreferences]
