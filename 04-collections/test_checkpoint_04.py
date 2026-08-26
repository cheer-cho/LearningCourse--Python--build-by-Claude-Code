import pytest
from checkpoint_04 import add_score, averages, class_stats, honor_roll


def test_add_score_creates_list_on_first_score():
    book = {}
    add_score(book, "Ada", 90)
    assert book == {"Ada": [90]}


def test_add_score_appends_to_existing_list():
    book = {"Ada": [90]}
    add_score(book, "Ada", 85)
    assert book == {"Ada": [90, 85]}


def test_add_score_keeps_students_independent():
    book = {}
    add_score(book, "Ada", 90)
    add_score(book, "Bo", 70)
    assert book == {"Ada": [90], "Bo": [70]}


def test_averages_typical():
    book = {"Ada": [90, 80], "Bo": [70]}
    assert averages(book) == {"Ada": 85.0, "Bo": 70.0}


def test_averages_does_not_mutate_book():
    book = {"Ada": [90, 80], "Bo": [70]}
    averages(book)
    assert book == {"Ada": [90, 80], "Bo": [70]}


def test_averages_returns_a_different_object_than_book():
    book = {"Ada": [90, 80]}
    result = averages(book)
    assert result is not book


def test_honor_roll_filters_and_sorts_alphabetically():
    book = {"Ada": [95, 91], "Bo": [60], "Cy": [92]}
    assert honor_roll(book, 90) == ["Ada", "Cy"]


def test_honor_roll_empty_when_nobody_qualifies():
    book = {"Ada": [50]}
    assert honor_roll(book, 90) == []


def test_honor_roll_includes_exact_threshold():
    book = {"Ada": [90, 90]}
    assert honor_roll(book, 90) == ["Ada"]


def test_class_stats_typical():
    book = {"Ada": [100], "Bo": [50, 50]}
    count, best_student, overall_avg = class_stats(book)
    assert count == 2
    assert best_student == "Ada"
    assert overall_avg == pytest.approx(200 / 3)


def test_class_stats_single_student():
    book = {"Ada": [80, 90, 100]}
    assert class_stats(book) == (1, "Ada", pytest.approx(90.0))
