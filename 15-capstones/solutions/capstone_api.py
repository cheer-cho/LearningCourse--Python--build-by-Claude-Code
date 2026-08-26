# Capstone C: a "bookshelf" FastAPI service AND its httpx-based client,
# in one module. Concepts: pydantic validation, FastAPI routing/error
# responses, and wrapping an injected httpx-compatible client.
# Run: uv run pytest 15-capstones -k capstone_api

from __future__ import annotations

import httpx
from fastapi import FastAPI, HTTPException
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
    global _next_id
    _books.clear()
    _next_id = 1


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookIn) -> Book:
    """Add a book. 409 if one with the same title AND author exists."""
    global _next_id
    for existing in _books.values():
        if existing.title == book.title and existing.author == book.author:
            raise HTTPException(status_code=409, detail="book already exists")
    row = Book(id=_next_id, **book.model_dump())
    _books[row.id] = row
    _next_id += 1
    return row


@app.get("/books", response_model=list[Book])
def get_books(author: str | None = None) -> list[Book]:
    """List books, optionally filtered to those by `author`."""
    books = list(_books.values())
    if author is not None:
        books = [b for b in books if b.author == author]
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Fetch one book by id. 404 if it doesn't exist."""
    book = _books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="book not found")
    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    """Remove a book by id. 404 if it doesn't exist."""
    if book_id not in _books:
        raise HTTPException(status_code=404, detail="book not found")
    del _books[book_id]


@app.get("/stats")
def get_stats() -> dict[str, int]:
    """Return the count of books per author."""
    counts: dict[str, int] = {}
    for book in _books.values():
        counts[book.author] = counts.get(book.author, 0) + 1
    return counts


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

    def _check(self, response: httpx.Response) -> httpx.Response:
        if response.status_code >= 400:
            raise ApiError(f"{response.status_code}: {response.text}")
        return response

    def add_book(self, title: str, author: str, year: int) -> Book:
        """POST a new book. Raises ApiError on 409 (duplicate) or 4xx/5xx."""
        response = self._check(
            self._client.post("/books", json={"title": title, "author": author, "year": year})
        )
        return Book.model_validate(response.json())

    def find_by_author(self, author: str) -> list[Book]:
        """GET books filtered by `author`."""
        response = self._check(self._client.get("/books", params={"author": author}))
        return [Book.model_validate(item) for item in response.json()]

    def remove(self, book_id: int) -> None:
        """DELETE a book by id. Raises ApiError on 404 or 4xx/5xx."""
        self._check(self._client.delete(f"/books/{book_id}"))

    def stats(self) -> dict[str, int]:
        """GET /stats — book counts per author."""
        response = self._check(self._client.get("/stats"))
        result: dict[str, int] = response.json()
        return result
