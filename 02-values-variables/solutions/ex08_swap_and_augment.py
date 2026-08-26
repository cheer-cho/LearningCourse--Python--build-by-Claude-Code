"""Reference solution for ex08_swap_and_augment. See exercises/ex08_swap_and_augment.py."""

from __future__ import annotations


def swap(a: object, b: object) -> tuple[object, object]:
    return b, a


def apply_raise_and_bonus(salary: float, raise_amount: float, bonus: float) -> float:
    salary += raise_amount
    salary += bonus
    return salary


def evaluate() -> int:
    return (2 + 3) * 4
