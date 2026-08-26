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
        self.cents = cents

    def __repr__(self):
        """Unambiguous repr used in error messages and sorted() output."""
        return f"Money({self.cents})"

    def __eq__(self, other):
        """Equal when both are Money with the same cent amount."""
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __hash__(self):
        """Consistent with __eq__: equal Money objects hash the same."""
        return hash(self.cents)

    def __add__(self, other):
        """Money + Money -> Money. NotImplemented for anything else."""
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)

    def __mul__(self, factor):
        """Money * int -> Money (scales the amount). No Money * Money."""
        if not isinstance(factor, int):
            return NotImplemented
        return Money(self.cents * factor)

    __rmul__ = __mul__

    def __lt__(self, other):
        """Enables sorted()/min()/max() over Money values."""
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents < other.cents

    def __le__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents <= other.cents
