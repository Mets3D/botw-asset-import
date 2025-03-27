import json, os, glob
from collections import defaultdict

WILDCARDS = ("TextureMaps", "ShaderParams", "TextureRefs", "Samplers")

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
#    elif isinstance(data, list):
#        for index, item in enumerate(data):
#            new_path = f"{path}[{index}]" if path else f"[{index}]"
#            count_values(item, counts, new_path)
    elif isinstance(data, list):
        # Treat the whole list as a single value
        counts[path][str(data)] += 1  # Count the entire list as a single entity (as a string)
    else:
        if path in ('MaterialU.Name'):
            return
        counts[path][data] += 1  # Count occurrences of values per key path

def process_json_files(directory):
    """Processes all JSON files in the given directory with a simple progress counter."""
    counts = defaultdict(lambda: defaultdict(int))
    json_files = glob.glob(f"{directory}/*.json")

    json_files = [f for f in json_files if not f.endswith('SceneMaterial_MasterMaterial.json') and not os.path.basename(f).startswith("Deferred")]

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
            print("Skipping: ", path, num_values)
            continue

        print("Storing: ", path, num_values)
        defaults[path] = most_common_value
    return defaults

def save_counts(counts, output_file):
    """Saves the counts dictionary to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=4, ensure_ascii=False)


def save_defaults(defaults, output_file):
    """Saves the default values to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(defaults, f, indent=4, ensure_ascii=False)

manual_default_overrides = {
    "MaterialU.ShaderParams.*.DataOffset": "IGNORE",
    "MaterialU.ShaderParams.*.DependIndex": "IGNORE",
    "MaterialU.ShaderParams.*.DependedIndex": "IGNORE",
    "MaterialU.ShaderParams.*.Type": "IGNORE",
    "TextureMaps.*.textureUnit": "IGNORE",
    "matparam.*.DependIndex": "IGNORE",
    "matparam.*.DependedIndex": "IGNORE",
    "matparam.*.DataOffset": "IGNORE",
    # "matparam.*.Type": "IGNORE",

    "matparam.*.ValueSrt2D.Scaling": "[0.0, 0.0]",
    "matparam.*.ValueSrt2D.Translation": "[0.0, 0.0]",

    "matparam.*.ValueSrt3D.Scaling": "[0.0, 0.0, 0.0]",
    "matparam.*.ValueSrt3D.Rotation": "[0.0, 0.0, 0.0]",
    "matparam.*.ValueSrt3D.Translation": "[0.0, 0.0, 0.0]",
    "matparam.*.ValueSrt3D.Mode": "ModeMaya",

    "matparam.*.ValueTexSrt.Mode": "ModeMaya",
    "matparam.*.ValueTexSrt.Scaling": "[0.0, 0.0]",
    "matparam.*.ValueTexSrt.Rotation": "null",
    "matparam.*.ValueTexSrt.Translation": "[0.0, 0.0]",

    "matparam.*.ValueTexSrtEx.Mode": "ModeMaya",
    "matparam.*.ValueTexSrtEx.Scaling": "[0.0, 0.0]",
    "matparam.*.ValueTexSrtEx.Rotation": "null",
    "matparam.*.ValueTexSrtEx.Translation": "[0.0, 0.0]",
    "matparam.*.ValueTexSrtEx.MatrixPointer": "null",

    "matparam.*.Value_Unk": "null",
    "matparam.*.ValueFloat": "[0.0]",
}

# Usage
directory = "D:\\BotW Assets\\Material Data Science\\converted" # the output of material_json_convert.py
counts_file = "D:\\BotW Assets\\Material Data Science\\material_value_occurrences.json"
defaults_file = "D:\\BotW Assets\\Material Data Science\\material_defaults.json"
value_counts, num_files = process_json_files(directory)

#json_files = glob.glob(f"{directory}/*.json")
#num_files = len(json_files)
#with open(counts_file, "r", encoding="utf-8") as file:
#    value_counts = json.load(file)

defaults = get_default_values(value_counts, num_files-1)
defaults.update(manual_default_overrides)
save_counts(value_counts, counts_file)
save_defaults(defaults, defaults_file)
