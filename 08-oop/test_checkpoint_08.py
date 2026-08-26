import pytest
from checkpoint_08 import Book, CheckoutError, Dvd, Library, LibraryItem, Member


def test_library_item_stores_title_and_year():
    item = LibraryItem("Dune", 1965)
    assert item.title == "Dune"
    assert item.year == 1965


def test_library_item_default_loan_period():
    assert LibraryItem("Dune", 1965).loan_period == 21


def test_library_item_repr():
    assert repr(LibraryItem("Dune", 1965)) == "LibraryItem('Dune', 1965)"


def test_book_has_longer_loan_period():
    book = Book("Dune", 1965, "Frank Herbert")
    assert book.loan_period == 28


def test_book_stores_fields_via_super_init():
    book = Book("Dune", 1965, "Frank Herbert")
    assert book.title == "Dune"
    assert book.year == 1965
    assert book.author == "Frank Herbert"


def test_book_repr_uses_its_own_class_name():
    book = Book("Dune", 1965, "Frank Herbert")
    assert repr(book) == "Book('Dune', 1965)"


def test_dvd_has_shorter_loan_period():
    dvd = Dvd("Arrival", 2016)
    assert dvd.loan_period == 7


def test_dvd_inherits_init_and_repr_from_library_item():
    dvd = Dvd("Arrival", 2016)
    assert dvd.title == "Arrival"
    assert repr(dvd) == "Dvd('Arrival', 2016)"


def test_member_default_borrowed_is_empty():
    member = Member("Ada", "M001")
    assert member.borrowed == []


def test_member_borrowed_is_independent_per_instance():
    a = Member("Ada", "M001")
    b = Member("Bo", "M002")
    a.borrowed.append("something")
    assert b.borrowed == []


def test_member_generated_eq_compares_by_value():
    assert Member("Ada", "M001") == Member("Ada", "M001")


def test_library_starts_empty():
    assert len(Library()) == 0


def test_library_add_increases_length():
    library = Library()
    library.add(Book("Dune", 1965, "Frank Herbert"))
    library.add(Dvd("Arrival", 2016))
    assert len(library) == 2


def test_library_contains_checks_by_title():
    library = Library()
    library.add(Book("Dune", 1965, "Frank Herbert"))
    assert "Dune" in library
    assert "Nonexistent" not in library


def test_library_checkout_moves_item_into_member_borrowed():
    library = Library()
    book = Book("Dune", 1965, "Frank Herbert")
    library.add(book)
    member = Member("Ada", "M001")

    returned = library.checkout(member, "Dune")

    assert returned is book
    assert member.borrowed == [book]


def test_library_checkout_raises_checkout_error_for_missing_title():
    library = Library()
    library.add(Book("Dune", 1965, "Frank Herbert"))
    member = Member("Ada", "M001")

    with pytest.raises(CheckoutError):
        library.checkout(member, "Nonexistent")


def test_library_catalog_is_sorted_titles():
    library = Library()
    library.add(Book("Dune", 1965, "Frank Herbert"))
    library.add(Dvd("Arrival", 2016))
    library.add(Book("Contact", 1985, "Carl Sagan"))

    assert library.catalog == ["Arrival", "Contact", "Dune"]
