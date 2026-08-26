# Handoff: Module 01 — Setup & Tooling

Build `01-setup-tooling/` in the course repo. Read
`CONVENTIONS.md` (same folder) and the master spec first; follow the
module anatomy exactly. You own ONLY this folder.

Audience: absolute beginner — this is their first contact with Python.
Nothing may assume knowledge of functions/loops beyond what the lesson
itself shows; keep required code trivial (single return statements).

## LESSON.md outline
1. Why this exists: you need a working toolbox before learning the
   language; meet your three tools — `uv` (runs everything), pytest
   (tells you when an exercise is solved), the traceback (tells you
   what went wrong).
2. Diagram: flowchart of the edit → `uv run pytest` → red/green loop.
3. Running Python three ways: REPL (`uv run python`), a script
   (`uv run python file.py`), and through pytest. Tiny example each.
4. Anatomy of a traceback — diagram (flowchart or annotated flow):
   read bottom-up (error type → message → the line, then the call
   chain).
5. `if __name__ == "__main__":` in 4 sentences + small diagram
   (imported vs run directly).
6. Gotchas: `python` vs `python3` vs `uv run python`; forgetting to
   save before re-running; indentation is syntax.
7. Try it now → exercises.

## Exercises (exactly 4)
- `ex01_hello.py` — `greet(name)` returns `"Hello, <name>!"`. Stub has
  the docstring and `raise NotImplementedError`. Teaches: the red/green
  loop itself.
- `ex02_tracebacks.py` — three tiny broken functions (NameError from a
  typo'd variable, TypeError from `"1" + 1`, ZeroDivisionError from a
  missing guard); comments show the traceback each one produces and the
  student fixes the code. Tests assert corrected behavior.
- `ex03_main_guard.py` — a `main()` that prints a banner, guarded by
  `if __name__ == "__main__":`. Stub has the guard MISSING so importing
  prints (bad); test imports the module capturing stdout (capsys at
  import via importlib.reload or subprocess `python -c "import ..."`)
  and asserts silence, plus `main()` output when called.
- `ex04_ruff_cleanup.py` — a working but messy function (unused import,
  bad spacing, unused variable, shadowed builtin like `list = ...`).
  Student must keep behavior identical and make ruff happy. Test checks
  behavior AND runs `ruff check` on the file via `subprocess`
  (`sys.executable -m ruff` won't work; use `["uv", "run", "ruff",
  "check", str(path)]`) asserting exit 0.

## Checkpoint (`checkpoint_01.py`)
"About-me card": `build_card(name, age)` returns a small multi-line
string using both values; `main()` prints it; main-guard present; file
ruff-clean (test runs ruff on it like ex04). Combines everything above.

## SUMMARY.md
Cheat-sheet: commands table (run script / REPL / test everything / test
this module / one exercise), traceback-reading recipe, main-guard
snippet. One mermaid mindmap. Self-quiz: 5 questions with answers in a
collapsed `<details>` block.

Finish with every "Definition of done" check from CONVENTIONS.md.
