# Handoff: Module 03 — Control Flow

Build `03-control-flow/` in the course repo. Read `CONVENTIONS.md`
(same folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–02 (values, strings, f-strings, bools,
None). Lists/dicts are NOT taught yet (module 04): exercises may receive
a list only as "something to loop over" when the lesson shows that
pattern; no indexing tricks, slicing, comprehensions, dict methods.

## LESSON.md outline
1. Why this exists: programs must decide and repeat.
2. `if / elif / else` — REQUIRED diagram: flowchart of an elif chain.
3. Truthiness — REQUIRED diagram or table: exactly which values are
   falsy (`0, 0.0, "", None, False`, empty containers); everything else
   truthy.
4. `while` + the infinite-loop mistake; `for x in ...` + `range()`
   (start/stop/step); `enumerate` for counting while looping.
5. `break`, `continue`, and the loop `else` — diagram: flowchart showing
   when the else branch runs (loop finished without break).
6. `match/case` — literals, `|` alternatives, capture patterns, `_`
   fallback, guards (`case x if x < 0`). Keep to those; no class
   patterns yet.
7. Gotchas: `=` vs `==`, off-by-one in range, mutating the loop
   variable does nothing, forgetting `break` in while-input loops.
8. Try it now → exercises.

## Exercises (exactly 7)
- `ex01_branches.py` — `grade(score) -> "A".."F"` elif chain;
  `shipping_cost(subtotal, express)` with nested decision.
- `ex02_truthiness.py` — `first_truthy(a, b, c)` (return the first
  truthy of three, else None — no lists); `describe(value)` returning
  "empty"/"missing"/"present" distinguishing `""`, `None`, other.
- `ex03_while.py` — `countdown(n) -> "3-2-1-liftoff"` built with a
  while loop and string concatenation; `collatz_steps(n)` counting steps
  to reach 1; guard against n < 1 by returning None.
- `ex04_for_range.py` — `sum_multiples(limit, k)`; `factorial(n)`;
  `stripes(n)` building `"=-=-="`-style alternating string with
  `range` + `%`.
- `ex05_break_else.py` — `first_divisor(n)` (loop + break);
  `is_prime(n)` using for/else; `find_char(s, c)` returning index via
  enumerate + break, -1 if absent.
- `ex06_match.py` — `command(text)` parsing "quit"/"help"/"go north"
  style strings with match on `text.split()` results is too advanced —
  instead match on simple values and tuples: `ex06` matches
  `(verb, arg)` tuples: `("go", "north") -> ...`, `("quit",) -> ...`,
  guard `("repeat", n) if n > 0`. Provide the tuples directly as args.
- `ex07_fizzbuzz_plus.py` — classic `fizzbuzz(n)` returning the string
  for ONE number; `fizzbuzz_run(limit)` joining 1..limit with commas
  (for-loop + accumulator); nested-loop `times_table(n)` multi-line
  string.

## Checkpoint (`checkpoint_03.py`)
Number-guessing game engine as a pure function:
`guess_feedback(secret, guess, attempt, max_attempts)` returns one of
"correct!", "too high", "too low", "game over — the number was N"
(attempt >= max_attempts and wrong), with input validation via early
returns; plus `play_round(secret, guesses)` walking a list of guesses
with a for-loop + break/else and returning the transcript string. Tests
cover win, loss, out-of-range guesses.

## SUMMARY.md
Cheat-sheet: falsy-values table, range recipes, loop-else rule of thumb,
match/case syntax box. One mermaid mindmap. Self-quiz: 7 questions,
answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
