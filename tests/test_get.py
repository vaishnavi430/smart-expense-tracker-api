from tests.conftest import client


def test_get_all_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_by_category():
    response = client.get("/expenses?category=Food")

    assert response.status_code == 200

    for expense in response.json():
        assert expense["category"] == "Food"