import re

from ...databases.asset_names import asset_names
from .constants import PRIMITIVE_NAMES, OBJ_PREFIXES

def rename_object(collection, obj):
    new_name = obj.name
    if "_Mt_" in new_name:
        new_name = new_name.split("_Mt_")[0]

    # TODO: Shouldn't this be collection.name instead?
    new_name = collection['asset_name'] + "_" + new_name

    if len(new_name) < 64:
        obj.name = new_name
    else:
        # This should never happen because we don't make names longer here.
        print("Couldn't rename due to 63-char limit: ", obj.name, new_name)

def derive_asset_name(dae_filename: str, dirname: str, remove_prefixes=True) -> str:
    without_ext = dae_filename.replace(".dae", "")
    asset_name = asset_names.get(without_ext, without_ext)

    # If the asset name wasn't in the dictionary, try without any _A, _B suffixes.
    if asset_name == without_ext and (without_ext.endswith("_A") or without_ext.endswith("_B")):
        asset_name = asset_names.get(without_ext[:-2], without_ext[:-2])

    # Guess Weapon sheaths based on the entries for weapons in the dictionary.
    for find, replace in (("Lsheath", "Lsword"), ("SpearSheath", "Spear"), ("Sheath", "Sword")):
        if asset_name == without_ext and find in asset_name:
            weapon_name = asset_names.get(asset_name.replace(find, replace))
            if weapon_name:
                asset_name = weapon_name + " Sheath"
                break

    # Make the "Enemy_" prefix optional in the dictionary.
    if asset_name == without_ext and "Enemy" in asset_name:
        asset_name = asset_names.get(asset_name.replace("Enemy_", ""), asset_name)

    if not remove_prefixes:
        return asset_name

    return tidy_name(asset_name)

def tidy_name(name):
    """This function is allowed to be fairly "destructive" in order to achieve a clean looking name,
    even at the cost of uniqueness (eg. a lot of garbage names might get turned into the same clean name)
    """
    trash = PRIMITIVE_NAMES + ["_Model", "_Root", "_lowpoly", "_low", "__abc", "_Mdl"]
    swap = {
        "_": " ",
        "  " : " ",
        "D L C" : "DLC",
    }

    new_name = name

    if "_MT_" in new_name:
        new_name = new_name.split("_MT_")[1]

    # Nuke certain strings
    for word in trash:
        new_name = new_name.replace(word, "")

    # Remove some prefixes
    for prefix in OBJ_PREFIXES:
        if new_name.startswith(prefix):
            new_name = new_name[len(prefix):]

    # Change CamelCase to Title Case
    new_name = re.sub(r'(?<!^)(?=[A-Z])', ' ', new_name)

    # Find and replace as per the `swap` dict
    for find, replace in swap.items():
        if find in new_name:
            new_name = new_name.replace(find, replace)

    # Remove _001
    suffix_pattern = re.compile(r"\_\d{3}$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    # Remove .001
    suffix_pattern = re.compile(r"\.\d{3}$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    # Remove _group###
    suffix_pattern = re.compile(r"_group\d*$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    if new_name.endswith("_"):
        new_name = new_name[:-1]

    # Remove numbers from end unless preceeded by a symbol (usually . or _)
    suffix_pattern = re.compile(r"(?<=[A-Za-z])\d+$")
    if suffix_pattern.search(new_name):
        new_name = suffix_pattern.sub("", new_name)

    return new_name
