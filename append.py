import json


def append_to_json_file(filename, new_data):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Append the new data to the existing data
    existing_data.append(new_data)

    # Write the combined data back to the file
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=2)
