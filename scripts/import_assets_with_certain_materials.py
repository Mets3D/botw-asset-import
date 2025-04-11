# For trying to understand material properties, it would be useful to list 
# out or import assets based on matching a set of material properties.
import bpy, os

from bl_ext.MyExtensionsLaptop.botw_asset_import.operators.botw_asset_import.constants import ensure_caches
from bl_ext.MyExtensionsLaptop.botw_asset_import.operators.botw_asset_import.process_material import get_shader_prop
from bl_ext.MyExtensionsLaptop.botw_asset_import.operators.botw_asset_import import import_and_process_dae
from bl_ext.MyExtensionsLaptop.botw_asset_import.prefs import get_models_folder

ALL_MATERIALS = ensure_caches()['shader_data']

match_props = {
    'matparam>const_value7>ValueFloat' : 0.2
}
do_import = 40
hide_irrelevant_objs = False

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

def match_material_props_uvstuff(filename, shader_data):
    sampler_use_array = get_shader_prop(shader_data, 'shaderassign>options>uking_sampler_use_array')==1
#    if sampler_use_array:
#        return True
    if not sampler_use_array:
        return False

    any_tex_idx = any([get_shader_prop(shader_data, f'shaderassign>options>uking_texture_array_texture{i}')==1 for i in range(5)])

#    if not any_tex_idx:
#        return True

    all_texturemaps = get_shader_prop(shader_data, 'TextureMaps')
    all_samplers = [data['SamplerName'] for name, data in all_texturemaps.items()]
    a1_sampler = "_a1" in all_samplers
    
    more_than_one_albedo = len([name for name, data in all_texturemaps.items() if "_Alb" in name or "MaterialAlb" in name])>1

    if not any_tex_idx and not more_than_one_albedo and not a1_sampler:
        return True

    return False

matching_materials = sorted([filename for filename, shader in ALL_MATERIALS.items() if match_material_props(filename, shader)])

for i, m in enumerate(matching_materials):
    print(i, m)

# The stored materials are the json filenames, so let's turn those into the .dae filenames.
dae_files = [os.sep.join(jfile.split(".")[:-2])+".dae" for jfile in matching_materials]
dae_files = sorted(list(set(dae_files)))

print("Number of materials with matching props: ", len(matching_materials))
print(f"Across {len(dae_files)} assets.")

# Now we need to dig up where those .dae files are...
models_folder = get_models_folder()

directory = "D:/BotW Assets/Models Backup"

if do_import:
    counter = 1
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "DgnObj" in file:
                continue
            if counter > do_import:
                break
            game_path = os.path.join(os.path.basename(root), file)
            if game_path in dae_files:
                full_path = os.path.join(root, file)
                print(f"Importing: {counter}/{len(dae_files)} {game_path}")
                import_and_process_dae(bpy.context, full_path)
                counter += 1

if hide_irrelevant_objs:
    import json
    for obj in bpy.data.objects:
        if obj.type != 'MESH':
            continue
        mat = obj.data.materials[0]
        data = json.loads(mat['shader_data'])
        for key, value in match_props.items():
            parts = key.split(">")
            for part in parts:
                if part not in data:
                    obj.hide_set(True)
                    break
                data = data[part]
            if obj.visible_get():
                if data != value:
                    obj.hide_set(True)