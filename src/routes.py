from typing import Optional
from fastapi import APIRouter, HTTPException
from src.models import ExpenseCreate
from src.storage import load_expenses, save_expenses, get_next_id

router = APIRouter()


@router.post("/expenses", status_code=201)
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


@router.get("/expenses")
def get_expenses(category: Optional[str] = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


@router.get("/expenses/summary")
def get_summary(category: Optional[str] = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    if category:
        return {
            "category": category,
            "total": total
        }

    return {
        "total": total
    }

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    expense = next(
        (expense for expense in expenses if expense["id"] == expense_id),
        None
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found."
        )

    expenses.remove(expense)
    save_expenses(expenses)

    return {
        "message": "Expense deleted successfully."
    }