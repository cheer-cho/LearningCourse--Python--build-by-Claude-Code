# Scenario: a mini movie catalogue and 2D points for a plotting tool.
# Unlike the other exercises here, you DEFINE two new types yourself
# (`Movie`, `Point`) — the functions below already work and just need
# annotations added, but they only type-check once the two classes above
# them have the right fields. Concepts: `TypedDict` (required + optional
# keys via `NotRequired`), `NamedTuple`.
# Run: uv run pytest 10-typing -k ex04

from typing import NamedTuple, NotRequired, TypedDict


class Movie(TypedDict):
    """title/year are required; rating is NotRequired."""

    title: str
    year: int
    rating: NotRequired[float]


class Point(NamedTuple):
    """A 2D point."""

    x: float
    y: float


def new_movie(title: str, year: int) -> Movie:
    """Build a Movie from a title and year, no rating yet.

    new_movie("Dune", 2021) -> {"title": "Dune", "year": 2021}
    """
    return {"title": title, "year": year}


def movie_summary(movie: Movie) -> str:
    """Include the rating only if the movie has one.

    movie_summary({"title": "Dune", "year": 2021}) -> "Dune (2021)"
    movie_summary({"title": "Dune", "year": 2021, "rating": 8.5})
        -> "Dune (2021) - 8.5/10"
    """
    rating = movie.get("rating")
    if rating is None:
        return f"{movie['title']} ({movie['year']})"
    return f"{movie['title']} ({movie['year']}) - {rating}/10"


def midpoint(p1: Point, p2: Point) -> Point:
    """Return the point halfway between `p1` and `p2`.

    midpoint(Point(0, 0), Point(4, 2)) -> Point(x=2.0, y=1.0)
    """
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def describe_point(point: Point) -> str:
    """Format `point` as "(x, y)".

    describe_point(Point(1, 2)) -> "(1, 2)"
    """
    return f"({point.x}, {point.y})"
