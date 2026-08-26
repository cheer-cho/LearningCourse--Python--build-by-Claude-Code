from dataclasses import dataclass, field


class LibraryItem:
    loan_period = 21

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"{type(self).__name__}({self.title!r}, {self.year})"


class Book(LibraryItem):
    loan_period = 28

    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author


class Dvd(LibraryItem):
    loan_period = 7


@dataclass
class Member:
    name: str
    card_id: str
    borrowed: list = field(default_factory=list)


class CheckoutError(Exception):
    """Raised when checkout is attempted for a title not in the library."""


class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __contains__(self, title):
        return any(item.title == title for item in self._items)

    def checkout(self, member, title):
        for item in self._items:
            if item.title == title:
                member.borrowed.append(item)
                return item
        raise CheckoutError(f"no item titled {title!r} in the library")

    @property
    def catalog(self):
        return sorted(item.title for item in self._items)
