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