from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Engine, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.pool import StaticPool


class Product(BaseModel):
    name: str
    price: float = Field(gt=0)


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float


class Base(DeclarativeBase):
    pass


class ProductRow(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    price: Mapped[float]


def make_engine() -> Engine:
    # StaticPool + check_same_thread=False: FastAPI's TestClient can call
    # the app from a different thread than the one that created the
    # engine, and plain sqlite:///:memory: gives each new connection its
    # own empty database. A single shared connection fixes both.
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    return engine


def find_product(session: Session, name: str) -> ProductRow | None:
    return session.scalar(select(ProductRow).where(ProductRow.name == name))


def add_product(session: Session, product: Product) -> ProductRow:
    row = ProductRow(name=product.name, price=product.price)
    session.add(row)
    session.flush()
    return row


def all_products(session: Session) -> list[ProductRow]:
    return list(session.scalars(select(ProductRow)))


_engine: Engine | None = None


def _get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = make_engine()
    return _engine


def reset_catalog() -> None:
    engine = _get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


app = FastAPI()


@app.get("/products", response_model=list[ProductOut])
def list_products() -> list[ProductRow]:
    with Session(_get_engine()) as session:
        return all_products(session)


@app.post("/products", response_model=ProductOut, status_code=201)
def create_product(product: Product) -> ProductRow:
    with Session(_get_engine()) as session:
        if find_product(session, product.name) is not None:
            raise HTTPException(status_code=409, detail="product already exists")
        row = add_product(session, product)
        session.commit()
        session.refresh(row)
        return row
