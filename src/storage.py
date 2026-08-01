import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)