import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty, BoolProperty
from . import __package__ as base_package

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

    rename_collections: BoolProperty(
        name="Rename Collections",
        description="Try to make collection names more human-readable using name tables, prefix stripping, and other string operations. Useful when trying to create an asset library, but may be undesired if you want to do further scripting work on the assets. Note that regardless of this option, the original collection name is always stored in a 'file_name' custom property",
        default=True
    )
    rename_obj_mat: BoolProperty(
        name="Rename Objects",
        description="Make object/material names more human-readable by discarding default object names of 3D modeling softwares (pCube, pCylinder, etc), and the _Mt_ prefix",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(self, 'game_models_folder')
        layout.prop(self, 'game_icons_folder')
        layout.prop(self, 'game_anims_folder')

        layout.separator()
        row = layout.row()
        row.alignment = 'LEFT'
        row.label(text="Rename:")
        row.prop(self, 'rename_collections', text="", icon='OUTLINER_COLLECTION')
        row.prop(self, 'rename_obj_mat', text="", icon='OBJECT_DATAMODE')

def get_addon_prefs(context=None):
    if not context:
        context = bpy.context
    if base_package.startswith('bl_ext'):
        # 4.2
        return context.preferences.addons[base_package].preferences
    else:
        return context.preferences.addons[base_package.split(".")[0]].preferences

registry = [BotWImportPreferences]
