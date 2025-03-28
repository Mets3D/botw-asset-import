import json, glob, os

def load_defaults(default_file):
    """Loads the defaults from the defaults.json file."""
    with open(default_file, "r", encoding="utf-8") as file:
        return json.load(file)

WILDCARDS = ("TextureMaps", "ShaderParams", "TextureRefs", "Samplers")

def get_default_path(data_path):
    parts = data_path.split(".")
    for i, part in enumerate(parts):
        if part in WILDCARDS and part!=parts[-1]:
            parts[i+1] = "*"
            break # meh, our data only ever has 1 wildcard.
    return ".".join(parts)

def remove_defaults(data, defaults, path=""):
    """Recursively removes keys whose values match the default values."""
    if isinstance(data, dict):
        cleaned_data = {}
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            default_path = get_default_path(new_path)

            # I doubt None is ever useful / overriding anything. Removing them helps filter out a lot of noise.
            ignore = value == None
            if not ignore:
                for default_path in (new_path, default_path):
                    if default_path in defaults:
                        default_value = defaults[default_path]
                        if default_value in ('IGNORE', value, json.dumps(value)):
                            ignore = True
                            break
            if ignore:
                continue

            cleaned_sub_data = remove_defaults(value, defaults, new_path)
            if cleaned_sub_data != {}:
                # NOTE: Important this only discards empty dictionaries, otherwise False or None values would get skipped when they shouldn't.
                cleaned_data[key] = cleaned_sub_data

        return cleaned_data

    return data

def process_json_files(input_directory, output_directory, defaults):
    """Processes all JSON files, removing keys with default values and saving to a new folder."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the output directory if it doesn't exist
    
    json_files = glob.glob(f"{input_directory}/*.json")  # Get all JSON files

    for i, filepath in enumerate(json_files):
        print(f"{i}/{len(json_files)}: {filepath}")
        if i > 0:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                cleaned_data = remove_defaults(data, defaults)

            # Save the cleaned JSON to the output folder
            output_filepath = os.path.join(output_directory, os.path.basename(filepath))
            with open(output_filepath, "w", encoding="utf-8") as file:
                json.dump(cleaned_data, file, indent=2, ensure_ascii=False)
        
        except json.JSONDecodeError:
            print(f"Error reading {filepath}")

defaults_file = "D:\\BotW Assets\\Material Data Science\\material_defaults.json"
input_directory = "D:\\BotW Assets\\Material Data Science\\converted" # the output of material_json_convert.py
output_directory = "D:\\BotW Assets\\Material Data Science\\shrunk"
defaults = load_defaults(defaults_file)
process_json_files(input_directory, output_directory, defaults)
