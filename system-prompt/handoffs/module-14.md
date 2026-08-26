# Handoff: Module 14 — Frameworks & Libraries

Build `14-frameworks-libraries/` in the course repo. Read
`CONVENTIONS.md` (same folder) and the master spec first. You own ONLY
this folder.

Audience: completed modules 01–13. Solutions fully type-hinted where
natural. Coverage philosophy: the 20% of each library used 80% of the
time — practical, not encyclopedic.

## Dependencies (already installed — do NOT touch pyproject/uv.lock)
pydantic, httpx, fastapi, typer, sqlalchemy, numpy, pandas live in the
`frameworks` dependency group and are already synced into the project
env. BUT a student on a fresh clone may not have them, so EVERY test
file in this module starts with `pytest.importorskip("<package>")`
(before other third-party imports) so the suite degrades to skips, not
collection errors. LESSON.md opens with a setup box:
`uv sync --all-groups` enables this module.

Constraints: no network access in any test (httpx uses MockTransport;
FastAPI uses TestClient; SQLAlchemy uses sqlite:///:memory:). No
running servers ever. Keep pandas/numpy exercises small and
deterministic. FastAPI's TestClient needs no extra deps beyond what's
installed (httpx is present — verify once).

## LESSON.md outline
1. Why this exists: the stdlib ends where the ecosystem begins —
   REQUIRED diagram: map of the Python ecosystem by job (validate →
   pydantic; HTTP → httpx; API → FastAPI; CLI → Typer; DB → SQLAlchemy;
   numbers → numpy; tables → pandas) with arrows showing how they
   compose.
2. One tight section per library (micro-example each, ≤ 15 lines):
   - pydantic v2: BaseModel, validation errors, Field constraints,
     model_validate / model_dump — "runtime types" vs module 10's
     static types (call the contrast out explicitly).
   - httpx: Client, raise_for_status, .json(); MockTransport for tests.
   - FastAPI: app, path/query/body params, pydantic response models,
     status codes, TestClient — REQUIRED diagram: request → route →
     validation → handler → response flow.
   - Typer: commands, arguments vs options, CliRunner testing.
   - SQLAlchemy 2.0 style ONLY: DeclarativeBase, Mapped/mapped_column,
     Session, select() — REQUIRED diagram: objects ↔ session ↔ engine
     ↔ sqlite.
   - numpy: array, dtype, vectorized ops, boolean masks, aggregation.
   - pandas: DataFrame, filtering, groupby-agg, new columns; "vectorize,
     don't iterate rows".
3. Gotchas: pydantic v1-vs-v2 API confusion, SQLAlchemy 1.x-style
   queries found in old tutorials, pandas SettingWithCopy, mutable
   session state.
4. Try it now → exercises.

## Exercises (exactly 10)
- `ex01_pydantic_basics.py` — `User(BaseModel)` (name, email
  EmailStr? NO — keep to `str` + a field_validator requiring "@";
  age with ge=0 Field): `parse_user(data)` returning User or raising;
  test asserts ValidationError details.
- `ex02_pydantic_nested.py` — `Order` with nested `list[Item]`,
  computed total via property or method; `load_orders(json_text)`
  using model_validate_json / TypeAdapter; `model_dump` roundtrip.
- `ex03_httpx_client.py` — functions taking an `httpx.Client`:
  `get_json(client, url)` with raise_for_status → custom ApiError;
  `fetch_with_retry(client, url, attempts)` retrying on 5xx. Tests
  build `httpx.Client(transport=httpx.MockTransport(handler))`.
- `ex04_fastapi_read.py` — build `app`: GET /health, GET
  /items/{item_id} (404 on miss from a module-level dict), GET /items
  with `?prefix=` filtering; TestClient tests incl. 404 and validation
  (string item_id → 422).
- `ex05_fastapi_write.py` — POST /items with pydantic body →
  201 + response_model, duplicate → 409; DELETE /items/{id}; state
  reset fixture pattern between tests (mutable module dict + a reset
  helper the tests call).
- `ex06_typer_cli.py` — Typer app `todo`: `add TEXT --priority`,
  `list --all/--done`, storage injected as an in-memory list module
  state with reset helper; tests via `typer.testing.CliRunner`
  asserting output and exit codes.
- `ex07_sqlalchemy_models.py` — 2.0 declarative `TaskRow` model
  (id PK autoincrement, title, done bool default False);
  `make_engine()` (sqlite :memory:, create_all); `add_task(session,
  title)`; `all_tasks(session)` via select().scalars().
- `ex08_sqlalchemy_queries.py` — seeded fixture data:
  `open_tasks(session)`, `rename_task(session, id, title)`,
  `complete_and_count(session, id)`, one-to-many `Project → TaskRow`
  relationship with `tasks_of(session, project_name)`.
- `ex09_numpy.py` — `normalize(arr)` (min-max, guard zero-range),
  `above_mean(arr)` boolean mask count, `moving_average(arr, k)`
  (convolve or sliding trick), `grid_distance(points)` vectorized —
  assert with numpy.testing / pytest.approx.
- `ex10_pandas.py` — from a records list: `to_frame(records)`,
  `revenue_by_region(df)` (groupby-agg → plain dict for asserts),
  `add_margin_column(df)`, `top_products(df, n)` (sort_values +
  head); all asserts on `.to_dict()` outputs for readability.

## Checkpoint (`checkpoint_14.py`)
A vertical slice "product catalog": pydantic `Product` model →
SQLAlchemy `ProductRow` + in-memory store functions → FastAPI app with
GET/POST /products (validation via the pydantic model, persistence via
the SQLAlchemy session) — acceptance-tested end-to-end through
TestClient only. (Skip numpy/pandas here; the slice is
validate→store→serve.)

## SUMMARY.md
Cheat-sheet: one "starter block" per library (the 5–10 lines you paste
to begin), the ecosystem map recap, a "which tool for which job"
table. One mermaid mindmap. Self-quiz: 8 questions, answers in
`<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
Watch runtime: keep the whole module's tests under ~20 seconds.
