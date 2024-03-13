import re
import json


def edit_data(fileName):
    # Load the JSON data from the file
    with open(fileName, "r") as file:
        data = json.load(file)

    # Prompt the user for module name and day name
    topic_name = input("Enter the Topic name (e.g., devops): ")
    module_name = input("Enter the Module name (e.g., linux): ")


    # Define regular expressions for the user input module and day
    module_regex = re.compile(rf"\b{module_name}\b", re.IGNORECASE)


    # Search for the specified module and day
    for module in data[topic_name]:
        if any(module_regex.match(key) for key in module):
            print("module: ", module)
            for item in module:
                item = input("Enter the new item: ")
                module.append(item)

    # Write the updated JSON data back to the file
    with open(fileName, "w") as file:
        json.dump(data, file, indent=2)

    print("Data added successfully.")
