import json
def append_to_json_file(filename, topic_name, new_module_data):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Check if the topic name already exists
    topic_found = False
    for topic in data:
        if topic_name in topic:
            # Append the new module data to the existing topic
            topic[topic_name].extend(new_module_data)
            topic_found = True
            break

    # If the topic name doesn't exist, create a new entry
    if not topic_found:
        data.append({topic_name: new_module_data})

    # Write the data back to the file
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
