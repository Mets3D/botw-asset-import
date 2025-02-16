from bpy.types import AddonPreferences
from bpy.props import StringProperty

class BotWImportPreferences(AddonPreferences):
    bl_idname = __package__

    game_models_folder: StringProperty(
        name="Models Folder",
        subtype='FILE_PATH',
        description="Path to extracted BotW Models folder, with the .png textures within each sub-folder"
    )
    game_icons_folder: StringProperty(
        name="Icons Folder",
        subtype='FILE_PATH',
        description="Path to folder of extracted BotW Icons, in .jpg format"
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(self, 'game_models_folder')
        layout.prop(self, 'game_icons_folder')

registry = [BotWImportPreferences]
