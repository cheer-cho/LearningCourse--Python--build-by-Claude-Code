"""Reference solution for ex01_numbers. See exercises/ex01_numbers.py."""

from __future__ import annotations

import math


def minutes_to_hours_minutes(total_minutes: int) -> tuple[int, int]:
    return total_minutes // 60, total_minutes % 60


def apply_discount(price: float, percent_off: float) -> float:
    return round(price * (1 - percent_off / 100), 2)


def power_area(radius: float) -> float:
    return round(math.pi * radius**2, 2)
