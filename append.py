import json

def append_to_json_file(filename, topic_name, new_module_data):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Update the data with new module data
    if topic_name in data:
        data[topic_name].extend(new_module_data)
    else:
        data[topic_name] = new_module_data

    # Write the data back to the file
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)