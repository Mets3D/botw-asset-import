import bpy, os
from bpy.types import Object
from ..prefs import get_addon_prefs

def get_resources_blend_path() -> str:
    addon_dir = os.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[:-1])
    blend_path = os.sep.join([addon_dir, 'resources.blend'])
    return blend_path

def ensure_widget(wgt_name, source_file="") -> Object:
    """Load custom shapes by appending them from resources.blend, unless they already exist in this file."""
    prefs = get_addon_prefs()
    link = prefs.resource_append_mode=='LINK'
    abs_path = bpy.path.abspath(source_file)
    if not source_file:
        abs_path = get_resources_blend_path()
    # Check if it already exists locally.
    if not wgt_name.startswith("WGT-"):
        wgt_name = "WGT-" + wgt_name
    old_wgt_ob = bpy.data.objects.get((wgt_name, None))
    if old_wgt_ob and not link:
        # Object exists and we don't want to overwrite it, so just return it.
        return old_wgt_ob

    # Import widget object from resources.blend file.
    with bpy.data.libraries.load(abs_path, link=link, relative=True) as (
        data_from,
        data_to,
    ):
        for o in data_from.objects:
            if o == wgt_name:
                data_to.objects.append(o)

    new_wgt_ob = bpy.data.objects.get((wgt_name, None))

    return new_wgt_ob
