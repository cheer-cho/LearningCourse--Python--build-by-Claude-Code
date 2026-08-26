class Money:
    def __init__(self, amount_cents, currency):
        self.amount_cents = amount_cents
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount_cents}, {self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self.amount_cents, self.currency) == (other.amount_cents, other.currency)

    def __add__(self, other):
        if not isinstance(other, Money) or other.currency != self.currency:
            raise ValueError("cannot add Money values with different currencies")
        return Money(self.amount_cents + other.amount_cents, self.currency)


class Playlist:
    def __init__(self, songs=None):
        self.songs = list(songs) if songs is not None else []

    def add_song(self, title):
        self.songs.append(title)

    def __len__(self):
        return len(self.songs)

    def __contains__(self, title):
        return title in self.songs
