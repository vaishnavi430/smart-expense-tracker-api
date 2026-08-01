import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    """Load all expenses from JSON file."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save all expenses to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses):
    """Generate the next expense ID."""
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1