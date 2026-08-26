Build a complete, self-paced Python mastery course as a Git repository
that I will study inside VS Code with you (Claude Code) acting as my
instructor. Follow this spec exactly. It uses the same system as my
TypeScript course (`../TypeScript/Course-Created-By-Claude/`) — reuse its
conventions wherever this spec doesn't say otherwise.

## Goal
I want to go from **zero to hero** in Python: every piece of syntax, every
core concept, the standard library, idiomatic "Pythonic" style, static
typing with type hints, and the important frameworks and libraries used in
real work. The course must be hands-on first: I learn by writing code and
making tests pass, not by reading long documents.

Assume **no prior Python knowledge**. I do know TypeScript — when a Python
concept has a direct TS analogue (e.g. type hints vs TS types, dicts vs
objects, async/await), a one-line "coming from TypeScript" note is welcome,
but never required to understand the lesson.

## Readability & diagrams (applies to EVERY document in the course)
- Write for clarity above all: short sentences, plain language, one idea
  per paragraph. Assume I'm smart but new to the concept.
- Every LESSON.md must follow this flow: (1) "Why this exists" — the
  problem the feature solves, in 2–3 sentences; (2) a Mermaid diagram
  showing the concept visually; (3) minimal syntax with a tiny runnable
  example; (4) common gotchas; (5) "Try it now" pointer to exercises.
- Use Mermaid diagrams generously to show flows and relationships,
  for example:
  - flowchart for exception propagation (try → except → else → finally)
  - flowchart for the import system / module resolution
  - graph for the iteration protocol (iterable → __iter__ → iterator →
    __next__ → StopIteration)
  - graph for method resolution order (MRO) in inheritance
  - sequence diagram for the asyncio event loop and await
  - flowchart for how a decorator wraps a function
  - graph for mutable vs immutable types and name-binding semantics
  - mindmap in each SUMMARY.md recapping the module's concepts
- Every diagram must have a one-line caption saying what to notice.
- ROADMAP.md must open with a single Mermaid flowchart of the entire
  course: modules as nodes, arrows showing the learning path, checkpoints
  marked as diamond nodes, with the "heart" module highlighted.
- Prefer a diagram + short prose over long prose. If a concept involves
  any flow, hierarchy, or decision, it gets a diagram.
- Use tables for comparisons (list vs tuple, is vs ==, args vs kwargs,
  threading vs multiprocessing vs asyncio, dataclass vs NamedTuple vs
  dict, etc.).

## Repository structure
Mirror the TypeScript course exactly, adapted to Python:
- README.md — course overview, prerequisites (none beyond a computer),
  setup with `uv` (fallback instructions for plain `python -m venv` +
  `pip`), how to run exercises and tests, how to enable Mermaid preview
  in VS Code.
- ROADMAP.md — full learning path as a checklist with checkboxes for
  every module and checkpoint, opening with the course-map flowchart.
  This is my progress tracker.
- CLAUDE.md — instructions that turn you into my instructor whenever I
  open this repo (spec below).
- One folder per module: `01-setup-tooling/`, `02-values-variables/`,
  etc. Each module contains:
  - LESSON.md — concise, diagram-first concept explanation (short —
    teach the minimum needed to attempt exercises).
  - exercises/ — numbered exercise files (ex01.py, ex02.py, ...) with
    TODO stubs and clear instructions in comments. Many exercises per
    topic, progressing from simple to hard.
  - solutions/ — reference solutions, kept out of my way (I should not
    see them unless I ask).
  - exercises/test_ex*.py — pytest tests verifying every exercise.
    From module 10 (typing) onward, exercises are ALSO checked with
    `mypy --strict`; a wrong or missing type hint must fail the check,
    never silently pass.
  - SUMMARY.md — one-page cheat-sheet: key syntax, rules, gotchas, a
    Mermaid mindmap of the concepts, and a 5–10 question self-quiz.
  - checkpoint.py — a graded checkpoint combining everything in the
    module. Passing its tests = module complete.
- playground/ — scratch space for experiments with my instructor.
- NOTES.md — instructor's log of my recurring mistakes.
- In every stub file (exercises and checkpoints), each function/class
  carries its own plain-English docstring or comment directly above it:
  what it does, inputs and outputs, edge cases, and 1–3 input → output
  examples. The file header stays short (scenario + concepts + how to
  run the tests) — never a numbered spec the reader must map back to
  declarations by hand.

## Curriculum (zero → hero; expand as needed, but at minimum)
1.  **Setup & tooling**: installing Python 3.12+, `uv` (venvs, deps,
    `uv run`), the REPL, running scripts, VS Code + Python extension,
    how pytest works (just enough to do exercises), ruff for lint/format,
    reading tracebacks.
2.  **Values & variables**: numbers (int/float, integer division, floor
    vs true division), strings & f-strings, booleans, None, operators,
    input/print, name binding (variables are labels, not boxes),
    mutability preview.
3.  **Control flow**: if/elif/else, truthiness rules, while, for +
    range, break/continue/else-on-loops, match/case (structural pattern
    matching).
4.  **Collections**: list, tuple, dict, set; indexing & slicing;
    unpacking (incl. starred); nesting; comprehensions (list/dict/set);
    copying vs aliasing; choosing the right collection.
5.  **Functions**: def, return, default parameters (and the mutable
    default trap), *args/**kwargs, keyword-only and positional-only
    params, scope & LEGB, closures, lambda, recursion, docstrings.
6.  **Errors, files & context managers**: exceptions, try/except/else/
    finally, raise & exception chaining, custom exceptions, EAFP vs
    LBYL, `with`, file I/O, pathlib, json & csv basics.
7.  **Modules & organization**: import forms, packages & `__init__.py`,
    `if __name__ == "__main__"`, the standard-library mindset ("batteries
    included" tour), project layout, pyproject.toml, adding dependencies
    with uv, virtualenv hygiene.
8.  **Object-oriented Python**: classes, `__init__`, methods, instance
    vs class attributes, properties, classmethod/staticmethod,
    inheritance & MRO, `super()`, dunder basics (`__repr__`, `__eq__`,
    `__len__`), dataclasses, ABCs vs duck typing.
9.  **Pythonic deep-dive (the heart of the course — go heavy here)**:
    - the data model: dunder protocols (`__getitem__`, `__contains__`,
      `__call__`, operator overloading, `__hash__` rules)
    - the iteration protocol; writing iterators by hand
    - generators, `yield`, generator expressions, lazy pipelines,
      `yield from`
    - decorators (plain, parameterized, class-based, `functools.wraps`)
    - writing context managers (`__enter__`/`__exit__`, contextlib)
    - functools (partial, lru_cache, reduce, singledispatch) and
      itertools mastery
    - idiom drills: exercises where I REWRITE clunky Java/JS-style code
      into idiomatic Python
10. **Type hints & static typing**: annotation syntax, typing
    fundamentals (Optional, Union with `|`, Literal, TypedDict,
    NamedTuple), generics & TypeVar, Protocol (structural typing),
    overloads, `mypy --strict`, gradual typing strategy — with explicit
    TypeScript-to-Python translation tables, since I already know TS
    types well.
11. **Async & concurrency**: asyncio (coroutines, await, tasks, gather),
    when async helps and when it doesn't, threads vs processes, the GIL,
    concurrent.futures, picking the right model (decision-flowchart
    required).
12. **Standard library power tools**: collections (Counter, defaultdict,
    deque), datetime & zoneinfo, re (regex), logging, argparse,
    subprocess, random/statistics, enum, os/sys essentials.
13. **Testing & quality deep-dive**: pytest for real — fixtures,
    parametrize, monkeypatch & mocking, tmp_path, coverage; ruff rules;
    property-based testing with hypothesis (taste); TDD workflow drills
    where I write the tests first.
14. **Frameworks & libraries (the important ones, each hands-on)**:
    - **pydantic** — validated models, settings; runtime validation vs
      static types
    - **httpx/requests** — HTTP clients, error handling, retries
      (against local fixtures, no live internet required)
    - **FastAPI** — routes, path/query/body params, dependency
      injection, tested entirely via `TestClient` (no running server)
    - **Typer** (or argparse recap) — real CLI apps
    - **SQLite + SQLAlchemy 2.0** — schema, sessions, queries
    - **numpy + pandas** — arrays, DataFrames, loading/cleaning/
      aggregating a small dataset
    Each library gets its own lesson section + exercises; keep coverage
    practical ("the 20% used 80% of the time"), not encyclopedic.
15. **Capstone projects (3, each with acceptance tests)**:
    - Capstone A: a Typer CLI task manager backed by SQLite/SQLAlchemy,
      fully type-hinted, mypy-strict clean.
    - Capstone B: a data pipeline — ingest a messy CSV/JSON dataset with
      pandas, clean it, aggregate it, emit a report; property-tested.
    - Capstone C: a small FastAPI service with pydantic models and an
      httpx-based client for it, tested end-to-end via TestClient.

## CLAUDE.md (instructor mode) must instruct you to:
- Act as my Python teacher: Socratic, encouraging, precise. My goal is
  zero-to-hero fluency and idiomatic, Pythonic style.
- Explain in the same easy-to-read style as the lessons; when I'm
  confused, draw an ad-hoc Mermaid diagram in your answer or in a
  scratch file rather than writing a wall of text.
- Answer any Python question with a small runnable example; when useful,
  create a scratch file in playground/ and run it with `uv run python
  playground/<file>.py` or `uv run pytest <file>`.
- When I ask to "check my answer", run the exercise's tests (and mypy
  where applicable), then review my code beyond the tests — style,
  idiomatic Python (PEP 8, Pythonic patterns), better alternatives — and
  explain WHY, not just what.
- Never reveal a solution outright; give escalating hints (concept →
  nudge → partial → full solution only on explicit request). Solutions
  live in `solutions/`; don't show them unless explicitly asked.
- When I pass a checkpoint, tick the box in ROADMAP.md yourself and
  suggest what's next.
- Quiz me periodically on earlier modules (spaced repetition), favoring
  topics from NOTES.md and each module's SUMMARY.md self-quiz.
- Track recurring mistakes in NOTES.md (date, module/exercise, the
  misconception — not just the wrong code — and the correction); remove
  entries I've clearly overcome.
- Since I know TypeScript: when I write "TypeScript-flavored" Python
  (e.g. reaching for classes where a dict or generator fits, verbose
  loops instead of comprehensions), point out the idiomatic Python way
  and log the habit in NOTES.md.

## Technical requirements
- Local repository of Markdown and Python files only — no web app to
  deploy, no server to keep running, no UI. Everything is consumed in
  VS Code and the terminal. FastAPI work runs through TestClient;
  capstones are CLI tools, libraries, or test-driven services.
- Python 3.12+, managed with `uv`; `pyproject.toml` defines the project
  and dev dependencies (pytest, mypy, ruff, plus module-14 libraries).
- Test runner UX must match the TS course:
  - `uv run pytest` — everything
  - `uv run pytest 03*` (or a small `scripts/test.py` wrapper so that
    "test module 3" and "test one exercise" are one short command —
    document the exact commands in README)
  - `uv run mypy <module>` for the typing modules; wire it into the
    module's test command so I can't pass on green tests with red types
- A freshly cloned repo must import cleanly everywhere (stubs raise
  NotImplementedError or return placeholders); failing tests are the
  only intended "red" — each failure is an unsolved exercise.
- Heavy dependencies (pandas, FastAPI, SQLAlchemy...) must be declared
  as an optional dependency group so modules 1–13 install fast.
- All Mermaid diagrams must use valid syntax that renders in VS Code's
  Markdown preview — verify each one renders before moving on.
- A `scripts/verify-solutions` equivalent must run each module's
  reference solutions against the same tests (and mypy where relevant)
  for course upkeep.

## Process
- Build the full structure and modules 1–4 completely first, then
  continue module by module. Verify the test commands behave correctly
  on the completed modules before moving on.
- Keep LESSON.md files tight; put depth into exercises and SUMMARY.md.
- Module 9 (Pythonic deep-dive) is the heart of the course — give it
  the same weight module 08 got in the TypeScript course (most
  exercises, a puzzle set, richest checkpoint).
