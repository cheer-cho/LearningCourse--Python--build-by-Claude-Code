# Checkpoint 14 — Product Catalog
#
# A vertical slice through the whole module: pydantic validates incoming
# products, SQLAlchemy persists them in an in-memory sqlite database,
# FastAPI serves GET/POST /products on top of both. Everything is
# exercised end-to-end through TestClient — no numpy/pandas here, this
# slice is validate -> store -> serve.
# Run: uv run pytest 14-frameworks-libraries -k checkpoint

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Product(BaseModel):
    """Incoming product data: a unique name and a positive price."""

    name: str
    price: float = Field(gt=0)


class ProductOut(BaseModel):
    """Outgoing product representation, built directly from a
    `ProductRow` (`from_attributes=True` lets FastAPI serialize the ORM
    object without a manual dict conversion).
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float


class Base(DeclarativeBase):
    """Declarative base for the catalog's one table."""


class ProductRow(Base):
    """The `products` table: id, unique name, price."""

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    price: Mapped[float]


def make_engine() -> Engine:
    """Create a fresh in-memory sqlite engine with `products` created.

    Unlike ex07/ex08's `make_engine`, this engine is used through
    FastAPI's `TestClient`, which may call the app from a different
    thread than the one that created the engine — and plain
    `sqlite:///:memory:` gives every new connection its own empty
    database. Pass `connect_args={"check_same_thread": False}` and
    `poolclass=StaticPool` (from `sqlalchemy.pool`) to `create_engine`
    so every checkout shares the one connection and its tables.
    """
    raise NotImplementedError


def find_product(session: Session, name: str) -> ProductRow | None:
    """Return the `ProductRow` named `name`, or None if there isn't one."""
    raise NotImplementedError


def add_product(session: Session, product: Product) -> ProductRow:
    """Insert `product` as a new `ProductRow`, flush, and return it.
    Callers check `find_product` first — this function does not guard
    against duplicates itself.
    """
    raise NotImplementedError


def all_products(session: Session) -> list[ProductRow]:
    """Return every `ProductRow`, via `select(ProductRow)`."""
    raise NotImplementedError


_engine: Engine | None = None


def _get_engine() -> Engine:
    """Lazily create (and cache) the module's one engine. Lazy so that
    importing this file never calls `make_engine()` itself — the first
    real call happens when a test or route actually needs the database.
    """
    global _engine
    if _engine is None:
        _engine = make_engine()
    return _engine


def reset_catalog() -> None:
    """Test-only helper: drop and recreate all tables for a clean slate
    between tests.
    """
    engine = _get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/products", response_model=list[ProductOut])
def list_products() -> list[ProductRow]:
    """GET /products — return every product in the catalog."""
    with Session(_get_engine()) as session:
        return all_products(session)


@app.post("/products", response_model=ProductOut, status_code=201)
def create_product(product: Product) -> ProductRow:
    """POST /products — validate `product` (pydantic body), 409 on a
    duplicate name, else persist it and return it with 201.
    """
    with Session(_get_engine()) as session:
        if find_product(session, product.name) is not None:
            raise HTTPException(status_code=409, detail="product already exists")
        row = add_product(session, product)
        session.commit()
        session.refresh(row)
        return row
