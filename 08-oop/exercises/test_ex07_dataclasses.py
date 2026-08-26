import dataclasses

import pytest
from ex07_dataclasses import Point, Task


def test_task_stores_title():
    assert Task("Buy milk").title == "Buy milk"


def test_task_done_defaults_to_false():
    assert Task("Buy milk").done is False


def test_task_tags_default_to_empty_list():
    assert Task("Buy milk").tags == []


def test_task_tags_are_independent_per_instance():
    a = Task("Buy milk")
    b = Task("Walk dog")
    a.tags.append("errand")
    assert b.tags == []


def test_task_generated_eq_compares_by_value():
    assert Task("Buy milk") == Task("Buy milk")
    assert Task("Buy milk") != Task("Walk dog")


def test_task_can_override_done_and_tags():
    task = Task("Buy milk", True, ["errand"])
    assert task.done is True
    assert task.tags == ["errand"]


def test_point_stores_x_and_y():
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_point_distance_to_3_4_5_triangle():
    assert Point(0, 0).distance_to(Point(3, 4)) == pytest.approx(5.0)


def test_point_distance_to_self_is_zero():
    p = Point(1, 1)
    assert p.distance_to(p) == 0


def test_point_generated_eq_compares_by_value():
    assert Point(1, 1) == Point(1, 1)
    assert Point(1, 1) != Point(2, 2)


def test_point_is_frozen():
    p = Point(1, 2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 9
