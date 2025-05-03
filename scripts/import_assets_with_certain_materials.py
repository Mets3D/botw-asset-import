# For trying to understand material properties, it's useful to list 
# out or import assets based on matching a set of material properties.
import bpy, os

from bl_ext.MyExtensionsHomePC.botw_asset_import.operators.botw_asset_import.constants import ensure_caches
from bl_ext.MyExtensionsHomePC.botw_asset_import.operators.botw_asset_import.process_material import get_shader_prop, is_blown_by_wind
from bl_ext.MyExtensionsHomePC.botw_asset_import.operators.botw_asset_import import import_and_process_dae
from bl_ext.MyExtensionsHomePC.botw_asset_import.prefs import get_models_folder

ALL_MATERIALS = ensure_caches()['shader_data']

match_props = {
    'shaderassign>options>uking_enable_wind_vtx_transform' : 1,
#    'shaderassign>options>uking_material_behave' : 105,

#    'shaderassign>options>uking_enable_wind_vtx_transform_normal_lock' : None,
#    'shaderassign>options>uking_wind_vtx_transform_channel' : 41,
#    'shaderassign>options>uking_metal_channel' : 20,
#    'shaderassign>options>uking_metal_color' : 3,
}
do_import = 0
skip = 0
hide_irrelevant_objs = True

def match_material_props(filename, shader_data):
    for key, value in match_props.items():
        mat_value = get_shader_prop(shader_data, key)
#        if mat_value != 1:
#            return True
        if type(value) == list:
            if mat_value not in value:
                return False
        elif mat_value != value:
            return False
    return True

def any_in_any(words, textures) -> bool:
    return any([any([word in texture for word in words]) for texture in textures])

matching_materials = sorted([filename for filename, shader in ALL_MATERIALS.items() if is_blown_by_wind(shader)])

for i, m in enumerate(matching_materials):
    if i<skip:
        continue
    print(i, m)

# The stored materials are the json filenames, so let's turn those into the .dae filenames.
dae_files = [os.sep.join(jfile.split(".")[:-2])+".dae" for jfile in matching_materials]
dae_files = sorted(list(set(dae_files)))

print("Number of materials with matching props: ", len(matching_materials))
print(f"Across {len(dae_files)} assets.")

def import_stuff():
    counter = 1
    for root, dirs, files in os.walk(get_models_folder()):
        for file in files:
            game_path = os.path.join(os.path.basename(root), file)
            if "_Far" in file:
                continue
            if game_path not in dae_files:
                continue
            if not file.endswith(".dae"):
                continue
            if "DgnObj" in file:
                continue
            if counter<skip:
                counter += 1
                continue
            if counter > do_import+skip:
                break

            full_path = os.path.join(root, file)
            print(f"Importing: {counter}/{len(dae_files)} {game_path}")
            import_and_process_dae(bpy.context, full_path)
            counter += 1

def do_hide_irrelevant_objs():
    for obj in bpy.data.objects:
        if obj.type != 'MESH':
            continue
        if len(obj.data.materials)==0:
            continue
        mat = obj.data.materials[0]
        if 'json_name' not in mat:
            continue
        if mat['json_name'] not in matching_materials:
            print("Hide ", obj.name)
            try:
                obj.hide_set(True)
            except RuntimeError: pass

if do_import:
    import_stuff()

if hide_irrelevant_objs:
    do_hide_irrelevant_objs()