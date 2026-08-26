# Scenario: the write side of the items API — create and delete, backed
# by a module-level dict standing in for a database. Concepts: pydantic
# request body, response_model, status codes (201/204/404/409), test
# isolation via a reset helper.
# Run: uv run pytest 14-frameworks-libraries -k ex05

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field


class ItemIn(BaseModel):
    """Request body for creating an item."""

    name: str
    price: float = Field(gt=0)


class ItemOut(BaseModel):
    """Response body for an item, including its assigned id."""

    id: int
    name: str
    price: float


app = FastAPI()

_items: dict[int, ItemOut] = {}
_next_id = 1


def reset_items() -> None:
    """Test-only helper: clear all items and reset the id counter to 1.
    Call this at the start of every test that touches `/items` so tests
    don't leak state into each other.
    """
    global _next_id
    _items.clear()
    _next_id = 1


@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemIn) -> ItemOut:
    """Create an item.

    409 if an item with this name already exists (check `_items`
    before inserting). On success, assign the next id, store it, and
    return it as an `ItemOut`.
    """
    raise NotImplementedError


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    """Delete an item by id. 404 if no item has that id."""
    raise NotImplementedError
