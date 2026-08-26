"""Reference solution for ex07_aliasing. See exercises/ex07_aliasing.py."""

from __future__ import annotations


def shared_append() -> list[int]:
    a = [1, 2]
    b = a
    b.append(3)
    return [1, 2, 3]


def two_names_one_list() -> list[int]:
    a = [1, 2, 3]
    b = a
    a.append(4)
    assert b is a
    return [1, 2, 3, 4]


def rebind_vs_alias() -> tuple[list[int], list[int]]:
    a = [1, 2]
    b = a
    b = b + [3]
    return ([1, 2], [1, 2, 3])
