"""Reference solution for ex04_bools. See exercises/ex04_bools.py."""

from __future__ import annotations


def is_teen(age: int) -> bool:
    return 13 <= age <= 19


def same_object(a: object, b: object) -> bool:
    return a is b


def same_value(a: object, b: object) -> bool:
    return a == b
