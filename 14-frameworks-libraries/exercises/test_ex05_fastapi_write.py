import pytest

pytest.importorskip("fastapi")

from ex05_fastapi_write import app, reset_items
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def _clean_state():
    reset_items()
    yield
    reset_items()


def test_create_item_returns_201_with_assigned_id():
    response = client.post("/items", json={"name": "Widget", "price": 9.99})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "Widget"
    assert body["price"] == 9.99


def test_create_item_rejects_non_positive_price_with_422():
    response = client.post("/items", json={"name": "Widget", "price": 0})
    assert response.status_code == 422


def test_create_duplicate_name_returns_409():
    client.post("/items", json={"name": "Widget", "price": 9.99})
    response = client.post("/items", json={"name": "Widget", "price": 5.0})
    assert response.status_code == 409


def test_delete_existing_item_returns_204():
    created = client.post("/items", json={"name": "Widget", "price": 9.99}).json()
    response = client.delete(f"/items/{created['id']}")
    assert response.status_code == 204


def test_delete_missing_item_returns_404():
    response = client.delete("/items/999")
    assert response.status_code == 404


def test_deleted_item_is_really_gone():
    created = client.post("/items", json={"name": "Widget", "price": 9.99}).json()
    client.delete(f"/items/{created['id']}")
    response = client.delete(f"/items/{created['id']}")
    assert response.status_code == 404
