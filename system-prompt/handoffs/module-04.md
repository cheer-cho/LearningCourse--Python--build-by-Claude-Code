# Handoff: Module 04 — Collections

Build `04-collections/` in the course repo. Read `CONVENTIONS.md`
(same folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–03 (values, control flow, loops).
Functions beyond simple `def f(args): return ...` are module 05 — no
*args/**kwargs, closures, lambdas (except: `sorted(key=...)` may use a
plain named helper function, not lambda).

## LESSON.md outline
1. Why this exists: real data comes in groups; Python gives four
   workhorse containers.
2. REQUIRED diagram: decision flowchart "which container?" (ordered? →
   mutable? → key-value? → unique?) ending in list/tuple/dict/set.
3. Lists: index (incl. negative), append/insert/remove/pop, `in`,
   `len`, `sorted` vs `.sort()`.
4. Slicing — REQUIRED diagram: a string/list ruler showing
   `s[start:stop:step]` boundaries; reversal `[::-1]`; slice-copy.
5. Tuples & unpacking: immutability, `a, b = b, a`, starred
   `first, *rest = items`.
6. Dicts: literal, `d[k]` vs `d.get(k, default)`, add/update/delete,
   `.keys() / .values() / .items()`, looping patterns, counting idiom.
7. Sets: dedupe, `| & - ^`, membership speed (one sentence).
8. Comprehensions: list/dict/set, with `if` filter; when NOT to use one
   (side effects, too clever).
9. Copy vs alias — REQUIRED diagram: alias vs `list(x)` shallow copy vs
   `copy.deepcopy` for nested data.
10. Gotchas table: mutating while iterating, `dict[k]` KeyError,
    `()` needs a comma for 1-tuples, `{}` is a dict not a set.
11. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_lists.py` — `top_three(scores)` (sorted desc, slice),
  `insert_sorted(items, x)`, `without_negatives(nums)` (loop version —
  comprehensions come later in ex06).
- `ex02_tuples_unpacking.py` — `min_max(nums) -> (lo, hi)`;
  `head_tail(items)` via starred unpacking; `distance(p, q)` unpacking
  2-tuples.
- `ex03_dicts.py` — `phonebook` ops: `add_contact`, `lookup` with
  `.get` default, `count_words(text)` classic counting idiom.
- `ex04_sets.py` — `unique_tags(tags)`, `common_interests(a, b)`,
  `only_in_first(a, b)`, `has_duplicates(items)`.
- `ex05_slicing.py` — `every_other(s)`, `reversed_copy(items)`,
  `middle(items)` (drop first/last), `rotate(items, n)` via two slices.
- `ex06_comprehensions.py` — rewrite drills: each function contains a
  working loop version in a comment; student re-implements with a
  comprehension: `squares_of_evens`, `name_lengths` (dict comp),
  `first_letters` (set comp), `celsius_table` (dict comp over range).
- `ex07_records.py` — list of dicts ("records"): `emails_of(users)`,
  `find_user(users, name)` (loop + return early),
  `active_users(users)`, `average_age(users)`.
- `ex08_copy_alias.py` — prediction + fix drills: `broken_reset()`
  demonstrates an alias bug (returned "copy" mutates the original) —
  student fixes with a real copy; `deep_trap()` needs `copy.deepcopy`;
  prediction functions like module 02's ex07 but with nested lists.

## Checkpoint (`checkpoint_04.py`)
Gradebook: scores stored as `dict[str, list[int]]`.
- `add_score(book, student, score)` (create list on first score — no
  defaultdict yet)
- `averages(book)` -> dict comp of per-student mean
- `honor_roll(book, threshold)` -> sorted list of names via
  comprehension + sorted
- `class_stats(book)` -> tuple `(count, best_student, overall_avg)`
  using unpacking
Tests include the alias trap: `averages` must not mutate the book.

## SUMMARY.md
Cheat-sheet: container comparison table (list/tuple/dict/set: ordered,
mutable, syntax, use-for), slicing recipes, comprehension patterns,
copy-depth table. One mermaid mindmap. Self-quiz: 8 questions, answers
in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
