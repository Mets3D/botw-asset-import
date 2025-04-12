
from bpy.types import bpy_struct

from rna_prop_ui import rna_idprop_ui_create


def make_property(
    owner: bpy_struct,
    name: str,
    default,
    *,
    value=None,
    id_type=None,
    subtype: str | None = None,
    ###
    description: str | None = None,
    overridable=True,
    ###
    min: float = 0.0,
    max: float = 1.0,
    soft_min=None,
    soft_max=None,
    ###
    **options,
):
    """
    Creates and initializes a custom property of owner.

    The soft_min and soft_max parameters default to min and max.
    Description defaults to the property name.
    """

    value = value or default

    # Some keyword argument defaults differ
    try:
        rna_idprop_ui_create(
            owner,
            name,
            default=default,
            min=min,
            max=max,
            soft_min=soft_min,
            soft_max=soft_max,
            description=description or name,
            overridable=overridable,
            subtype=subtype,
            id_type=id_type,
            **options,
        )

        owner.property_overridable_library_set(f'["{name}"]', overridable)
    except TypeError:
        # Python custom properties will throw an error when trying to call update() on them, but it doesn't matter.
        pass

    if value and value != default:
        owner[name] = value

def copy_property(from_owner, to_owner, prop_name):
    try:
        prop_data = from_owner.id_properties_ui(prop_name).as_dict()
    except TypeError:
        # This should only happen with python dictionaries.
        prop_data = {'default': from_owner[prop_name]}

    value = from_owner[prop_name]
    if hasattr(value, 'to_list'):
        value = value.to_list()
    elif hasattr(value, 'to_dict'):
        value = value.to_dict()

    prop_data['value'] = value
    prop_data['overridable'] = from_owner.is_property_overridable_library(
        f'["{prop_name}"]'
    )

    if 'description' not in prop_data:
        prop_data['description'] = ""

    make_property(to_owner, prop_name, **prop_data)
