# Modified from bmubin: https://github.com/augmero/bmubin/blob/main/scripts/asset/dae_fixer.py
# I don't bother changing texture paths, since I get that info from material jsons instead.
# I also don't make copies of the .dae files but modify them in place because YOLO.
# I also don't do it as a separate step which would be more optimal, but instead do it every time I import, which is more convenient. 
# (ofc processing a given .dae file a 2nd or 3rd time won't do anything anymore.)

import re

def fix_dae_uvmaps_in_place(dae_file_path):
    lines_to_write = []
    with open(dae_file_path, 'r') as file:
        lines_to_write = file.readlines()
        lines_to_write = simplify_names(lines_to_write)
    if not lines_to_write:
        return
    with open(dae_file_path, 'w') as file:
        file.writelines(lines_to_write)


def simplify_names(lines: list[str]):
    # Fixes blender import issues
    name_cache = {}
    uv_map_counter = 0
    vertex_col_counter = 0
    
    # First pass: Build name cache.
    for line in lines:
        # TEXCOORD
        regex_match = re.search('source=".*-texcoord', line)
        if regex_match:
            matched_name = regex_match.group()[9:]
            if matched_name in name_cache:
                continue
            matched_name_value = f'UVMap{uv_map_counter}-texcoord'
            name_cache[matched_name] = matched_name_value
            uv_map_counter += 1

        # VCOLOR
        regex_match = re.search('source=".*-color', line)
        if regex_match:
            matched_name = regex_match.group()[9:]
            if matched_name in name_cache:
                continue
            matched_name_value = f'Color{vertex_col_counter}-color'
            name_cache[matched_name] = matched_name_value
            vertex_col_counter += 1

    if uv_map_counter == vertex_col_counter == 0:
        return False

    # Second pass: Rename
    lines_to_write = lines
    for key, value in name_cache.items():
        lines_to_write = [re.sub(key, value, x) for x in lines_to_write]
    return lines_to_write
