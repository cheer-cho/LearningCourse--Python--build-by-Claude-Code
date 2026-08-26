from fastapi import FastAPI, HTTPException

app = FastAPI()

_ITEMS: dict[int, str] = {1: "Widget", 2: "Gadget", 3: "Widget Pro"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, object]:
    if item_id not in _ITEMS:
        raise HTTPException(status_code=404, detail="item not found")
    return {"id": item_id, "name": _ITEMS[item_id]}


@app.get("/items")
def list_items(prefix: str = "") -> list[dict[str, object]]:
    return [{"id": id_, "name": name} for id_, name in _ITEMS.items() if name.startswith(prefix)]
