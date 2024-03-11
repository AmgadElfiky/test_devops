import json
import re


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


def delete_activity_data(fileName):
    # Load the JSON data from the file
    with open(fileName, "r") as file:
        data = json.load(file)

    # Prompt the user for module name and day name
    topic_name = input("Enter the Topic name (e.g., devops): ")
    module_name = input("Enter the Module name (e.g., linux): ")
    day_name = input("Enter the day name (e.g., day1): ")
    # day_index = input("Enter the day index (e.g., intro): ")

    # Define regular expressions for the user input module and day
    module_regex = re.compile(rf"\b{module_name}\b", re.IGNORECASE)
    day_regex = re.compile(rf"\b{day_name}\b", re.IGNORECASE)
    # index_regex = re.compile(rf"\b{day_index}\b", re.IGNORECASE)

    # Search for the specified module and day
    for module in data[topic_name]:
        if any(module_regex.match(key) for key in module):
            # print("module: ", module)
            for day in module[module_name]:
                if any(day_regex.match(key) for key in day):
                    # print("day: ", day)
                    new_day = day[day_name]
                    for index, day_item in enumerate(new_day):
                        # show_index = index + 1
                        print(f"index: {index}, day_item: {day_item}")
                    for index, day_item in enumerate(new_day):
                        index_num = int(
                            input("choose the index of activity you want to delete: ")
                        )
                        # index_num -= 1
                        del new_day[index_num]
                        print("REMOVED !!!")
                        break

    # Write the updated JSON data back to the file
    with open(fileName, "w") as file:
        json.dump(data, file, indent=2)

    print("Data deleted successfully.")
