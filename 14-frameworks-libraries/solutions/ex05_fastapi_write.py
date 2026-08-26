from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class ItemIn(BaseModel):
    name: str
    price: float = Field(gt=0)


class ItemOut(BaseModel):
    id: int
    name: str
    price: float


app = FastAPI()

_items: dict[int, ItemOut] = {}
_next_id = 1


def reset_items() -> None:
    global _next_id
    _items.clear()
    _next_id = 1


@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemIn) -> ItemOut:
    global _next_id
    if any(existing.name == item.name for existing in _items.values()):
        raise HTTPException(status_code=409, detail="item already exists")
    created = ItemOut(id=_next_id, name=item.name, price=item.price)
    _items[created.id] = created
    _next_id += 1
    return created


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="item not found")
    del _items[item_id]
