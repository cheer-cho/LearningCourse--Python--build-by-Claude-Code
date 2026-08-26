# Scenario: a checkout system needs money values that compare and add
# safely, and a playlist that works with len()/in. Concepts: __repr__,
# __eq__ (incl. NotImplemented), __add__, __len__, __contains__.
# Run: uv run pytest 08-oop -k ex05


class Money:
    """An amount of money in whole cents, tagged with a currency."""

    def __init__(self, amount_cents, currency):
        self.amount_cents = amount_cents
        self.currency = currency

    def __repr__(self):
        """Return a repr an engineer can read back, e.g.

        Money(500, "USD") -> "Money(500, 'USD')"
        """
        raise NotImplementedError

    def __eq__(self, other):
        """Two Money values are equal if amount_cents AND currency both
        match. If `other` isn't a Money, return NotImplemented (not
        False) so Python can fall back correctly.

        Money(500, "USD") == Money(500, "USD") -> True
        Money(500, "USD") == Money(500, "EUR") -> False
        Money(500, "USD") == "500 USD" -> False (via NotImplemented)
        """
        raise NotImplementedError

    def __add__(self, other):
        """Add two Money values of the SAME currency, returning a new
        Money. Raise ValueError if currencies differ.

        Money(500, "USD") + Money(150, "USD") -> Money(650, "USD")
        """
        raise NotImplementedError


class Playlist:
    """An ordered list of song titles."""

    def __init__(self, songs=None):
        """Store the given songs (or an empty, independent list if
        `songs` is None).
        """
        raise NotImplementedError

    def add_song(self, title):
        """Append `title` to the playlist. Returns nothing."""
        raise NotImplementedError

    def __len__(self):
        """Support len(playlist) -> number of songs."""
        raise NotImplementedError

    def __contains__(self, title):
        """Support `title in playlist` -> True/False."""
        raise NotImplementedError
