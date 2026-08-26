# Scenario: a to-do list was originally raw dicts; a graphics tool needs
# an immutable 2D point. Concepts: @dataclass, field(default_factory=...),
# @dataclass(frozen=True). (Field annotations like `title: str` are
# required syntax here — what they MEAN gets its full module (10).)
# Run: uv run pytest 08-oop -k ex07


class Task:
    """A to-do item, currently written by hand with a plain __init__.

    Rewrite this whole class as a @dataclass (add
    `from dataclasses import dataclass, field` at the top) with three
    fields:
    - title (no default)
    - done, defaulting to False
    - tags, defaulting to an empty list — use
      field(default_factory=list) so every Task gets its OWN list,
      not one shared list (the same trap as ex02's Team bug).

    Task("Buy milk").title -> "Buy milk"
    Task("Buy milk").done -> False
    Task("Buy milk").tags -> []
    Task("Buy milk") == Task("Buy milk") -> True (dataclass generates __eq__)
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError


class Point:
    """An (x, y) point, currently written by hand with a plain __init__.

    Rewrite this whole class as @dataclass(frozen=True) (needs the same
    `from dataclasses import dataclass` import as Task above) with
    fields x and y, so instances can never be mutated after creation.
    Keep the
    distance_to method (frozen only blocks assignment, not methods).

    Point(0, 0).distance_to(Point(3, 4)) -> 5.0
    Point(1, 1) == Point(1, 1) -> True (dataclass generates __eq__)
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def distance_to(self, other):
        """Return the straight-line (Euclidean) distance to `other`."""
        raise NotImplementedError
