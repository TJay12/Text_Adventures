import json
from pathlib import Path

# File folder for all JSON files
root = Path("data")

# Read JSON File (Display data info from file)
def read_json(filename):
    path = root / filename

    with path.open("r") as file:
        data = json.load(file)
        return data

# Save JSON file (Overwrite file data with new info)
def save_json(filename, data):
    path = root / filename

    with path.open("w") as file:
        json.dump(data, file, indent=4)

# Edit JSON file (Read data from file, edit data from file, then save data to file)
def edit_json(filename, action, category, item, quantity):

# Load data from json file
    data = read_json(filename)

    # action will either be add or remove (Change to boolean later)
    # If action is add
    if action == "add":
        # If dictionary has categories
        #   - Category: Key: Value
        if data[category].items():
            if item in data[category]:
                data[category][item] += quantity
            else:
                data[category][item] = quantity
        # If dictionary doesn't have categories
        #   - Key: Value
        else:
            data[item] += quantity

    # If action is remove
    elif action == "remove":
        #  If dictionary has categories
        if data[category].items():
            data[category][item] -= quantity
            if data[category][item] < 0:
                data[category][item] = 0
        #  If dictionary doesn't have categories
        else:
            data[item] -= quantity
            if data[item] < 0:
                data[item] = 0

    save_json(filename, data)




