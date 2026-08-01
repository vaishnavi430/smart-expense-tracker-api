from tests.conftest import client


def test_summary():
    response = client.get("/expenses/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data


def test_summary_by_category():
    response = client.get("/expenses/summary?category=Food")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert data["category"] == "Food"