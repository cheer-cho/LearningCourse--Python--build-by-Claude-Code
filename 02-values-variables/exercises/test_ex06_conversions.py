from __future__ import annotations

import pytest
from ex06_conversions import age_next_year, parse_price


def test_parse_price_with_dollar_sign() -> None:
    assert parse_price("$3.50") == pytest.approx(3.5)


def test_parse_price_with_surrounding_whitespace() -> None:
    assert parse_price(" $12.00 ") == pytest.approx(12.0)


def test_parse_price_without_dollar_sign() -> None:
    assert parse_price("9.99") == pytest.approx(9.99)


def test_parse_price_raises_value_error_on_garbage() -> None:
    with pytest.raises(ValueError):
        parse_price("free")


def test_age_next_year_typical() -> None:
    assert age_next_year("41") == 42


def test_age_next_year_zero() -> None:
    assert age_next_year("0") == 1


def test_age_next_year_raises_value_error_on_garbage() -> None:
    with pytest.raises(ValueError):
        age_next_year("old")
