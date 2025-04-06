# This script makes material jsons that came out of my modified Switch Toolbox easier to process further.
# The input is the folder containing the root of the Switch Toolbox batch model extract, and the output is a folder with a flat list of json files.
# (It should be 27456 .json files adding up to almost 5gb)
# NOTE: To avoid irresponsible use, output_dir is NOT created for you, needs to exist before executing.
input_dir = "D:/BotW Assets/Models Backup"
out_dir = "D:/BotW Assets/Material Data Science/converted"

import json, os, re
from pathlib import Path
from collections import defaultdict

value_counts = defaultdict(lambda: defaultdict(int))

def write_more_readable_json_data(models_dir, output_dir):
    # Define the root directory
    root_dir = Path(models_dir)

    # Find all .dae files. We can't just rely on the .json files because it's not clear 
    # from their name where the object name begins and ends (because I should've used a 
    # different separator in Switch Toolbox than _)
    # NOTE: The material name does NOT always start with Mt_, eg. in FldObj_RuinStatueKnight_B_01, 
    # there's a material named Face_zou_Mt_Rock_RuinStatueKnightCrack_A. Face_zou is part of the material name, not the object.
    
    missing_materials = []
    materials_that_didnt_start_with_mt = []
    
    dae_files = list(root_dir.rglob("*.dae"))
    json_files = []
    for i, dae_filepath in enumerate(dae_files):
        print(f"Processing .dae: {i}/{len(dae_files)} {dae_filepath}")
        mat_names = read_dae_material_names(dae_filepath)
        dirpath = os.path.dirname(dae_filepath)
        obj_name = os.path.splitext(os.path.basename(dae_filepath))[0]
        for mat_name in mat_names:
            json_files.append((dirpath, obj_name, mat_name))

    for i, (dirpath, obj_name, mat_name) in enumerate(json_files):
        if not mat_name.startswith("Mt"):
            materials_that_didnt_start_with_mt.append(mat_name)
        json_dir_name = os.path.basename(dirpath)
        out_name = ".".join([json_dir_name, obj_name, mat_name, "json"])
        source_file = os.path.join(dirpath, obj_name+"_"+mat_name+".json")
        if not os.path.isfile(source_file):
            missing_materials.append((dirpath, obj_name, source_file))
            continue
        target_file = os.path.join(output_dir, out_name)
        print(f"{i+1}/{len(json_files)} {source_file}")
        if os.path.exists(target_file):
            # Don't overwrite, so the script can resume progress in case it gets interrupted.
            # If you want to start over, just delete the unfinished output files manually.
            continue
        # if i > 0:  # Limit for testing (can remove later)
        #    break
        try:
            with open(source_file, "r", encoding="utf-8") as f:
                data = json.load(f)  # Load JSON data
                data = traverse_json(data, flatten_single_key_dicts_processor)
                data = traverse_json(data, remove_redundant_name_processor)
                data = traverse_json(data, convert_named_list_to_dict_processor)
                data = traverse_json(data, process_renderinfo_only_processor)
                data = traverse_json(data, replace_value_key_processor)
                data = traverse_json(data, convert_strings_to_int_processor)
                data = traverse_json(data, convert_semicolon_strings_to_float_list_processor)
                data = traverse_json(data, replace_none_values_processor)
                data = traverse_json(data, extract_value_from_single_value_dict_processor)
                save_json(data, target_file)

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Skipping {source_file} due to error: {e}")

    print("Materials that didn't start with Mt_:")
    for mat in materials_that_didnt_start_with_mt:
        # There are like 200 of them, so don't rely on _Mt_ for much of anything. (TODO)
        print(mat)

    print("Missing materials:")
    for mat in missing_materials:
        print(mat)

def read_dae_material_names(filepath):
    """
    Reads a .dae file and extracts material IDs from the <library_materials> section.
    
    :param filepath: Path to the .dae file.
    :return: List of material ID strings.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regular expression to extract material ids
        material_ids = re.findall(r'<material id="(.*?)"', content)
        
        return material_ids
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def traverse_json(data, process_key_value):
    """
    Recursively traverses a JSON object and applies a processing function to each key-value pair.

    :param data: The JSON data (dict, list, or primitive value).
    :param process_key_value: A function that takes (key, value) and returns (new_key, new_value).
    :return: The processed JSON structure.
    """
    if isinstance(data, dict):
        return {
            process_key_value(k, v)[0]: traverse_json(process_key_value(k, v)[1], process_key_value)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [traverse_json(item, process_key_value) for item in data]
    else:
        return data  # Base case: return the value as-is if it's not a dict or list

def remove_redundant_name_processor(key, value):
    """Removes 'Name' property if it matches its parent key."""
    if isinstance(value, dict) and "Name" in value and value["Name"] == key:
        del value["Name"]
    return key, value  # Return the updated key-value pair

def convert_named_list_to_dict_processor(key, value):
    """Converts a list of dictionaries with 'Name' keys into a dictionary."""
    if isinstance(value, list) and all(isinstance(item, dict) and "Name" in item for item in value):
        # Convert list to dictionary: "Name" becomes the key, rest of the dictionary is the value
        converted_dict = {item["Name"]: {k: v for k, v in item.items() if k != "Name"} for item in value}
        return key, converted_dict  # Return the transformed structure
    return key, value  # Return unchanged if condition isn't met

def flatten_single_key_dicts_processor(key, value):
    """Flattens lists where each element is a dictionary with a single key."""
    if isinstance(value, list) and all(isinstance(item, dict) and len(item) == 1 for item in value):
        flattened = {k: v for item in value for k, v in item.items()}
        return key, flattened
    return key, value

def convert_strings_to_int_processor(key, value):
    """Converts numeric strings (including negative numbers) into integers."""
    if isinstance(value, str):
        try:
            return key, int(value)  # Try converting the string to an integer
        except ValueError:
            pass  # If conversion fails, return the original value
    return key, value  # Return unchanged if not a valid integer

def process_renderinfo_only_processor(key, value):
    """
    If the key is 'renderinfo', find the first non-null 'Value*' field in its children and replace the dictionary.
    """
    if key == "renderinfo" and isinstance(value, dict):
        for sub_key, sub_value in value.items():
            if isinstance(sub_value, dict):
                for inner_key, inner_value in sub_value.items():
                    if inner_key.startswith("Value") and inner_value is not None:
                        # If it's a list with a single value, extract it
                        if isinstance(inner_value, list) and len(inner_value) == 1:
                            value[sub_key] = inner_value[0]  # Replace with the single value
                        else:
                            value[sub_key] = inner_value  # Replace with the first non-null value
                        break  # Only process the first matching Value* field

    return key, value  # Return unchanged if not "renderinfo" or no match

def convert_semicolon_strings_to_float_list_processor(key, value):
    """
    Converts strings with ';' into lists of floats.
    Example: "0;0;0" → [0.0, 0.0, 0.0]
    """
    if isinstance(value, str) and ";" in value:
        try:
            return key, [float(num) for num in value.split(";")]  # Convert to list of floats
        except ValueError:
            pass  # Ignore if conversion fails (e.g., string contains non-numeric values)
    
    return key, value  # Return unchanged if condition isn't met

def replace_value_key_processor(key, value):
    """Replaces dictionaries containing only a '_value' key (or with extra metadata) with the '_value' itself."""
    if isinstance(value, dict) and "_value" in value:
        extracted_value = value["_value"]

        # If _value is a list with a single item, extract that item
        if isinstance(extracted_value, list) and len(extracted_value) == 1:
            extracted_value = extracted_value[0]

        return key, extracted_value  # Replace the dictionary with the extracted value

    return key, value  # Return unchanged if condition isn't met

def replace_none_values_processor(key, value):
    """
    Replaces any value that evaluates as False (e.g., None, empty string, empty list, etc.) with None.
    """
    if isinstance(value, bool):  # Don't modify boolean values
        return key, value  # Return the boolean value unchanged

    if not value:  # Checks if the value would evaluate to False
        return key, None  # Replace with None
    
    return key, value  # Return unchanged if value is not False

def extract_value_from_single_value_dict_processor(key, value):
    """
    If the value is a dictionary with exactly one key, and that key is 'Value',
    replace the dictionary with the value inside 'Value'.
    """
    if isinstance(value, dict) and len(value) == 1 and "Value" in value:
        return key, value["Value"]  # Replace with the value of 'Value'

    return key, value  # Return unchanged if conditions are not met

def save_json(data, filepath):
    # Define the file path for saving the statistics
    output_file = Path(filepath)

    # Write the statistics to a file in JSON format
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {filepath}")

write_more_readable_json_data(input_dir, out_dir)
