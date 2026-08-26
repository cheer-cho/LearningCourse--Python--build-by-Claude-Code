# Course-Wide Conventions (read this first)

You are one of several agents building a self-paced Python course. The
master spec is `../build-python-course.md` — read it. This file pins the
technical conventions every agent MUST follow so all modules fit together.

Style reference: the sibling TypeScript course at
`/home/acheer/study/TypeScript/Course-Created-By-Claude/` — especially
`02-basics/LESSON.md`, `02-basics/SUMMARY.md`, and its exercise files.
Match that tone: short sentences, diagram-first, encouraging, no walls of
text.

## Repo root
`/home/acheer/study/Python/Course-Created-By-Claude/`

## Toolchain
- Python 3.12+ (machine has 3.14), managed with `uv`.
- `pyproject.toml` at repo root; dev dependency group: pytest, ruff, mypy.
- Run everything through uv: `uv run pytest`, `uv run python ...`.

## Module folder anatomy
```
NN-module-name/
  LESSON.md            # diagram-first lesson (see spec for required flow)
  exercises/
    exNN_topic.py      # stub the student edits
    test_exNN_topic.py # pytest tests for it
  solutions/
    exNN_topic.py      # reference solution (same filename as stub)
    checkpoint_NN.py   # reference solution for the checkpoint
  checkpoint_NN.py     # graded checkpoint stub (module root)
  test_checkpoint_NN.py
  SUMMARY.md           # cheat-sheet + mermaid mindmap + 5–10 Q self-quiz
```

## Naming — IMPORTANT (import-collision rule)
Every Python file that gets imported must have a name that is **unique
across the whole course** and a valid Python identifier:
- Exercises: `ex01_<topic>.py` — the `<topic>` suffix makes it unique
  (e.g. `ex01_hello.py` in module 01, `ex01_numbers.py` in module 02).
- Checkpoints: `checkpoint_<NN>.py` (e.g. `checkpoint_03.py`).
The root `conftest.py` puts every module dir and `exercises/` dir on
`sys.path`, so tests import naturally: `from ex01_numbers import add`.
Never create two importable files with the same basename anywhere.

## Exercise file rules
- File header comment: 2–4 lines — scenario, concepts covered, and the
  exact command to run its tests. Never a numbered spec.
- Each function/class carries its own plain-English docstring directly
  on it: what it does, params, return, edge cases, and 1–3
  `input -> output` examples.
- Stub bodies: `raise NotImplementedError` (after the docstring), or a
  clearly-wrong placeholder when the exercise is "fix this code".
- Every stub file must import cleanly on a fresh clone
  (`python -m compileall` clean, no import-time errors). Failing tests
  are the ONLY intended red.
- Difficulty progresses ex01 → exNN from trivial to challenging.

## Test file rules
- pytest, plain `assert`, descriptive test names:
  `def test_greet_returns_hello_name():`.
- Import the exercise at module top: `from ex01_hello import greet`.
- Several small tests per exercise (happy path + edge cases), so a
  partially-correct answer gets partial feedback.
- Tests must be meaningful against the stub (all red on fresh clone) and
  all green against the reference solution.
- Use `pytest.raises` for error-behavior specs; `pytest.approx` for
  floats.

## Commands (already wired by the scaffold — do not redefine)
- `uv run pytest` — everything
- `uv run pytest 03-control-flow` — one module
- `uv run pytest 03-control-flow -k ex02` — one exercise
- `uv run python scripts/test.py 3 -k ex02` — same, by number
- `uv run python scripts/verify_solutions.py 03` — run the module's
  tests against the reference solutions (must exit 0)

## Mermaid rules
- Every LESSON.md: at least 2 diagrams; every SUMMARY.md: exactly one
  `mindmap`. Every diagram gets a one-line italic caption underneath
  starting with "*What to notice:*".
- Use only widely-supported syntax (flowchart TD/LR, graph, sequenceDiagram,
  mindmap). Quote node labels containing special characters:
  `A["like this (safe)"]`. No experimental diagram types.

## Definition of done for a module (verify ALL before finishing)
1. `uv run python -m compileall <module-dir>` — clean.
2. `uv run pytest <module-dir>` — collects with no errors; every failure
   is an unsolved exercise (NotImplementedError / wrong placeholder),
   never an import/collection error.
3. `uv run python scripts/verify_solutions.py <NN>` — exits 0 (all tests
   green against solutions).
4. `uv run ruff check <module-dir>` — clean (solutions and stubs).
5. LESSON.md and SUMMARY.md follow the spec flow and diagram rules.
6. You did NOT edit any file outside your module folder.

Report back (final message): module name, exercise list (one line each),
verification command outputs summarized, and any convention you had to
bend (should be none).
