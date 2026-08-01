from typing import Optional,List
from fastapi import APIRouter
from src.models import ExpenseCreate
from src.storage import load_expenses, save_expenses, get_next_id

router = APIRouter()


@router.post(
    "/expenses",
    status_code=201
)
def add_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = {
        "id": get_next_id(expenses),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense

@router.get(
    "/expenses"
)
def get_expenses(category: Optional[str] = None):
    """
    Retrieve all expenses or filter them by category.
    """

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses