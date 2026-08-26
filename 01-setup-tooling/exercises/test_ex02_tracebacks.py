"""Tests for ex02_tracebacks.

Run: uv run pytest 01-setup-tooling -k ex02
"""

from ex02_tracebacks import average_score, order_total, receipt_line


def test_order_total_multiplies_price_and_quantity():
    assert order_total(10, 3) == 30


def test_order_total_zero_quantity_is_zero():
    assert order_total(10, 0) == 0


def test_receipt_line_formats_name_and_count():
    assert receipt_line("apples", 3) == "apples: 3"


def test_receipt_line_count_is_stringified():
    assert receipt_line("pears", 0) == "pears: 0"


def test_average_score_of_several_scores():
    assert average_score([10, 20, 30]) == 20.0


def test_average_score_of_empty_list_is_zero():
    assert average_score([]) == 0.0
