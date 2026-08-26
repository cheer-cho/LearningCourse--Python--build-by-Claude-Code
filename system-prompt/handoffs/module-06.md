# Handoff: Module 06 — Errors, Files & Context Managers

Build `06-errors-files/` in the course repo. Read `CONVENTIONS.md` (same
folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–05. No classes yet beyond subclassing
`Exception` (module 08 covers OOP) — custom exceptions here are
`class FooError(Exception): pass` or with a simple `__init__` storing
attributes, explained line by line in the lesson. No type hints.

All file-touching tests MUST use pytest's `tmp_path` fixture — never
write into the repo.

## LESSON.md outline
1. Why this exists: things go wrong; Python's answer is exceptions, not
   error codes.
2. REQUIRED diagram: flowchart of `try → except → else → finally`
   (which branch runs when; finally always).
3. REQUIRED diagram: small graph of the exception hierarchy
   (BaseException → Exception → ValueError/TypeError/KeyError/OSError…)
   — catch the most specific type you can.
4. `raise`, custom exceptions, and chaining (`raise X from e`).
5. EAFP vs LBYL — comparison table + one-sentence rule of thumb.
6. `with` — REQUIRED diagram: enter → body → exit-even-on-error; why
   it replaces try/finally for cleanup.
7. pathlib essentials: `Path`, `/` joining, `exists`, `glob`, `stem`,
   `suffix`, `read_text`, `write_text`.
8. json and csv in 10 lines each.
9. Gotchas: bare `except:`, swallowing exceptions silently, forgetting
   encoding, `except Exception as e` scoping.
10. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_raising.py` — validators: `require_positive(n)`,
  `parse_age(text)` (ValueError with helpful messages — tests assert
  message content with `pytest.raises(..., match=...)`).
- `ex02_catching.py` — `safe_divide(a, b)` (None on ZeroDivisionError),
  `int_or_default(text, default)` EAFP, `first_working(funcs)` trying
  callables until one doesn't raise.
- `ex03_else_finally.py` — `guarded_process(data, log)` appending
  "start"/"error"/"ok"/"cleanup" to a log list from the right branches;
  tests assert exact event order for success and failure paths.
- `ex04_custom_exceptions.py` — `InsufficientFunds(Exception)` carrying
  `needed` and `available` attributes; `withdraw(balance, amount)`
  raising it; test asserts the attributes.
- `ex05_chaining.py` — `load_setting(raw, key)` catching
  KeyError/ValueError and re-raising a custom `ConfigError from e`;
  test asserts `__cause__` is set.
- `ex06_pathlib.py` — `build_report_path(base, name)`,
  `find_py_files(folder)` (glob, sorted), `swap_suffix(path, new)`;
  tests build trees in tmp_path.
- `ex07_files.py` — `write_lines(path, lines)`, `count_words(path)`,
  `append_log(path, message)` (creates file if missing), all with
  `with` + encoding="utf-8".
- `ex08_json_csv.py` — `save_config(path, config)` / `load_config(path)`
  JSON roundtrip; `read_inventory(path)` parsing a CSV into a list of
  dicts with int quantities.

## Checkpoint (`checkpoint_06.py`)
Contacts file store: `ContactError(Exception)`;
`load_contacts(path)` — missing file returns `{}` (EAFP), corrupt JSON
raises `ContactError from e`; `save_contacts(path, contacts)`;
`add_contact(path, name, email)` load-modify-save rejecting duplicates
via ContactError. Tests use tmp_path, cover the corrupt-file chain and
the duplicate path.

## SUMMARY.md
Cheat-sheet: try/except/else/finally skeleton, exception-hierarchy
mini-tree, EAFP-vs-LBYL table, pathlib one-liners, json/csv snippets.
One mermaid mindmap. Self-quiz: 8 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
