from append import append_to_json_file
from addData import enterData


def build_module_data(topic_name):
    modules = []
    number_of_module = int(input("Enter number of modules for {}: ".format(topic_name)))

    while number_of_module > 0:
        module_name = input("Enter module name for {}: ".format(topic_name))

        num_days = int(input("Enter number of days for {}: ".format(module_name)))
        enterData(modules, num_days, module_name)
        number_of_module -= 1

    return modules


def main():
    topic_name = input("Enter topic name: ")
    module_data = build_module_data(topic_name)
    append_to_json_file("study_data.json", topic_name, module_data)
    print("JSON data appended successfully.")


if __name__ == "__main__":
    main()
