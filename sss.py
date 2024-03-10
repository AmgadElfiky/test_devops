my_array = [1, 2, 3, 4, 5]

# Iterate over items in the array and delete a specific item
for index, item in enumerate(my_array):
    if index == 2:  # Change 2 to the index you want to delete
        print(f"Item at index {index}: {item} will be deleted.")
        del my_array[index]
        break  # Exit the loop after deleting the item

# Print the updated array
print("Array after deletion:", my_array)
