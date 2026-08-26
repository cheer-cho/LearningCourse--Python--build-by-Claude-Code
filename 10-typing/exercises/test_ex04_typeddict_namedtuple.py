import subprocess
import sys
import typing
from pathlib import Path

from ex04_typeddict_namedtuple import (
    Movie,
    Point,
    describe_point,
    midpoint,
    movie_summary,
    new_movie,
)

THIS_FILE = Path(__file__).resolve().parent / "ex04_typeddict_namedtuple.py"


def test_movie_has_required_and_optional_keys():
    assert Movie.__required_keys__ == frozenset({"title", "year"})
    assert Movie.__optional_keys__ == frozenset({"rating"})


def test_movie_field_types():
    hints = typing.get_type_hints(Movie)
    assert hints.get("title") is str
    assert hints.get("year") is int
    assert hints.get("rating") is float


def test_point_fields():
    assert Point._fields == ("x", "y")
    hints = typing.get_type_hints(Point)
    assert hints.get("x") is float
    assert hints.get("y") is float


def test_new_movie_behaves_correctly():
    assert new_movie("Dune", 2021) == {"title": "Dune", "year": 2021}


def test_new_movie_is_annotated():
    hints = typing.get_type_hints(new_movie)
    assert hints.get("title") is str
    assert hints.get("year") is int
    assert hints.get("return") is Movie


def test_movie_summary_without_rating():
    assert movie_summary({"title": "Dune", "year": 2021}) == "Dune (2021)"


def test_movie_summary_with_rating():
    movie: Movie = {"title": "Dune", "year": 2021, "rating": 8.5}
    assert movie_summary(movie) == "Dune (2021) - 8.5/10"


def test_movie_summary_is_annotated():
    hints = typing.get_type_hints(movie_summary)
    assert hints.get("movie") is Movie
    assert hints.get("return") is str


def test_midpoint_behaves_correctly():
    assert midpoint(Point(0, 0), Point(4, 2)) == Point(2.0, 1.0)


def test_midpoint_is_annotated():
    hints = typing.get_type_hints(midpoint)
    assert hints.get("p1") is Point
    assert hints.get("p2") is Point
    assert hints.get("return") is Point


def test_describe_point_behaves_correctly():
    assert describe_point(Point(1, 2)) == "(1, 2)"


def test_describe_point_is_annotated():
    hints = typing.get_type_hints(describe_point)
    assert hints.get("point") is Point
    assert hints.get("return") is str


def test_ex04_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
