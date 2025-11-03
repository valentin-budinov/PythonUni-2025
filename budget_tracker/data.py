import json

FILE_PATH = "expenses.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Corrupted data file. Starting fresh.")
        return []

def save_data(expenses):
    with open(FILE_PATH, "w") as json_file:
        json.dump(expenses, json_file, indent=4)