# Scenario: a tiny geometry toolkit, and the LEARNING TARGET behind
# `mod07_geo/__init__.py`. Concepts: `__all__` as a package's explicit
# public-API contract, and a leading underscore marking a name as
# module-private (never meant to be imported from outside).
# Run: uv run pytest 07-modules-organization -k ex04

__all__ = ["distance", "midpoint"]


def _helper(a, b):
    """Return `a - b`. Private: this name isn't in `__all__` above, so
    `mod07_geo` (the package built on top of this file) never
    re-exports it — even though it's still directly importable from
    THIS module for testing.

    _helper(5, 2) -> 3
    """
    raise NotImplementedError


def distance(p1, p2):
    """Return the straight-line distance between points `p1` and `p2`
    (each an `(x, y)` tuple).

    distance((0, 0), (3, 4)) -> 5.0
    """
    raise NotImplementedError


def midpoint(p1, p2):
    """Return the midpoint of `p1` and `p2` (each an `(x, y)` tuple) as
    an `(x, y)` tuple.

    midpoint((0, 0), (4, 2)) -> (2.0, 1.0)
    """
    raise NotImplementedError
