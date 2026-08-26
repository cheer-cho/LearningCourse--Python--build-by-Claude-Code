import ex04_init_api
import mod07_geo
from mod07_geo import distance, midpoint


def test_distance_3_4_5_triangle():
    assert distance((0, 0), (3, 4)) == 5.0


def test_distance_same_point_is_zero():
    assert distance((1, 1), (1, 1)) == 0.0


def test_midpoint_typical():
    assert midpoint((0, 0), (4, 2)) == (2.0, 1.0)


def test_midpoint_negative_coordinates():
    assert midpoint((-2, -2), (2, 2)) == (0.0, 0.0)


def test_helper_still_directly_importable_from_flat_module():
    assert ex04_init_api._helper(5, 2) == 3


def test_helper_not_part_of_package_public_api():
    assert "_helper" not in mod07_geo.__all__
    assert not hasattr(mod07_geo, "_helper")
