from tests.conftest import client


def test_delete_existing_expense():
    create_response = client.post(
        "/expenses",
        json={
            "title": "Delete Test",
            "amount": 100,
            "category": "Testing",
            "date": "2026-08-01"
        }
    )

    expense_id = create_response.json()["id"]

    response = client.delete(f"/expenses/{expense_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully."


def test_delete_invalid_expense():
    response = client.delete("/expenses/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found."