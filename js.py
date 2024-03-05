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

from append import append_to_json_file
from addData import enterData


def build_json_structure():
    topics = []
    topic_number = int(input("Enter number of topics: "))

    while topic_number > 0:
        topic_name = input("Enter topic name: ")

        modules = []
        module_number = int(
            input("Enter number of modules for {}: ".format(topic_name))
        )

        while module_number > 0:
            module_name = input("Enter module name for {}: ".format(topic_name))

            num_days = int(input("Enter number of days for {}: ".format(module_name)))

            enterData(modules, num_days, module_name)
            module_number -= 1

        topic = {topic_name: modules}
        topics.append(topic)
        topic_number -= 1

    return {"topics": topics}


def main():
    study_data = build_json_structure()
    append_to_json_file("study_data.json", study_data)
    print("JSON data appended successfully.")


if __name__ == "__main__":
    main()
