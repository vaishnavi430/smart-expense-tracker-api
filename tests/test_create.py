from tests.conftest import client


def test_create_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Groceries",
            "amount": 500,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Groceries"
    assert data["amount"] == 500
    assert data["category"] == "Food"