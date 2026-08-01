# Smart Expense Tracker API

A RESTful API built with **FastAPI** to manage personal expenses.

This application allows users to add, view, filter, summarize, and delete expenses. Data is stored in a local JSON file, so no database setup is required.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive API documentation using Swagger UI
- Unit tests using Pytest

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pytest

---

## Project Structure

```
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── storage.py
│   └── expenses.json
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_create.py
    ├── test_get.py
    ├── test_summary.py
    └── test_delete.py
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd smart-expense-tracker
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
uvicorn src.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Run Tests

```bash
pytest -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/summary` | Calculate total expenses |
| GET | `/expenses/summary?category=Food` | Calculate total by category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Sample Expense

```json
{
  "title": "Groceries",
  "amount": 500,
  "category": "Food",
  "date": "2026-08-01"
}
```

---

## Testing

The project includes unit tests for:

- Expense creation
- Viewing expenses
- Category filtering
- Expense summary
- Expense deletion

Run all tests:

```bash
pytest -v
```

---

## Author

Vaishnavi Patole