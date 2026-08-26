import math

from ex01_import_forms import alphabet_position, circle_area, middle_value


def test_circle_area_radius_one():
    assert circle_area(1) == math.pi


def test_circle_area_radius_zero():
    assert circle_area(0) == 0.0


def test_circle_area_radius_two():
    assert circle_area(2) == math.pi * 4


def test_middle_value_odd_count():
    assert middle_value([3, 1, 2]) == 2


def test_middle_value_even_count():
    assert middle_value([1, 2, 3, 4]) == 2.5


def test_middle_value_single_item():
    assert middle_value([7]) == 7


def test_alphabet_position_a_is_one():
    assert alphabet_position("a") == 1


def test_alphabet_position_m_is_thirteen():
    assert alphabet_position("m") == 13


def test_alphabet_position_z_is_twenty_six():
    assert alphabet_position("z") == 26
