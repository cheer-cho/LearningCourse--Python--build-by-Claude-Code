# Handoff: Repo Scaffold

Build the skeleton of the Python course repo at
`/home/acheer/study/Python/Course-Created-By-Claude/`. Other agents will
build modules on top of this — get the plumbing right and verified.

Read first: `system-prompt/build-python-course.md` (master spec) and
`system-prompt/handoffs/CONVENTIONS.md`. Style-match the TypeScript
course at `/home/acheer/study/TypeScript/Course-Created-By-Claude/`
(its README.md, ROADMAP.md, CLAUDE.md are your templates — adapt, don't
copy blindly).

## Deliverables

### 1. Project plumbing
- `uv init`-style `pyproject.toml`: project name `python-mastery-course`,
  `requires-python = ">=3.12"`, dev group with pytest, ruff, mypy.
  Pytest config in `[tool.pytest.ini_options]`:
  `addopts = "--import-mode=importlib"`, and exclude `.verify`,
  `playground`, `solutions`, `system-prompt` from collection
  (`norecursedirs`). Ruff config: line-length 100, target py312.
- Run `uv sync` so `uv.lock` exists and tools work.
- `.gitignore` (venv, __pycache__, .pytest_cache, .ruff_cache, .verify/).
- Root `conftest.py`: at import, glob `[0-9][0-9]-*` module dirs under
  the repo root and insert each module dir AND its `exercises/` subdir
  into `sys.path`, so tests can do `from ex01_hello import greet` and
  `from checkpoint_02 import ...`. (Unique-filename rule in CONVENTIONS
  makes this safe.)
- `scripts/test.py`: maps a module number to its folder and execs
  pytest with any extra args passed through
  (`uv run python scripts/test.py 3 -k ex02`). Friendly error for an
  unknown module number.
- `scripts/verify_solutions.py`: for a given `NN` (or all modules if no
  arg): copy that module folder into `.verify/NN-*/`, overwrite each
  `exercises/exNN_*.py` stub and root `checkpoint_NN.py` with the
  same-named file from `solutions/`, copy the root `conftest.py` in (so
  imports resolve inside `.verify`), run pytest on the copy, exit
  non-zero on any failure. Print a clear PASS/FAIL per module.
- `playground/README.md` — one paragraph: scratch space, how to run
  files with `uv run python playground/<f>.py`.
- `NOTES.md` — header + "no entries yet" placeholder, format documented
  (date, module/exercise, misconception, correction).

### 2. README.md
Adapt the TS course README to Python/uv/pytest: overview, zero
prerequisites (no prior programming needed), setup (`uv sync`,
`uv run pytest` — expect failures, those are the TODOs), Mermaid VS Code
extension instructions, how-to-use flow, the commands table, repo layout
tree. Mention fallback setup without uv (`python -m venv` + `pip install
-e ".[dev]"` or requirements — keep it to 3 lines).

### 3. ROADMAP.md
Opens with ONE mermaid flowchart of the whole course: 15 module nodes,
checkpoint diamonds between them, module 09 highlighted as the heart,
module 15 as the finish. Caption line under it. Then a progress checklist
section per module (Lesson read / Exercises exNN–exNN / ✦ Checkpoint N
passed). Use exactly these module names, folder names, and exercise
counts:

| NN | Folder | Title | Exercises |
|----|--------|-------|-----------|
| 01 | 01-setup-tooling | Setup & Tooling | ex01–ex04 |
| 02 | 02-values-variables | Values & Variables | ex01–ex08 |
| 03 | 03-control-flow | Control Flow | ex01–ex07 |
| 04 | 04-collections | Collections | ex01–ex08 |
| 05 | 05-functions | Functions | ex01–ex08 |
| 06 | 06-errors-files | Errors, Files & Context Managers | ex01–ex08 |
| 07 | 07-modules-organization | Modules & Organization | ex01–ex06 |
| 08 | 08-oop | Object-Oriented Python | ex01–ex08 |
| 09 | 09-pythonic-deep-dive | Pythonic Deep-Dive | ex01–ex12 (+ idiom drills) |
| 10 | 10-typing | Type Hints & Static Typing | ex01–ex08 |
| 11 | 11-async-concurrency | Async & Concurrency | ex01–ex07 |
| 12 | 12-stdlib-power-tools | Standard Library Power Tools | ex01–ex08 |
| 13 | 13-testing-quality | Testing & Quality | ex01–ex07 |
| 14 | 14-frameworks-libraries | Frameworks & Libraries | ex01–ex10 |
| 15 | 15-capstones | Capstone Projects | A / B / C |

Module 15's checklist lists the three capstones from the master spec
instead of exercises.

### 4. CLAUDE.md (instructor mode)
Adapt the TS course CLAUDE.md per the "CLAUDE.md (instructor mode)"
section of the master spec — Python commands (`uv run pytest ...`,
`uv run python scripts/verify_solutions.py NN`), Pythonic-style coaching,
the TypeScript-habits note, hint escalation, roadmap tick-off, spaced
repetition, NOTES.md rules, and course-maintenance rules referencing
CONVENTIONS.md.

### 5. Smoke-test fixture, then git
To prove the plumbing, create a throwaway module `99-smoke/` with one
exercise `exercises/ex01_smoke.py` (+ test) and a solution, following
CONVENTIONS. Verify:
- `uv run pytest` collects it and the test fails with NotImplementedError
- `uv run python scripts/test.py 99` works
- `uv run python scripts/verify_solutions.py 99` exits 0
- `uv run ruff check .` clean
Then DELETE `99-smoke/` entirely, `git init`, and make one commit
"scaffold course repository" (plain message, no attribution lines, no
Co-Authored-By).

## Do NOT
- Do not create any real module folders (01–15) — other agents own those.
- Do not add content beyond this list.

Report back: files created, output of each smoke-test command
(summarized), anything you changed relative to this handoff.
