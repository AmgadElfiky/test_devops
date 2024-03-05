class_name = input("Enter the name of the class: ")

# Taking the number of modules as an integer input
num_modules = int(input("Enter the number of modules: "))

# Initialize lists to store module names and days for each module
module_names = []
days_per_module = []

# Loop to gather information for each module
for i in range(num_modules):
    module_name = input(f"Enter the name of Module {i + 1}: ")
    module_names.append(module_name)

    # Taking the number of days for each module as an integer input
    days = int(input(f"Enter the number of days for Module {i + 1}: "))
    days_per_module.append(days)

# Displaying the gathered information
module_days = []
print("\nClass Information:")
print(f"Class Name: {class_name}")
print("Module Information:")
for i in range(num_modules):
    print(f"Module {i + 1}: {module_names[i]}, Days: {days_per_module[i]}")
    for j in range(days_per_module):
        module_days = input(
            f"Enter elements for list {i + 1} (comma-separated): "
        ).split(",")
        module_days = [int(x) if x.isdigit() else x for x in module_days]
        days_per_module.append(module_days)
        
print("\nClass Information:")
print(f"Class Name: {class_name}")
print("Module Information:")
for i in range(num_modules):
    print(f"Module {i + 1}: {module_names[i]}, Days: {days_per_module[i]}, module_per_day: {days_per_module}")
        


# num_lists = int(input("Enter the number of lists: "))

# # Initializing an empty list to store the lists
# list_of_lists = []

# # Loop to take input for each inner list
# for i in range(num_lists):
#     inner_list = input(f"Enter elements for list {i + 1} (comma-separated): ").split(
#         ","
#     )
#     # Converting input values to the appropriate data type (e.g., integers or strings)
#     inner_list = [int(x) if x.isdigit() else x for x in inner_list]
#     # Adding the inner list to the list of lists
#     list_of_lists.append(inner_list)

# # Displaying the resulting list of lists
# print("List of Lists:")
# print(list_of_lists)


# Creating a dictionary from the two lists
my_dict = dict(zip(module_names, days_per_module))

# Displaying the resulting dictionary
print(my_dict)
