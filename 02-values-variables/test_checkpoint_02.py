from __future__ import annotations

import pytest
from checkpoint_02 import format_receipt, parse_money

ITEMS = [
    ("Widget", "$3.50", 2),
    ("Gadget", "$12.00", 1),
    ("Gizmo", "$0.99", 5),
]

EXPECTED_LINES = [
    "=== Corner Store ===",
    "Widget     x2   @ $  3.50 = $   7.00",
    "Gadget     x1   @ $ 12.00 = $  12.00",
    "Gizmo      x5   @ $  0.99 = $   4.95",
    "-" * 34,
    "Subtotal                $   23.95",
    "Tax (7%)                $    1.68",
    "Total                   $   25.63",
]


def test_parse_money_with_dollar_sign() -> None:
    assert parse_money("$12.30") == pytest.approx(12.3)


def test_parse_money_with_whitespace() -> None:
    assert parse_money(" $3.50 ") == pytest.approx(3.5)


def test_parse_money_without_dollar_sign() -> None:
    assert parse_money("9.99") == pytest.approx(9.99)


def test_format_receipt_exact_lines() -> None:
    receipt = format_receipt("Corner Store", ITEMS)
    assert receipt.split("\n") == EXPECTED_LINES


def test_format_receipt_full_text() -> None:
    receipt = format_receipt("Corner Store", ITEMS)
    assert receipt == "\n".join(EXPECTED_LINES)


def test_format_receipt_different_store_and_items() -> None:
    items = [
        ("Pen", "$1.00", 4),
        ("Notebook", "$5.50", 2),
        ("Eraser", "$0.50", 3),
    ]
    receipt = format_receipt("Stationery Shop", items)
    lines = receipt.split("\n")
    assert lines[0] == "=== Stationery Shop ==="
    assert lines[1] == "Pen        x4   @ $  1.00 = $   4.00"
    subtotal = 4.00 + 11.00 + 1.50
    assert f"${subtotal:>8.2f}" in lines[5]
