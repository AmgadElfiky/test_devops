import json


def delete_json_data(fileName):
    try:
        with open(fileName, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File Not Found.")
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
    for module_data in data[topic_name]:
        if module_name in module_data:
            data[topic_name].remove(module_data)
            break

    with open(fileName, "w") as file:
        json.dump(data, file, indent=2)
    print("JSON data Deleted successfully.")
