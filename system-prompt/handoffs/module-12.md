# Handoff: Module 12 — Standard Library Power Tools

Build `12-stdlib-power-tools/` in the course repo. Read
`CONVENTIONS.md` (same folder) and the master spec first. You own ONLY
this folder.

Audience: completed modules 01–11. Solutions lightly type-hinted from
here on. Everything must be deterministic: seed all randomness with
injected `random.Random(seed)`, use fixed datetimes (never `now()` in
assertions — pass timestamps in), tmp_path for any file.

## LESSON.md outline
1. Why this exists: before reaching for pip, check the batteries —
   REQUIRED mindmap diagram of the stdlib areas this module tours.
2. collections: Counter (counting/top-n), defaultdict (grouping),
   deque (windows/rotation) — micro-example each.
3. datetime: aware vs naive — REQUIRED diagram (naive vs aware, UTC
   store / local display rule); strptime/strftime table of common
   codes; timedelta math; zoneinfo.
4. re: raw strings, the 6 metacharacters you actually need, groups,
   `findall`/`search`/`sub`; "regex is a last resort for parsing" note.
5. enum: Enum, auto, value lookup, match on enums.
6. logging: logger/handler/level model in one diagram, getLogger(name),
   why not print.
7. argparse: parser → add_argument → parse_args(argv); testable CLIs
   take argv as a parameter.
8. subprocess: run, capture_output, returncode, check=False.
9. random (seeded instances) + statistics (mean/median/stdev).
10. Gotchas: naive/aware mixing raises, regex greedy vs lazy, mutable
    module-level state in logging, forgetting raw strings.
11. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_collections.py` — `top_words(text, n)` (Counter.most_common
  with deterministic tie-handling — sort), `group_by_first_letter
  (names)` (defaultdict(list)), `LastN` recent-items keeper (deque
  maxlen).
- `ex02_datetime.py` — `parse_iso_date(text)`, `days_between(a, b)`,
  `format_friendly(dt)` -> "Tue 26 Aug 2026", `to_utc(dt_string, tz)`
  using zoneinfo (pick tz names that exist everywhere: "UTC",
  "Europe/Paris", "Asia/Bangkok").
- `ex03_regex.py` — `extract_emails(text)`, `redact_phones(text)`
  (sub), `parse_log_line(line)` with NAMED groups → dict
  (level/timestamp/message).
- `ex04_enum.py` — `Status(Enum)` (PENDING/ACTIVE/CLOSED),
  `from_label(text)` (case-insensitive, ValueError otherwise),
  `next_status(s)` via match, `is_terminal(s)`.
- `ex05_logging.py` — `make_logger(name, level, stream)` building an
  isolated logger writing to an injected StringIO with a fixed format
  (no root-logger pollution: propagate=False, clear handlers);
  `audit(logger, event, ok)` logging at info/error appropriately;
  tests read the StringIO.
- `ex06_argparse.py` — `build_parser()` for a `notes` CLI: positional
  `action` (add/list), `--tag` repeatable (append), `--limit` int with
  default; `run(argv)` dispatching to given pure helpers and returning
  output text. Tests drive `run(["add", "milk", "--tag", "shop"])`
  etc.; also assert `--help` exits SystemExit cleanly.
- `ex07_subprocess.py` — `python_version()` running
  `[sys.executable, "--version"]` capturing stdout;
  `run_snippet(code)` via `-c` returning (returncode, stdout, stderr);
  `safe_run(cmd)` never raising, returning a result dict.
- `ex08_random_stats.py` — `sample_scores(rng, n)` from an injected
  Random; `summarize(nums)` -> dict with mean/median/stdev (statistics;
  stdev None when n < 2); `weighted_pick(rng, options)`.

## Checkpoint (`checkpoint_12.py`)
Log-file analyzer: given text of synthetic log lines
("2026-08-26T10:00:00 ERROR Payment failed" style):
`parse_line` (regex named groups + datetime + Status-like level enum),
`filter_entries(entries, *, level=None, since=None)`,
`report(entries, top=3)` using Counter → formatted string, and
`run(argv)` wiring an argparse front-end over an input file
(tmp_path in tests). Ties every tool in the module together.

## SUMMARY.md
Cheat-sheet: Counter/defaultdict/deque one-liners, strftime code
table, regex mini-reference, logging recipe, argparse skeleton,
subprocess.run recipe. One mermaid mindmap. Self-quiz: 8 questions,
answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
