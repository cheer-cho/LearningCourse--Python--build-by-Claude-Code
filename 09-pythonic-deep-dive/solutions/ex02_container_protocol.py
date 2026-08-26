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
        self.cards = [(rank, suit) for rank in RANKS for suit in SUITS]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        """Supports both a single int index and a slice."""
        return self.cards[index]

    def __contains__(self, card):
        return card in self.cards
