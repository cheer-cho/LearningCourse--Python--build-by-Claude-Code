# Scenario: parse a batch of orders (each with nested line items) out of
# raw JSON text. Concepts: nested BaseModels, list[Model], TypeAdapter,
# model_validate_json, model_dump roundtrip.
# Run: uv run pytest 14-frameworks-libraries -k ex02

from __future__ import annotations

from pydantic import BaseModel, Field


class Item(BaseModel):
    """One line item on an order. `price` and `quantity` must be positive."""

    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class Order(BaseModel):
    """An order: an id plus a list of `Item`s."""

    id: int
    items: list[Item]

    @property
    def total(self) -> float:
        """Sum of `price * quantity` across every item on this order."""
        return sum(item.price * item.quantity for item in self.items)


def load_orders(json_text: str) -> list[Order]:
    """Parse a JSON array of orders into a list of `Order`.

    Use `TypeAdapter(list[Order]).validate_json(json_text)` — this
    validates a whole list in one call, which is the pattern to reach
    for whenever the thing you're parsing is a list rather than a single
    model. Raises `pydantic.ValidationError` on bad data.

    load_orders('[{"id": 1, "items": [{"name": "Pen", "price": 1.5, "quantity": 2}]}]')
        -> [Order(id=1, items=[Item(name="Pen", price=1.5, quantity=2)])]
    """
    raise NotImplementedError
