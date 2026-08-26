# Handoff: Module 15 — Capstone Projects

Build `15-capstones/` in the course repo. Read `CONVENTIONS.md` (same
folder) and the master spec first. You own ONLY this folder.

Audience: finished modules 01–14. Capstones are graduation work: the
student builds each from a written brief against acceptance tests —
no step-by-step hand-holding.

## Structural deviations (intentional, for this module only)
- No `checkpoint_15.py` — the three capstones ARE the checkpoints
  (ROADMAP already lists Capstone A/B/C).
- Each capstone is ONE flat module in `exercises/` (single-file apps
  are fine and keep `scripts/verify_solutions.py 15` working):
  `capstone_taskman.py`, `capstone_pipeline.py`, `capstone_api.py`,
  each with `test_capstone_*.py` acceptance tests and a full reference
  solution in `solutions/`.
- Stubs here are THIN: module docstring (the brief's TL;DR), the
  required public functions/classes with docstrings and
  NotImplementedError bodies — no scaffolded logic. The challenge is
  the point.
- Every test file starts with `pytest.importorskip` for its third-party
  deps (typer/sqlalchemy for A, pandas for B, fastapi/pydantic/httpx
  for C). No network, no running servers, sqlite :memory: or tmp_path
  only.
- LESSON.md is the briefing document (one section per capstone: goal,
  user stories, required public API, acceptance criteria, suggested
  module-skills checklist). SUMMARY.md is the course wrap-up.

## Capstone A — `capstone_taskman.py` (Typer + SQLAlchemy + typing)
CLI task manager, fully type-hinted (its acceptance tests include a
mypy --strict subprocess check like module 10's).
Public API: SQLAlchemy 2.0 `TaskRow`; `make_engine(url)`;
service layer `add_task(session, title, *, priority)`,
`complete_task(session, task_id)` (custom TaskNotFound),
`list_tasks(session, *, include_done, sort)`; Typer app with commands
`add`, `done`, `list` (table-ish text output), `stats` (counts by
priority). Acceptance tests: service layer against :memory: engine +
CLI via CliRunner with a tmp sqlite file, error paths included.

## Capstone B — `capstone_pipeline.py` (pandas + files + errors)
Data pipeline over a messy dataset. Ship a committed fixture
`data/messy_sales.csv` (~40 rows you author: mixed date formats,
"N/A"/empty cells, duplicated rows, inconsistent region casing, a
negative quantity, prices with "$").
Public API: `load_sales(path)` (raises PipelineError on missing file),
`clean(df)` (parse dates, normalize regions, drop dupes, coerce
money/qty, drop-and-report bad rows → returns (clean_df, issues list)),
`aggregate(df)` (revenue by region and by month),
`report(agg) -> str` (formatted text), `run(argv)` argparse front-end
writing the report to an output path. Acceptance tests assert exact
cleaned shapes/values from the fixture and the issues list, using
tmp_path for outputs.

## Capstone C — `capstone_api.py` (FastAPI + pydantic + httpx client)
A "bookshelf" service AND its client in one module.
Service: pydantic `Book` (validation: year bounds, non-empty title),
in-memory store with reset helper, endpoints: POST /books (201/409),
GET /books (filter `?author=`), GET /books/{id} (404), DELETE, and
GET /stats (counts by author). Client class `BookshelfClient` wrapping
an injected `httpx.Client` (tests wire it to the app via
`httpx.Client(transport=httpx.WSGITransport?` — NO: use
`fastapi.testclient.TestClient` directly as the injected client since
it IS an httpx-compatible client; verify this works) with methods
`add_book`, `find_by_author`, `remove`, raising ApiError on non-2xx.
Acceptance tests drive everything through BookshelfClient over
TestClient — full loop, no sockets.

## SUMMARY.md — course wrap-up (not a module cheat-sheet)
- Mermaid mindmap: the whole course's skill tree (modules as branches).
- "You can now…" checklist mapping each capstone to the modules it
  proved.
- Where to go next: real projects, reading the stdlib docs, PEP 8/20,
  contributing, deeper ecosystems (Django, polars, ruff internals) —
  short, encouraging, no fluff.

Finish with every "Definition of done" check from CONVENTIONS.md
(items about LESSON/SUMMARY interpreted per the deviations above);
`uv run python scripts/verify_solutions.py 15` MUST pass with all
three reference solutions, and stub-state tests must be red-only (or
skipped where deps are absent — but in THIS repo deps are installed,
so expect red).
