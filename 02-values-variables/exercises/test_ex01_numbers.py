from __future__ import annotations

import pytest
from ex01_numbers import apply_discount, minutes_to_hours_minutes, power_area


def test_minutes_to_hours_minutes_typical() -> None:
    assert minutes_to_hours_minutes(125) == (2, 5)


def test_minutes_to_hours_minutes_under_an_hour() -> None:
    assert minutes_to_hours_minutes(59) == (0, 59)


def test_minutes_to_hours_minutes_exact_hour() -> None:
    assert minutes_to_hours_minutes(180) == (3, 0)


def test_minutes_to_hours_minutes_zero() -> None:
    assert minutes_to_hours_minutes(0) == (0, 0)


def test_apply_discount_twenty_percent() -> None:
    assert apply_discount(50.0, 20) == pytest.approx(40.0)


def test_apply_discount_rounds_to_two_decimals() -> None:
    assert apply_discount(19.99, 10) == pytest.approx(17.99)


def test_apply_discount_zero_percent() -> None:
    assert apply_discount(9.5, 0) == pytest.approx(9.5)


def test_power_area_radius_two() -> None:
    assert power_area(2) == pytest.approx(12.57)


def test_power_area_radius_one() -> None:
    assert power_area(1) == pytest.approx(3.14)
