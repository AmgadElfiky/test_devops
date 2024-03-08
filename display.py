import json


def display_json_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print(json.dumps(data, indent=2))
    except FileNotFoundError:
        print("File not found.")
