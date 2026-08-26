# Python Mastery Course

A complete, self-paced Python course you study **inside VS Code**, with
Claude Code acting as your personal instructor. It is hands-on first: you
learn by writing code and making tests pass, not by reading long documents.

## What you'll get out of it

Full fluency in Python, zero to hero — every piece of syntax, the standard
library, idiomatic "Pythonic" style, static typing with type hints, and the
important frameworks and libraries used in real work (pydantic, httpx,
FastAPI, SQLAlchemy, pandas, and more).

## Prerequisites

- None. No prior programming experience needed.
- [Python](https://www.python.org) 3.12 or newer.
- [uv](https://docs.astral.sh/uv/) — installs and manages everything else.
- VS Code.
- If you already know TypeScript, occasional "coming from TypeScript" notes
  will speed things up, but they're never required to follow a lesson.

## Setup

```bash
uv sync
uv run pytest       # run everything (expect failures — those are your TODOs!)
```

No `uv`? A plain venv works too:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Enable Mermaid diagrams in VS Code

Lessons use Mermaid diagrams heavily. To see them rendered:

1. Open the Extensions panel (`Ctrl+Shift+X`).
2. Install **"Markdown Preview Mermaid Support"** (`bierner.markdown-mermaid`).
3. Open any `LESSON.md` and press `Ctrl+Shift+V` (or `Ctrl+K V` for side-by-side).

## How to use this course

1. Open [ROADMAP.md](./ROADMAP.md) — it is your progress tracker.
2. Enter the current module folder (start with `01-setup-tooling/`).
3. Read `LESSON.md` — short, diagram-first. 5–10 minutes.
4. Work through `exercises/ex01_*.py`, `ex02_*.py`, … in order. Each file
   has a short header comment and a docstring per function/class with
   input → output examples.
5. Check yourself: `uv run python scripts/test.py 01` (replace `01` with
   the module number).
6. Finish the module with `checkpoint_NN.py` — passing its tests means the
   module is complete. Your instructor will tick it off in the roadmap.
7. Skim `SUMMARY.md` as a cheat-sheet and take its self-quiz.

### How the tests work

A freshly cloned repo imports cleanly everywhere, but most tests fail —
each failure is an exercise you haven't solved yet. That's the point: your
job is to turn the module you're working on green. From module 10 (type
hints) onward, exercises are also checked with `mypy --strict`; a wrong or
missing annotation fails the check, never silently passes.

### Commands

| Command | Does |
| --- | --- |
| `uv run pytest` | everything |
| `uv run pytest 03-control-flow` | one module |
| `uv run pytest 03-control-flow -k ex02` | one exercise |
| `uv run python scripts/test.py 3 -k ex02` | same, by module number |
| `uv run python scripts/verify_solutions.py 03` | run module 03's tests against the reference solutions (course upkeep) |
| `uv run ruff check .` | lint |
| `uv run mypy 10-typing` | type-check a module (from module 10 on) |

## Working with your instructor

Open this repo in Claude Code. [CLAUDE.md](./CLAUDE.md) turns Claude into
your Python teacher. Useful things to say:

- *"Explain this lesson to me"* / *"I don't get decorators, draw it"*
- *"Check my answer for ex03"* — runs the tests **and** reviews your style
- *"Give me a hint"* — you get escalating hints, never the full solution
  (unless you explicitly ask for it)
- *"Quiz me"* — spaced-repetition review of earlier modules

## Repository layout

```
01-setup-tooling/     one folder per module
  LESSON.md           concise, diagram-first explanation
  exercises/           exNN_topic.py, test_exNN_topic.py, ...
  solutions/           reference solutions — don't peek, ask for hints instead
  checkpoint_NN.py     graded checkpoint; passing it = module complete
  SUMMARY.md           cheat-sheet + mindmap + self-quiz
playground/            scratch space for experiments with your instructor
scripts/               test.py, verify_solutions.py
NOTES.md               your instructor's log of your recurring mistakes
ROADMAP.md             full learning path + progress checkboxes
```
