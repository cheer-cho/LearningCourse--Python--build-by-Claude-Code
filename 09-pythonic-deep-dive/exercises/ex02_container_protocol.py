# Scenario: a playing-card deck. Covers the container protocol —
# __len__, __getitem__ (index AND slice), __contains__ — which unlocks
# for/in/random.choice for free.
# Run: uv run pytest 09-pythonic-deep-dive -k ex02

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Deck:
    """A standard 52-card deck, built once from ranks x suits. Joining
    the container protocol (`__len__`, `__getitem__`, `__contains__`)
    gives you `len()`, indexing, slicing, `for`/`in`, and
    `random.choice()` for free — `random.choice` only needs `__len__`
    and `__getitem__`.

    Deck() has 52 cards in rank-major, suit-minor order:
    ("2","Clubs"), ("2","Diamonds"), ("2","Hearts"), ("2","Spades"),
    ("3","Clubs"), ...
    len(Deck()) -> 52
    Deck()[0] -> ("2", "Clubs")
    Deck()[:2] -> [("2","Clubs"), ("2","Diamonds")]
    ("A", "Spades") in Deck() -> True
    ("Joker", "Clubs") in Deck() -> False
    """

    def __init__(self):
        """Build self.cards ONCE here: every (rank, suit) pair, ranks
        outer loop, suits inner loop."""
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, index):
        """Supports both a single int index and a slice — delegate to
        the underlying list, it already handles both."""
        raise NotImplementedError

    def __contains__(self, card):
        raise NotImplementedError
