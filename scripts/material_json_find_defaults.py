# After running material_json_convert.py, this script goes through all of the .json files
# and writes two new files: material_value_occurrences.json contains a listing of how often each material property has a certain value.
# That can be useful to find correlations. Maybe.
# And material_defaults.json, a copy of which is included with this addon, in the databases folder, and is (arguably) used by the material importer.
# (The importer probably never actually does anything special when encountering a default value)

converted_jsons = "D:\\BotW Assets\\Material Data Science\\converted" # the output of material_json_convert.py
output_value_occurrences = "D:\\BotW Assets\\Material Data Science\\material_value_occurrences.json"
output_defaults = "D:\\BotW Assets\\Material Data Science\\material_defaults.json"
process_value_occurrences = False

import json, glob, re
from collections import defaultdict

WILDCARDS = ("TextureMaps", "ShaderParams", "TextureRefs", "Samplers")

manual_default_overrides = {
    "Material": "IGNORE",
    "MaterialU>ShaderAssign>ShaderOptions": "IGNORE",
    "MaterialU>RenderInfos": "IGNORE",

    "MaterialU>ShaderParams>*>DataOffset": "IGNORE",
    "MaterialU>ShaderParams>*>DependIndex": "IGNORE",
    "MaterialU>ShaderParams>*>DependedIndex": "IGNORE",
    "MaterialU>ShaderParams>*>Type": "IGNORE",
    "MaterialU>TextureRefs>*>Texture": "IGNORE",
    # "TextureMaps>*>textureUnit": "IGNORE",
    "matparam>*>DependIndex": "IGNORE",
    "matparam>*>DependedIndex": "IGNORE",
    "matparam>*>DataOffset": "IGNORE",

    "matparam>*>ValueSrt2D>Scaling": [0.0, 0.0],
    "matparam>*>ValueSrt2D>Translation": [0.0, 0.0],

    "matparam>*>ValueSrt3D>Scaling": [0.0, 0.0, 0.0],
    "matparam>*>ValueSrt3D>Rotation": [0.0, 0.0, 0.0],
    "matparam>*>ValueSrt3D>Translation": [0.0, 0.0, 0.0],
    "matparam>*>ValueSrt3D>Mode": "ModeMaya",

    "matparam>*>ValueTexSrt>Mode": "ModeMaya",
    # "matparam>*>ValueTexSrt>Scaling": [0.0, 0.0],
    "matparam>*>ValueTexSrt>Translation": [0.0, 0.0],

    "matparam>*>ValueTexSrtEx>Mode": "ModeMaya",
    "matparam>*>ValueTexSrtEx>Scaling": [0.0, 0.0],
    "matparam>*>ValueTexSrtEx>Translation": [0.0, 0.0],

    # "matparam>*>ValueFloat": [0.0],
    "matparam>*>HasPadding": "IGNORE",
    "matparam>*>HasPadding": "IGNORE",
    # "matparam>*>PaddingLength": "IGNORE",

    "matparam>gsys_bake_st0": "IGNORE",
    "matparam>gsys_bake_st1": "IGNORE",
    "matparam>gsys_alpha_test_ref_value": "IGNORE",
    "matparam>gsys_bake_light_scale": "IGNORE",

    "MaterialU>ShaderParamData": "IGNORE",  # I don't know what this is and it's a lot of data, so meh.
    "MaterialU>Name": "IGNORE", # Because it's always the same as "text"> Also the same as the end of the filename, starting with Mt_ so, meh.
    **{f"matparam>tex_srt{i}>ValueTexSrt>Scaling" : [1.0, 1.0] for i in range(6)},
    **{f"matparam>texture_array_index{i}>ValueFloat" : [0.0] for i in range(6)},
}

# Some values we want to be able to read without stressing about whether they exist or not.
# Also they deviate from the most common value very often.
force_no_default = [
    "TextureMaps>*>Type",
    "TextureMaps>*>textureUnit",
    "TextureMaps>*>SamplerName",
    "isTransparent",
    "text",
]

def count_values(data, counts, path=""):
    """Recursively counts occurrences of values for each key in the JSON."""
    if isinstance(data, dict):
        for key, value in data.items():
            # Special handling for 'TextureMaps' to treat them as grouped data
            if key in WILDCARDS:
                # Iterate over the values inside TextureMaps and skip the entry names
                if not value:
                    print("No value here: ", path, key)
                    continue
                for entry_name, entry_data in value.items():
                    new_path = f"{path}>{key}>*" if path else f"{key}>*"
                    count_values(entry_data, counts, new_path)
            else:
                new_path = f"{path}>{key}" if path else key
                count_values(value, counts, new_path)
    elif isinstance(data, list):
        # Treat the whole list as a single value
        counts[path][str(data)] += 1
    else:
        if path in (''):
            return
        counts[path][data] += 1

def get_json_list(directory):
    json_files = glob.glob(f"{directory}/*.json")
    return json_files

def process_json_files(directory):
    counts = defaultdict(lambda: defaultdict(int))

    json_files = get_json_list(directory)
    total_files = len(json_files)

    for index, filepath in enumerate(json_files, start=1):
        # if index > 100:
        #     break
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                count_values(data, counts)
        except json.JSONDecodeError:
            # This should never happen.
            print(f"Error reading {filepath}")

        print(f"{index}/{total_files} {filepath}")

    return counts, total_files

def get_default_values(counts: dict, num_files: int):
    """Determines the most common value for each key path, if the total number 
    of recorded values for that key path matches or exceeds the number of files counted."""
    defaults = {}
    for path, value_counts in counts.items():
        # Get the most common value (max based on frequency)
        most_common_value = max(value_counts.items(), key=lambda item: item[1])[0]
        num_values = sum([value for key, value in value_counts.items()])
        if num_values < num_files:
            # If a value is not present in all files, don't store it as a default value.
            continue

        # Convert it from string to pythonic representation
        try:
            real_value = json.loads(most_common_value)
        except:
            real_value = most_common_value
        defaults[path] = real_value

    for path in force_no_default + list(manual_default_overrides.keys()):
        paths = [path]
        if "*" in path:
            paths = [key for key in defaults.keys() if re.match(path.replace("*", ".*"), key)]
        for new_path in paths:
            if new_path not in defaults:
                continue
            del defaults[new_path]

    for path, value in manual_default_overrides.items():
        if value == 'IGNORE':
            paths = [path]
            if "*" in path:
                paths = [key for key in defaults.keys() if re.match(path.replace("*", ".*"), key)]
            else:
                paths = [key for key in defaults.keys() if key.startswith(path+">") or key==path]
            for new_path in paths:
                del defaults[new_path]

    defaults.update(manual_default_overrides)

    return defaults

def save_value_occurrences(counts, output_file):
    """Saves the counts dictionary to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=4, ensure_ascii=False)

def save_defaults(defaults, output_file):
    """Saves the default values to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as file:
        # Keep lists single-line and sort alphabetically
        json_str = json.dumps(dict(sorted(defaults.items())), indent=2)
        json_str = re.sub(r"\[\s+([^\[\]]+?)\s+\]", lambda m: "[" + " ".join(m.group(1).split()) + "]", json_str)
        file.write(json_str)

json_files = get_json_list(converted_jsons)
num_files = len(json_files)

if process_value_occurrences:
    value_counts, num_files = process_json_files(converted_jsons)
    save_value_occurrences(value_counts, output_value_occurrences)
else:
    with open(output_value_occurrences, "r", encoding="utf-8") as file:
        value_counts = json.load(file)

defaults = get_default_values(value_counts, num_files-1)
save_defaults(defaults, output_defaults)
