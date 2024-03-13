import json
import re
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


def edit_activity_data(fileName):
    # Load the JSON data from the file
    with open(fileName, "r") as file:
        data = json.load(file)

    # Prompt the user for module name and day name
    topic_name = input("Enter the Topic name (e.g., devops): ")
    module_name = input("Enter the Module name (e.g., linux): ")
    day_name = input("Enter the day name (e.g., day1): ")

    # Define regular expressions for the user input module and day
    module_regex = re.compile(rf"\b{module_name}\b", re.IGNORECASE)
    day_regex = re.compile(rf"\b{day_name}\b", re.IGNORECASE)

    # Search for the specified module and day
    for module in data[topic_name]:
        if any(module_regex.match(key) for key in module):
            # print("module: ", module)
            for day in module[module_name]:
                if any(day_regex.match(key) for key in day):
                    # print("day: ", day)
                    new_day = day[day_name]
                    for index, day_item in enumerate(new_day):
                        print(f"index: {index}, day_item: {day_item}")
                    for index, day_item in enumerate(new_day):
                        index_num = int(
                            input("choose the index of activity you want to udpate: ")
                        )
                        del new_day[index_num]
                        break
                    # add item after deleted it
                    new_item = input("Enter the new item: ")
                    day[day_name].append(new_item)

    # Write the updated JSON data back to the file
    with open(fileName, "w") as file:
        json.dump(data, file, indent=2)

    print("Data added successfully.")
