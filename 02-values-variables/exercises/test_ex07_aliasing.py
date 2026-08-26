from __future__ import annotations

from ex07_aliasing import rebind_vs_alias, shared_append, two_names_one_list


def test_shared_append_mutates_through_the_alias() -> None:
    assert shared_append() == [1, 2, 3]


def test_two_names_one_list_sees_the_mutation() -> None:
    assert two_names_one_list() == [1, 2, 3, 4]


def test_rebind_vs_alias_leaves_original_untouched() -> None:
    a, b = rebind_vs_alias()
    assert a == [1, 2]
    assert b == [1, 2, 3]
