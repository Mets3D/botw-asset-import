import json, os, glob, re
from collections import defaultdict

WILDCARDS = ("TextureMaps", "ShaderParams", "TextureRefs", "Samplers")

manual_default_overrides = {
    "MaterialU.ShaderParams.*.DataOffset": "IGNORE",
    "MaterialU.ShaderParams.*.DependIndex": "IGNORE",
    "MaterialU.ShaderParams.*.DependedIndex": "IGNORE",
    "MaterialU.ShaderParams.*.Type": "IGNORE",
    # "TextureMaps.*.textureUnit": "IGNORE",
    "matparam.*.DependIndex": "IGNORE",
    "matparam.*.DependedIndex": "IGNORE",
    "matparam.*.DataOffset": "IGNORE",

    "matparam.*.ValueSrt2D.Scaling": [0.0, 0.0],
    "matparam.*.ValueSrt2D.Translation": [0.0, 0.0],

    "matparam.*.ValueSrt3D.Scaling": [0.0, 0.0, 0.0],
    "matparam.*.ValueSrt3D.Rotation": [0.0, 0.0, 0.0],
    "matparam.*.ValueSrt3D.Translation": [0.0, 0.0, 0.0],
    "matparam.*.ValueSrt3D.Mode": "ModeMaya",

    "matparam.*.ValueTexSrt.Mode": "ModeMaya",
    "matparam.*.ValueTexSrt.Scaling": [0.0, 0.0],
    "matparam.*.ValueTexSrt.Translation": [0.0, 0.0],

    "matparam.*.ValueTexSrtEx.Mode": "ModeMaya",
    "matparam.*.ValueTexSrtEx.Scaling": [0.0, 0.0],
    "matparam.*.ValueTexSrtEx.Translation": [0.0, 0.0],

    "matparam.gsys_bake_light_scale.Type": "Float3",
    "matparam.gsys_bake_st0.Type": "Float4",
    "matparam.gsys_bake_st1.Type": "Float4",
    "matparam.gsys_alpha_test_ref_value.Type": "Float",
    "matparam.gsys_bake_light_scale.ValueFloat": [1.0, 1.0, 1.0],

    # "matparam.*.ValueFloat": [0.0],
    "matparam.*.HasPadding": "IGNORE",
    "matparam.*.HasPadding": "IGNORE",
    # "matparam.*.PaddingLength": "IGNORE",

    "MaterialU.ShaderParamData": "IGNORE",  # I don't know what this is and it's a lot of data, so meh.
    "MaterialU.Name": "IGNORE", # Because it's always the same as "text". Also the same as the end of the filename, starting with Mt_ so, meh.
    **{f"matparam.tex_srt{i}.ValueTexSrt.Scaling" : [1.0, 1.0] for i in range(6)},
    **{f"matparam.texture_array_index{i}.ValueFloat" : [0.0] for i in range(6)},
}

# Some values we want to be able to read without stressing about whether they exist or not.
# Also they deviate from the most common value very often.
force_no_default = [
    "TextureMaps.*.Type",
    "TextureMaps.*.textureUnit",
    "TextureMaps.*.SamplerName",
    "TextureMaps.*.WrapModeS",
    "TextureMaps.*.WrapModeT",
    "isTransparent",
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
                    new_path = f"{path}.{key}.*" if path else f"{key}.*"
                    count_values(entry_data, counts, new_path)
            else:
                new_path = f"{path}.{key}" if path else key
                count_values(value, counts, new_path)
    elif isinstance(data, list):
        # Treat the whole list as a single value
        counts[path][str(data)] += 1
    else:
        if path in ('MaterialU.Name'):
            return
        counts[path][data] += 1

def get_json_list(directory):
    json_files = glob.glob(f"{directory}/*.json")
    json_files = [f for f in json_files if not f.endswith('SceneMaterial_MasterMaterial.json') and not os.path.basename(f).startswith("Deferred")]
    return json_files

def process_json_files(directory):
    """Processes all JSON files in the given directory with a simple progress counter."""
    counts = defaultdict(lambda: defaultdict(int))

    json_files = get_json_list(directory)
    total_files = len(json_files)

    for index, filepath in enumerate(json_files, start=1):
#        if index > 100:
#            break
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                count_values(data, counts)
        except json.JSONDecodeError:
            print(f"Error reading {filepath}")

        print(f"Processing: {index}/{total_files}")

    return counts, total_files


def get_default_values(counts: dict, num_files: int):
    """Determines the most common value for each key path, if the total number 
    of recorded values for that key path matches or exceeds the number of files counted."""
    defaults = {}
    print("Num files: ", num_files)
    for path, value_counts in counts.items():
        # Get the most common value (max based on frequency)
        most_common_value = max(value_counts.items(), key=lambda item: item[1])[0]
        num_values = sum([value for key, value in value_counts.items()])
        if num_values < num_files:
            # If a value is not present in all files, don't store it as a default value.
            print("Skipping: ", path, num_values)
            continue

        print("Storing: ", path, num_values)

        # Convert it from string to pythonic representation
        try:
            real_value = json.loads(most_common_value)
        except:
            real_value = most_common_value
        defaults[path] = real_value

    for path in force_no_default + list(manual_default_overrides.keys()):
        matching_keys = [path]
        if "*" in path:
            matching_keys = [key for key in defaults.keys() if re.match(path.replace(".", "\\.").replace("*", ".*"), key)]
        for new_path in matching_keys:
            if new_path not in defaults:
                print("Couldn't remove ", path)
                continue
            del defaults[new_path]

    defaults.update(manual_default_overrides)

    for key, value in list(defaults.items()):
        if value == None:
            del defaults[key]

    return defaults

def save_counts(counts, output_file):
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

# Usage
directory = "D:\\BotW Assets\\Material Data Science\\converted" # the output of material_json_convert.py
counts_file = "D:\\BotW Assets\\Material Data Science\\material_value_occurrences.json"
defaults_file = "D:\\BotW Assets\\Material Data Science\\material_defaults.json"

json_files = get_json_list(directory)
num_files = len(json_files)
with open(counts_file, "r", encoding="utf-8") as file:
    value_counts = json.load(file)

# value_counts, num_files = process_json_files(directory)
# save_counts(value_counts, counts_file)

defaults = get_default_values(value_counts, num_files-1)
save_defaults(defaults, defaults_file)
