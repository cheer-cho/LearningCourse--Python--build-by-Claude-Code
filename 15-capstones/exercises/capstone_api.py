# Capstone C: build a "bookshelf" FastAPI service AND its httpx-based
# client, in one module. Concepts: pydantic validation, FastAPI
# routing/error responses, wrapping an injected httpx-compatible client.
# Brief: LESSON.md. Run: uv run pytest 15-capstones -k capstone_api

from __future__ import annotations

import httpx
from fastapi import FastAPI
from pydantic import BaseModel, Field

MIN_YEAR = 1450  # Gutenberg's press — a plausible earliest publication year
MAX_YEAR = 2100  # generous ceiling; keeps the bound simple and stable


class BookIn(BaseModel):
    """Payload for creating a book. Validation: `title` and `author`
    can't be empty/whitespace-only; `year` must be within
    [MIN_YEAR, MAX_YEAR].
    """

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=MIN_YEAR, le=MAX_YEAR)


class Book(BookIn):
    """A stored book: `BookIn`'s fields plus the server-assigned `id`."""

    id: int


app = FastAPI(title="Bookshelf")

_books: dict[int, Book] = {}
_next_id: int = 1


def reset_store() -> None:
    """Clear every book and reset the id counter back to 1.

    Call this between tests so each test starts from an empty shelf.
    """
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookIn) -> Book:
    """Add a book. 409 if one with the same title AND author exists."""
    raise NotImplementedError


@app.get("/books", response_model=list[Book])
def get_books(author: str | None = None) -> list[Book]:
    """List books, optionally filtered to those by `author`."""
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Fetch one book by id. 404 if it doesn't exist."""
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    """Remove a book by id. 404 if it doesn't exist."""
    raise NotImplementedError


@app.get("/stats")
def get_stats() -> dict[str, int]:
    """Return the count of books per author."""
    raise NotImplementedError


class ApiError(Exception):
    """Raised by BookshelfClient when the API returns a non-2xx response."""


class BookshelfClient:
    """Thin wrapper around an httpx-compatible client for the bookshelf
    API. `client` can be a real `httpx.Client` or, in tests, a
    `fastapi.testclient.TestClient` — it subclasses `httpx.Client`, so
    it satisfies this same interface with no network involved.
    """

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def add_book(self, title: str, author: str, year: int) -> Book:
        """POST a new book. Raises ApiError on 409 (duplicate) or 4xx/5xx."""
        raise NotImplementedError

    def find_by_author(self, author: str) -> list[Book]:
        """GET books filtered by `author`."""
        raise NotImplementedError

    def remove(self, book_id: int) -> None:
        """DELETE a book by id. Raises ApiError on 404 or 4xx/5xx."""
        raise NotImplementedError

    def stats(self) -> dict[str, int]:
        """GET /stats — book counts per author."""
        raise NotImplementedError
