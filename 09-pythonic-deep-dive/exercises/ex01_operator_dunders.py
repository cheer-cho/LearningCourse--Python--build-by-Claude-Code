# Scenario: a tiny money type for a shopping cart. Covers the operator
# protocol — __add__, __mul__, __lt__/__le__, __eq__/__hash__ — and the
# NotImplemented convention for mixed-type operations.
# Run: uv run pytest 09-pythonic-deep-dive -k ex01


class Money:
    """An amount of money stored as a whole number of cents, so
    arithmetic never suffers floating-point rounding errors. Joins the
    operator protocol: `+`, `*` (by an int), `<`/`<=` (so `sorted()`
    works), `==`, and `hash()`.

    Money(500) + Money(150) -> Money(650)
    Money(500) * 3 -> Money(1500)
    Money(500) == Money(500) -> True
    sorted([Money(500), Money(100)]) -> [Money(100), Money(500)]
    hash(Money(500)) == hash(Money(500)) -> True
    """

    def __init__(self, cents):
        raise NotImplementedError

    def __repr__(self):
        """Unambiguous repr used in error messages and sorted() output."""
        raise NotImplementedError

    def __eq__(self, other):
        """Equal when both are Money with the same cent amount. Return
        NotImplemented (not False) for any non-Money `other`."""
        raise NotImplementedError

    def __hash__(self):
        """Consistent with __eq__: equal Money objects hash the same."""
        raise NotImplementedError

    def __add__(self, other):
        """Money + Money -> Money. NotImplemented for anything else."""
        raise NotImplementedError

    def __mul__(self, factor):
        """Money * int -> Money (scales the amount). NotImplemented for
        non-int factors (no Money * Money)."""
        raise NotImplementedError

    __rmul__ = __mul__

    def __lt__(self, other):
        """Enables sorted()/min()/max() over Money values."""
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError
