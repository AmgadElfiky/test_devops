import json
from addData import enterData


def edit_json_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return

    topic_name = input("Enter the topic name you want to edit: ")
    if topic_name not in data:
        print("Topic not found.")
        return

    module_name = input("Enter the module name you want to edit: ")
    module_found = False

    for module_data in data[topic_name]:
        if module_name in module_data:
            module_found = True
            break

    if not module_found:
        print("Module not found.")
        return

    while True:
        try:
            num_days = int(
                input("Enter the number of days for {}: ".format(module_name))
            )
            if num_days < 0:
                raise ValueError("Number of days cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Remove old module data
    for module_data in data[topic_name]:
        if module_name in module_data:
            data[topic_name].remove(module_data)
            break

    enterData(data[topic_name], num_days, module_name)

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print("JSON data edited successfully.")
