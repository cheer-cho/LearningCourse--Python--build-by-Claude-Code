"""Reference solution for ex05_none_defaults. See exercises/ex05_none_defaults.py."""

from __future__ import annotations


def label_or_default(label: str | None) -> str:
    return label if label is not None else "(none)"


def first_non_none(a: object | None, b: object) -> object:
    return a if a is not None else b
