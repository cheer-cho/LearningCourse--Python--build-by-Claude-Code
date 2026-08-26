# Checkpoint 08 — Mini Library System
#
# A small library catalog: items you can check out have a default loan
# period that varies by item type, members are simple data records, and
# the library itself supports len(), `in`, and a sorted catalog view.
# This combines almost everything from this module: inheritance +
# super(), a dataclass, dunders, properties, and a custom exception.
# Run: uv run pytest 08-oop -k checkpoint


class LibraryItem:
    """Base for anything the library lends out.

    loan_period is a CLASS attribute (given): the default number of
    days an item can be borrowed for. Subclasses override it.
    """

    loan_period = 21

    def __init__(self, title, year):
        """Store title and year.

        LibraryItem("Dune", 1965).title -> "Dune"
        """
        raise NotImplementedError

    def __repr__(self):
        """Return "<ClassName>(<title!r>, <year>)", e.g.

        repr(LibraryItem("Dune", 1965)) -> "LibraryItem('Dune', 1965)"

        Use type(self).__name__ so subclasses print their own class
        name automatically, without overriding __repr__ themselves.
        """
        raise NotImplementedError


class Book(LibraryItem):
    """A book: has an author, and a longer loan period than the default."""

    loan_period = 28

    def __init__(self, title, year, author):
        """Set up the shared LibraryItem state via super().__init__,
        then store author.
        """
        raise NotImplementedError


class Dvd(LibraryItem):
    """A DVD: same fields as LibraryItem, just a shorter loan period."""

    loan_period = 7


class Member:
    """A library member, currently written by hand with a plain
    __init__. Rewrite this whole class as a @dataclass (add
    `from dataclasses import dataclass, field` at the top) with three
    fields:
    - name (no default)
    - card_id (no default)
    - borrowed, defaulting to an empty list — use
      field(default_factory=list) so members don't share one list
      (the same trap as ex02's Team bug).

    Member("Ada", "M001").name -> "Ada"
    Member("Ada", "M001").borrowed -> []
    Member("Ada", "M001") == Member("Ada", "M001") -> True
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError


class CheckoutError(Exception):
    """Raised when checkout is attempted for a title not in the library."""


class Library:
    """Holds a collection of LibraryItems and lends them to Members."""

    def __init__(self):
        """Set up an empty, internal list of items."""
        raise NotImplementedError

    def add(self, item):
        """Add `item` to the library's collection."""
        raise NotImplementedError

    def __len__(self):
        """Support len(library) -> number of items in the collection."""
        raise NotImplementedError

    def __contains__(self, title):
        """Support `title in library` -> True if any item has that title."""
        raise NotImplementedError

    def checkout(self, member, title):
        """Find the item with `title`, append it to member.borrowed,
        and return it. If no item in the library has that title, raise
        CheckoutError instead.
        """
        raise NotImplementedError

    @property
    def catalog(self):
        """Return every item's title, alphabetically sorted."""
        raise NotImplementedError
