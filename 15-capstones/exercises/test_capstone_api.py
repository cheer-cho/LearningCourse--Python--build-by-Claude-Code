"""Acceptance tests for Capstone C. Everything is driven through
BookshelfClient wrapping a fastapi.testclient.TestClient — no sockets,
no running server. `reset_store()` runs before every test so the
in-memory shelf starts empty each time.
"""

from __future__ import annotations

import pytest

pytest.importorskip("fastapi")
pytest.importorskip("pydantic")
pytest.importorskip("httpx")

from capstone_api import (
    ApiError,
    Book,
    BookIn,
    BookshelfClient,
    app,
    reset_store,
)
from fastapi.testclient import TestClient
from pydantic import ValidationError


@pytest.fixture
def client():
    reset_store()
    with TestClient(app) as tc:
        yield BookshelfClient(tc)


# --- pydantic validation -------------------------------------------------


def test_bookin_rejects_empty_title():
    with pytest.raises(ValidationError):
        BookIn(title="", author="Ada Lovelace", year=1843)


def test_bookin_rejects_year_out_of_bounds():
    with pytest.raises(ValidationError):
        BookIn(title="Time Traveler's Diary", author="Anon", year=1000)


def test_bookin_accepts_a_valid_book():
    book = BookIn(title="Dune", author="Frank Herbert", year=1965)
    assert book.title == "Dune"
    assert book.year == 1965


# --- BookshelfClient over TestClient --------------------------------------


def test_add_book_returns_book_with_assigned_id(client):
    book = client.add_book("Dune", "Frank Herbert", 1965)
    assert isinstance(book, Book)
    assert book.id is not None
    assert book.title == "Dune"


def test_add_duplicate_book_raises_api_error(client):
    client.add_book("Dune", "Frank Herbert", 1965)
    with pytest.raises(ApiError):
        client.add_book("Dune", "Frank Herbert", 1965)


def test_find_by_author_filters_correctly(client):
    client.add_book("Dune", "Frank Herbert", 1965)
    client.add_book("Children of Dune", "Frank Herbert", 1976)
    client.add_book("Foundation", "Isaac Asimov", 1951)

    herbert_books = client.find_by_author("Frank Herbert")
    assert {b.title for b in herbert_books} == {"Dune", "Children of Dune"}

    asimov_books = client.find_by_author("Isaac Asimov")
    assert {b.title for b in asimov_books} == {"Foundation"}


def test_find_by_author_no_matches_returns_empty_list(client):
    client.add_book("Dune", "Frank Herbert", 1965)
    assert client.find_by_author("Nobody") == []


def test_remove_deletes_the_book(client):
    book = client.add_book("Dune", "Frank Herbert", 1965)
    client.remove(book.id)
    assert client.find_by_author("Frank Herbert") == []


def test_remove_missing_book_raises_api_error(client):
    with pytest.raises(ApiError):
        client.remove(999)


def test_stats_counts_books_per_author(client):
    client.add_book("Dune", "Frank Herbert", 1965)
    client.add_book("Children of Dune", "Frank Herbert", 1976)
    client.add_book("Foundation", "Isaac Asimov", 1951)

    stats = client.stats()
    assert stats == {"Frank Herbert": 2, "Isaac Asimov": 1}


def test_stats_empty_shelf_is_empty_dict(client):
    assert client.stats() == {}


# --- direct HTTP-level checks (through the same TestClient) --------------


def test_get_book_by_id_returns_404_for_missing_id():
    reset_store()
    with TestClient(app) as tc:
        response = tc.get("/books/12345")
    assert response.status_code == 404


def test_post_books_returns_201_and_the_created_book():
    reset_store()
    with TestClient(app) as tc:
        response = tc.post(
            "/books", json={"title": "Dune", "author": "Frank Herbert", "year": 1965}
        )
    assert response.status_code == 201
    assert response.json()["title"] == "Dune"
