import pytest

pytest.importorskip("pydantic")

from ex02_pydantic_nested import Item, Order, load_orders
from pydantic import ValidationError

SAMPLE_JSON = """
[
    {"id": 1, "items": [{"name": "Pen", "price": 1.5, "quantity": 2}]},
    {"id": 2, "items": [
        {"name": "Mug", "price": 8.0, "quantity": 1},
        {"name": "Plate", "price": 4.0, "quantity": 3}
    ]}
]
"""


def test_load_orders_returns_order_objects():
    orders = load_orders(SAMPLE_JSON)
    assert orders == [
        Order(id=1, items=[Item(name="Pen", price=1.5, quantity=2)]),
        Order(
            id=2,
            items=[
                Item(name="Mug", price=8.0, quantity=1),
                Item(name="Plate", price=4.0, quantity=3),
            ],
        ),
    ]


def test_order_total_sums_price_times_quantity():
    orders = load_orders(SAMPLE_JSON)
    assert orders[0].total == pytest.approx(3.0)
    assert orders[1].total == pytest.approx(20.0)


def test_load_orders_rejects_non_positive_price():
    bad_json = '[{"id": 1, "items": [{"name": "Pen", "price": 0, "quantity": 1}]}]'
    with pytest.raises(ValidationError):
        load_orders(bad_json)


def test_model_dump_roundtrip():
    orders = load_orders(SAMPLE_JSON)
    dumped = orders[0].model_dump()
    assert Order.model_validate(dumped) == orders[0]
