import re
import json


def add_activity_data(fileName):
    # Load the JSON data from the file
    with open(fileName, "r") as file:
        data = json.load(file)

    # Prompt the user for category name and day name
    topic_name = input("Enter the Topic name (e.g., devops): ")
    category_name = input("Enter the Module name (e.g., linux): ")
    day_name = input("Enter the day name (e.g., day1): ")

    # Define regular expressions for the user input category and day
    category_regex = re.compile(rf"\b{category_name}\b", re.IGNORECASE)
    day_regex = re.compile(rf"\b{day_name}\b", re.IGNORECASE)

    # Search for the specified category and day
    for category in data[topic_name]:
        if any(category_regex.match(key) for key in category):
            for day in category[category_name]:
                if any(day_regex.match(key) for key in day):
                    # Prompt the user to input the data
                    new_item = input("Enter the new item: ")
                    # Add the new data to the specified day
                    day[day_name].append(new_item)

    # Write the updated JSON data back to the file
    with open(fileName, "w") as file:
        json.dump(data, file, indent=2)

    print("Data added successfully.")
