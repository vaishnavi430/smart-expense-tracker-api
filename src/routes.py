from fastapi import APIRouter
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