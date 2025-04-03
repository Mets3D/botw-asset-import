# For trying to understand material properties, it would be useful to list 
# out or import assets based on matching a set of material properties.
import bpy, os

from bl_ext.MyExtensionsLaptop.botw_asset_import.operators.botw_batch_asset_import import ensure_caches, get_shader_prop, import_and_process_dae
from bl_ext.MyExtensionsLaptop.botw_asset_import.prefs import get_addon_prefs

ALL_MATERIALS = ensure_caches()['shader_data']

match_props = {
    'shaderassign>options>uking_enable_texcoord0' : 1
}

def material_matches_props(shader_data):
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

matching_materials = sorted([filename for filename, shader in ALL_MATERIALS.items() if material_matches_props(shader)])

for i, m in enumerate(matching_materials):
    print(i, m)

# The stored materials are the json filenames, so let's turn those into the .dae filenames.
dae_files = [os.sep.join(jfile.split(".")[:-2])+".dae" for jfile in matching_materials]
dae_files = sorted(list(set(dae_files)))

print("Number of materials with matching props: ", len(matching_materials))
print(f"Across {len(dae_files)} assets.")

# Now we need to dig up where those .dae files are...
models_folder = get_addon_prefs().game_models_folder

directory = "D:/BotW Assets/Models Backup"

counter = 1
for root, dirs, files in os.walk(directory):
    for file in files:
        game_path = os.path.join(os.path.basename(root), file)
        if game_path in dae_files:
#            print(f"Importing: {counter}/{len(dae_files)} {game_path}")
            full_path = os.path.join(root, file)
#            import_and_process_dae(bpy.context, full_path)
            counter += 1