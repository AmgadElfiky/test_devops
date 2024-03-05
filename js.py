import json
import addData as add


def build_json_structure():
    topics = []
    ch = int(input("enter number of topics: "))
    number_of_module = int(input("enter number of modules: "))

    while ch > 0:
        topic_name = input("Enter topic name : ")

        modules = []
        while number_of_module > 0:
            module_name = input("Enter module name for {}: ".format(topic_name))

            num_days = int(input("Enter number of days for {}: ".format(module_name)))

            add.getData(modules, num_days, module_name)
            number_of_module -= 1

        topic = {topic_name: modules}
        topics.append(topic)
        ch -= 1

    return {"topics name": topics}


def append_in_file(fileName, data):
    with open(fileName, 'r') as file:
        existing_data = json.load(file)
    return True

def main():
    study_data = build_json_structure()
    with open("study_data.json", "w+") as json_file:
        json.dump(study_data, json_file, indent=2)
    print("JSON file created successfully.")


if __name__ == "__main__":
    main()
