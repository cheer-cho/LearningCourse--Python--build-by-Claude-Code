import pytest

pytest.importorskip("fastapi")
pytest.importorskip("pydantic")
pytest.importorskip("sqlalchemy")

from checkpoint_14 import app, reset_catalog
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(autouse=True)
def _clean_state():
    reset_catalog()
    yield


def test_list_products_starts_empty():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product_returns_201_with_id():
    response = client.post("/products", json={"name": "Widget", "price": 9.99})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "Widget"
    assert body["price"] == 9.99


def test_create_product_rejects_non_positive_price_with_422():
    response = client.post("/products", json={"name": "Widget", "price": 0})
    assert response.status_code == 422


def test_create_duplicate_name_returns_409():
    client.post("/products", json={"name": "Widget", "price": 9.99})
    response = client.post("/products", json={"name": "Widget", "price": 5.0})
    assert response.status_code == 409


def test_created_product_shows_up_in_list():
    client.post("/products", json={"name": "Widget", "price": 9.99})
    client.post("/products", json={"name": "Gadget", "price": 4.5})
    response = client.get("/products")
    names = {p["name"] for p in response.json()}
    assert names == {"Widget", "Gadget"}


def test_catalog_resets_between_tests():
    # If reset_catalog() (via the autouse fixture) didn't work, this would
    # see the "Widget" created by an earlier test.
    response = client.get("/products")
    assert response.json() == []
