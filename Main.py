from append import append_to_json_file
from addData import enterData
import json


def build_module_data(topic_name):
    modules = []
    while True:
        try:
            number_of_module = int(
                input("Enter number of modules for {}: ".format(topic_name))
            )
            if number_of_module < 0:
                raise ValueError("Number of days cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    while number_of_module > 0:
        module_name = input("Enter module name for {}: ".format(topic_name))

        while True:
            try:
                num_days = int(
                    input("Enter number of days for {}: ".format(module_name))
                )
                if num_days < 0:
                    raise ValueError("Number of days cannot be negative.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid positive integer.")

        enterData(modules, num_days, module_name)
        number_of_module -= 1

    return modules


# def deleteData(item_data):
#     with open("study_data.json", "r") as file:
#         data = json.load(file)
#     # print(data)
#     for item in data:
#         for details in item:
#             print("item : ", details)
#             if item_data in details:
#                 data.pop(item_data)
#                 with open("study_data.json", "w") as delete:
#                     json.dump(data, delete, indent=2)
#                     print("Deleted Successfully")


def main():

    topic_name = input("Enter topic name: ")
    module_data = build_module_data(topic_name)
    append_to_json_file("study_data.json", topic_name, module_data)
    print("JSON data appended successfully.")


if __name__ == "__main__":
    main()
