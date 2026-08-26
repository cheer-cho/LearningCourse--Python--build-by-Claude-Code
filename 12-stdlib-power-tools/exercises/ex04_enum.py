# Scenario: modeling a ticket's lifecycle with a fixed set of named
# states instead of magic strings. Concepts: Enum, auto, name lookup,
# match/case on enum members.
# Run: uv run pytest 12-stdlib-power-tools -k ex04

from enum import Enum, auto


class Status(Enum):
    """A ticket's lifecycle state, in pipeline order."""

    PENDING = auto()
    ACTIVE = auto()
    CLOSED = auto()


def from_label(text: str) -> Status:
    """Look up a Status by name, case-insensitively. Raises ValueError
    (not KeyError) for a label that doesn't match any member.

    from_label("active") -> Status.ACTIVE
    from_label("PENDING") -> Status.PENDING
    from_label("bogus") -> raises ValueError
    """
    raise NotImplementedError


def next_status(s: Status) -> Status:
    """Return the next status in the pipeline: PENDING -> ACTIVE ->
    CLOSED. CLOSED is terminal and maps to itself. Implement with
    match/case on `s`.

    next_status(Status.PENDING) -> Status.ACTIVE
    next_status(Status.CLOSED) -> Status.CLOSED
    """
    raise NotImplementedError


def is_terminal(s: Status) -> bool:
    """Return True if `s` has no further transitions (CLOSED), else
    False.

    is_terminal(Status.CLOSED) -> True
    is_terminal(Status.ACTIVE) -> False
    """
    raise NotImplementedError
