# operations
from append import append_to_json_file
from addData import enterData
from display import display_json_data
from edit import edit_json_data
from delete import delete_json_data
# from addDayData import add_activity_data
from test import add_activity_data

# style
import pyfiglet as pyg
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer
from inquirer.themes import BlueComposure


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


def main():
    file_name = "study_data.json"
    # welcome msg
    welcome_message = pyg.figlet_format("Welcome To MindTreeED")
    print(welcome_message)

    # Choices
    while True:
        # Define the list of topics
        Options = [
            "ADD",
            "UPDATE",
            "DISPLAY",
            "DELETE",
            "EXIT",
        ]

        # Define the questions
        Choices_questions = [
            inquirer.List(
                "Choice",
                message="Choose... ",
                choices=Options,
            )
        ]

        # Prompt the user to choose a topic
        answers = inquirer.prompt(Choices_questions, theme=BlueComposure())
        selected_option = answers["Choice"]

        # list of choices
        if selected_option == "ADD":

            addOptions = [
                "ADD NEW MODULE",
                "ADD ACTIVITY IN MODULE",
            ]

            # Define the questions
            Choices_questions = [
                inquirer.List(
                    "addChoice",
                    message="Choose... ",
                    choices=addOptions,
                )
            ]

            # Prompt the user to choose a topic
            answers = inquirer.prompt(Choices_questions, theme=BlueComposure())
            selected_add_option = answers["addChoice"]

            if selected_add_option == "ADD NEW MODULE":
                topic_name = input("Enter topic name: ")
                module_data = build_module_data(topic_name)
                append_to_json_file(file_name, topic_name, module_data)
                print("JSON data appended successfully.")
            elif selected_add_option == "ADD ACTIVITY IN MODULE":
                add_activity_data(file_name)
        elif selected_option == "UPDATE":
            # welcome message
            edit_script = pyg.figlet_format("Edit Script")
            print(edit_script)
            edit_json_data(file_name)
        elif selected_option == "DISPLAY":
            # welcome message
            display_script = pyg.figlet_format("Display Script")
            print(display_script)
            display_json_data(file_name)
        elif selected_option == "DELETE":
            # welcome message
            delete_script = pyg.figlet_format("Delete Script")
            print(delete_script)
            delete_json_data(file_name)
        elif selected_option == "EXIT":
            goodbye_message = pyg.figlet_format("Thanks For Using Our System")
            print(goodbye_message)
            break
        else:
            print("Invalid action. Please choose a valid option.")
        # print("You selected: ", selected_option)


if __name__ == "__main__":
    main()
