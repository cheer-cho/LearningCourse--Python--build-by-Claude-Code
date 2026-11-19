"""Demo: !r in f-strings, the three ways to re-raise, and int()'s leniency.

Run: uv run python playground/06-errors-files/repr_and_from_none.py
"""

import traceback

# --- Part 1: !r --------------------------------------------------------
text = "4 2"
print(f"str : invalid age: {text}")  # uses str(text)
print(f"repr: invalid age: {text!r}")  # uses repr(text)

for tricky in ["", "  ", "42\n"]:
    print(f"  {tricky}  vs  {tricky!r}")


# --- Part 2: three ways to re-raise --------------------------------------
# The same parser, three endings. Watch how the traceback changes.


def parse_age_implicit(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"invalid age: {text!r}")  # no `from`


def parse_age_explicit(text: str) -> int:
    try:
        return int(text)
    except ValueError as err:
        raise ValueError(f"invalid age: {text!r}") from err  # keep the cause


def parse_age_clean(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"invalid age: {text!r}") from None  # hide the cause


test = [
    ("no `from`   -> 'During handling ... another exception occurred'", parse_age_implicit),
    ("from err    -> 'The above exception was the direct cause of ...'", parse_age_explicit),
    ("from None   -> only the new error", parse_age_clean),
]
for label, parser in test:
    print(f"\n===== {label} =====")
    try:
        parser("abc")
    except ValueError as exc:
        traceback.print_exc()
        # The three endings only differ in these three attributes:
        print(
            f"  __cause__={exc.__cause__!r}\n"
            f"  __context__={exc.__context__!r}\n"
            f"  __suppress_context__={exc.__suppress_context__}"
        )


# --- Part 3: int() accepts more than you'd think -------------------------
# Guess each result before running!
print("\n===== int() leniency =====")
for raw in ["42", " 42 ", "+42", "1_000", "٤٢", "4 2", "42.0", ""]:
    try:
        print(f"  int({raw!r:8}) -> {int(raw)}")
    except ValueError:
        print(f"  int({raw!r:8}) -> ValueError")

# Takeaway: whitespace, a leading +, underscores, and non-ASCII digits
# ("٤٢" is Arabic-Indic 42) all parse. For a strict form field, check
# first, e.g. `text.isascii() and text.isdigit()`, or use a regex.
