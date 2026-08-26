from dataclasses import dataclass, replace


@dataclass
class Order:
    id: int
    item: str
    quantity: int
    unit_price: float
    paid: bool = False


def make_order(**overrides: object) -> Order:
    defaults = Order(id=1, item="widget", quantity=1, unit_price=9.99, paid=False)
    return replace(defaults, **overrides)


def make_paid_order(**overrides: object) -> Order:
    overrides = {**overrides, "paid": True}
    return make_order(**overrides)


def describe_failure(expected: object, actual: object) -> str:
    return f"expected {expected!r}, got {actual!r}"
