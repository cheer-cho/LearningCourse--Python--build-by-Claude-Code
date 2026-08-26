import math

import pytest
from ex06_inheritance import Circle, Rectangle, total_area


def test_circle_area():
    assert Circle("c", 2).area == pytest.approx(12.566370614359172)


def test_rectangle_area():
    assert Rectangle("r", 3, 4).area == 12


def test_circle_stores_name_via_super_init():
    assert Circle("c", 2).name == "c"


def test_rectangle_stores_name_via_super_init():
    assert Rectangle("r", 3, 4).name == "r"


def test_describe_formats_name_and_area_two_decimals():
    assert Rectangle("r", 3, 4).describe() == "r: area=12.00"


def test_describe_uses_the_subclass_area():
    assert Circle("c", 2).describe() == "c: area=12.57"


def test_total_area_sums_across_subclasses():
    shapes = [Circle("c", 1), Rectangle("r", 2, 3)]
    expected = math.pi * 1**2 + 2 * 3
    assert total_area(shapes) == pytest.approx(expected)


def test_total_area_empty_list_is_zero():
    assert total_area([]) == 0
