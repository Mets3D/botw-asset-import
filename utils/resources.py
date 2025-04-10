import bpy, os
from bpy.types import ID
from ..prefs import get_addon_prefs

RESOURCES_BLEND = "resources.blend"

def get_resources_blend_path() -> str:
    addon_dir = os.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[:-1])
    blend_path = os.sep.join([addon_dir, RESOURCES_BLEND])
    return blend_path

def ensure_lib_datablock(container_name, name, blend_path="", link=None) -> ID:
    """Load a datablock by appending/linking from a .blend file (default to the add-on's resources.blend), 
    unless they already exist in this file."""
    container = getattr(bpy.data, container_name)

    prefs = get_addon_prefs()
    if link==None:
        link = prefs.resource_append_mode=='LINK'
    abs_path = os.path.abspath(bpy.path.abspath(blend_path))
    if not blend_path:
        abs_path = get_resources_blend_path()
    assert os.path.isfile(abs_path), "File not found: "+blend_path

    # Check if it already exists.
    lib_path = next((lib.filepath for lib in bpy.data.libraries if os.path.abspath(bpy.path.abspath(lib.filepath)) == abs_path), None) if link else None
    pre_existing_datablock = container.get((name, lib_path))
    if pre_existing_datablock:
        # Datablock exists and we don't want to overwrite it, so just return it.
        return pre_existing_datablock

    # Import datablock from resources.blend file.
    with bpy.data.libraries.load(abs_path, link=link, relative=True) as (
        data_from,
        data_to,
    ):
        container_from = getattr(data_from, container_name)
        container_to = getattr(data_to, container_name)
        for o in container_from:
            if o == name:
                container_to.append(o)

    lib_path = next((lib.filepath for lib in bpy.data.libraries if os.path.abspath(bpy.path.abspath(lib.filepath)) == abs_path), None) if link else None
    new_datablock = container.get((name, lib_path))

    assert new_datablock, f"Datablock {name} not found in {container} in {abs_path} ({abs_path} != {lib_path})."

    return new_datablock

def ensure_widget(widget_name):
    if not widget_name.startswith("WGT-"):
        widget_name = "WGT-"+widget_name
    return ensure_lib_datablock('objects', widget_name)
