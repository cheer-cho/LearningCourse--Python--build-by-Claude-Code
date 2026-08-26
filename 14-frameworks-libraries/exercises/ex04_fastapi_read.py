# Scenario: a read-only "items" API — a health check, look up one item,
# list items with an optional filter. Concepts: FastAPI app, path params,
# query params, 404 via HTTPException, automatic 422 validation,
# TestClient.
# Run: uv run pytest 14-frameworks-libraries -k ex04

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()

_ITEMS: dict[int, str] = {1: "Widget", 2: "Gadget", 3: "Widget Pro"}


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness check. Always returns {"status": "ok"}."""
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, object]:
    """Look up one item by id.

    `item_id` is typed as `int`, so FastAPI rejects a non-numeric id
    with a 422 automatically — no code needed for that part.

    read_item(1) -> {"id": 1, "name": "Widget"}
    read_item(999) -> raises HTTPException(404) — no item 999
    """
    raise NotImplementedError


@app.get("/items")
def list_items(prefix: str = "") -> list[dict[str, object]]:
    """List every item whose name starts with `prefix` (default ""
    matches everything), as `[{"id": ..., "name": ...}, ...]`.

    list_items(prefix="Widget") -> [{"id": 1, "name": "Widget"}, {"id": 3, "name": "Widget Pro"}]
    """
    raise NotImplementedError
