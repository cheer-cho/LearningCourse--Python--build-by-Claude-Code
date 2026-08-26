import subprocess
import sys
import typing
from collections.abc import Iterable
from pathlib import Path

from checkpoint_10 import (
    Cart,
    HasTotal,
    Order,
    cheapest,
    filter_expensive,
    first_or_none,
    format_order,
    group_by_item,
    order_total,
    sum_totals,
    total_revenue,
)

THIS_FILE = Path(__file__).resolve().parent / "checkpoint_10.py"

MUG = {"id": "1", "item": "Mug", "qty": 2, "price": 5.0}
PEN = {"id": "2", "item": "Pen", "qty": 1, "price": 1.0}
MUG2 = {"id": "3", "item": "Mug", "qty": 1, "price": 5.0}


def test_order_has_required_keys():
    assert Order.__required_keys__ == frozenset({"id", "item", "qty", "price"})
    hints = typing.get_type_hints(Order)
    assert hints.get("id") is str
    assert hints.get("item") is str
    assert hints.get("qty") is int
    assert hints.get("price") is float


def test_has_total_declares_total_method():
    assert hasattr(HasTotal, "total")
    hints = typing.get_type_hints(HasTotal.total)
    assert hints.get("return") is float


def test_order_total_behaves_correctly():
    assert order_total(MUG) == 10.0


def test_order_total_is_annotated():
    hints = typing.get_type_hints(order_total)
    assert hints.get("order") is Order
    assert hints.get("return") is float


def test_format_order_behaves_correctly():
    assert format_order(MUG) == "2x Mug ($10.00)"


def test_format_order_is_annotated():
    hints = typing.get_type_hints(format_order)
    assert hints.get("order") is Order
    assert hints.get("return") is str


def test_filter_expensive_behaves_correctly():
    assert filter_expensive([MUG, PEN], 5.0) == [MUG]


def test_filter_expensive_is_annotated():
    hints = typing.get_type_hints(filter_expensive)
    assert hints.get("orders") == list[Order]
    assert hints.get("threshold") is float
    assert hints.get("return") == list[Order]


def test_group_by_item_behaves_correctly():
    assert group_by_item([MUG, PEN, MUG2]) == {"Mug": [MUG, MUG2], "Pen": [PEN]}


def test_group_by_item_is_annotated():
    hints = typing.get_type_hints(group_by_item)
    assert hints.get("orders") == list[Order]
    assert hints.get("return") == dict[str, list[Order]]


def test_first_or_none_behaves_correctly():
    assert first_or_none([1, 2, 3]) == 1
    assert first_or_none([]) is None


def test_first_or_none_is_generic():
    """`return` should be `T | None` for the SAME T used in `items: list[T]` —
    not `object | None` or some other type-safety-losing shortcut.
    """
    hints = typing.get_type_hints(first_or_none)
    return_args = typing.get_args(hints.get("return"))
    assert type(None) in return_args
    (type_var,) = [arg for arg in return_args if arg is not type(None)]
    assert hints.get("items") == list[type_var]


def test_cheapest_behaves_correctly():
    assert cheapest([MUG, PEN]) == PEN
    assert cheapest([]) is None


def test_cheapest_is_annotated():
    hints = typing.get_type_hints(cheapest)
    assert hints.get("orders") == list[Order]
    assert hints.get("return") == Order | None


def test_total_revenue_behaves_correctly():
    assert total_revenue([MUG, PEN]) == 11.0
    assert total_revenue([]) == 0.0


def test_total_revenue_is_annotated():
    hints = typing.get_type_hints(total_revenue)
    assert hints.get("orders") == list[Order]
    assert hints.get("return") is float


def test_cart_total_behaves_correctly():
    assert Cart([MUG, PEN]).total() == 11.0


def test_cart_is_annotated():
    init_hints = typing.get_type_hints(Cart.__init__)
    assert init_hints.get("orders") == list[Order]
    assert init_hints.get("return") is type(None)
    total_hints = typing.get_type_hints(Cart.total)
    assert total_hints.get("return") is float


def test_sum_totals_behaves_correctly():
    assert sum_totals([Cart([MUG]), Cart([PEN])]) == 11.0


def test_sum_totals_is_annotated():
    hints = typing.get_type_hints(sum_totals)
    assert hints.get("items") == Iterable[HasTotal]
    assert hints.get("return") is float


def test_checkpoint_10_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
