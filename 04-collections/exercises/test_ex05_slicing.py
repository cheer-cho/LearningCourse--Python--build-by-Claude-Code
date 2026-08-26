from ex05_slicing import every_other, middle, reversed_copy, rotate


def test_every_other_typical():
    assert every_other("PYTHON") == "PTO"


def test_every_other_empty_string():
    assert every_other("") == ""


def test_every_other_single_char():
    assert every_other("A") == "A"


def test_reversed_copy_typical():
    assert reversed_copy([1, 2, 3]) == [3, 2, 1]


def test_reversed_copy_does_not_mutate_input():
    items = [1, 2, 3]
    reversed_copy(items)
    assert items == [1, 2, 3]


def test_middle_typical():
    assert middle([1, 2, 3, 4, 5]) == [2, 3, 4]


def test_middle_two_items_leaves_nothing():
    assert middle([1, 2]) == []


def test_rotate_typical():
    assert rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_rotate_zero_is_unchanged():
    assert rotate([1, 2, 3], 0) == [1, 2, 3]


def test_rotate_wraps_around_with_modulo():
    assert rotate([1, 2, 3], 4) == [2, 3, 1]


def test_rotate_empty_list():
    assert rotate([], 3) == []
