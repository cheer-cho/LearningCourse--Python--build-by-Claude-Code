"""Reference solution for ex06_conversions. See exercises/ex06_conversions.py."""

from __future__ import annotations


def parse_price(text: str) -> float:
    return float(text.strip().removeprefix("$"))


def age_next_year(age_text: str) -> int:
    return int(age_text) + 1
