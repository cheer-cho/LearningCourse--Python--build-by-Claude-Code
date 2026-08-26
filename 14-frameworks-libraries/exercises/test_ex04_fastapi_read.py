import pytest

pytest.importorskip("fastapi")

from ex04_fastapi_read import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_item_found():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Widget"}


def test_read_item_missing_returns_404():
    response = client.get("/items/999")
    assert response.status_code == 404


def test_read_item_non_numeric_id_returns_422():
    response = client.get("/items/not-a-number")
    assert response.status_code == 422


def test_list_items_no_filter_returns_all():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_list_items_prefix_filters():
    response = client.get("/items", params={"prefix": "Widget"})
    assert response.status_code == 200
    names = {item["name"] for item in response.json()}
    assert names == {"Widget", "Widget Pro"}
