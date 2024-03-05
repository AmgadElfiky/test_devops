# import json
# import addData as add


# def build_json_structure():
#     topics = []
#     ch = int(input("enter number of topics: "))
#     number_of_module = int(input("enter number of modules: "))

#     while ch > 0:
#         topic_name = input("Enter topic name : ")

#         modules = []
#         while number_of_module > 0:
#             module_name = input("Enter module name for {}: ".format(topic_name))

#             num_days = int(input("Enter number of days for {}: ".format(module_name)))

#             add.getData(modules, num_days, module_name)
#             number_of_module -= 1

#         topic = {topic_name: modules}
#         topics.append(topic)
#         ch -= 1

#     return {"topics name": topics}


# def append_in_file(fileName, data):
#     try:
#         with open(fileName, "r") as file:
#             existing_data = json.dump(file)
#     except FileNotFoundError:
#         existing_data = []

#     existing_data.append(data)

#     with open(fileName, "w") as file:
#         json.dump(existing_data, file, indent=2)


# def main():
#     study_data = build_json_structure()
#     with open("study_data.json", "w+") as json_file:
#         # json.dump(study_data, json_file, indent=2)
#         append_in_file("study_data.json", study_data)
#     print("JSON file created successfully.")


# if __name__ == "__main__":
#     main()

import json

def append_to_json_file(filename, new_data):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Append the new data to the existing data
    existing_data.append(new_data)

    # Write the combined data back to the file
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=2)

def build_json_structure():
    topics = []
    ch = int(input("Enter number of topics: "))

    while ch > 0:
        topic_name = input("Enter topic name: ")

        modules = []
        number_of_module = int(input("Enter number of modules for {}: ".format(topic_name)))
        
        while number_of_module > 0:
            module_name = input("Enter module name for {}: ".format(topic_name))

            num_days = int(input("Enter number of days for {}: ".format(module_name)))
            days = []

            for day in range(1, num_days + 1):
                activities = []
                num_activities = int(input("Enter number of activities for Day {} of {}: ".format(day, module_name)))
                for activity in range(1, num_activities + 1):
                    activity_name = input("Enter name of activity {} for Day {} of {}: ".format(activity, day, module_name))
                    activities.append(activity_name)
                
                day_data = {"day{}".format(day): activities}
                days.append(day_data)

            module = {module_name: days}
            modules.append(module)
            number_of_module -= 1

        topic = {topic_name: modules}
        topics.append(topic)
        ch -= 1

    return {"topics": topics}

def main():
    study_data = build_json_structure()
    append_to_json_file("study_data.json", study_data)
    print("JSON data appended successfully.")

if __name__ == "__main__":
    main()
