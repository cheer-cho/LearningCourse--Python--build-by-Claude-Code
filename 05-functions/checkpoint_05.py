# Checkpoint 05 — Text-stats toolkit
#
# Three small tools that lean on everything from this module: default
# parameters with the None-sentinel, keyword-only parameters, closures,
# and *args. Build them one at a time.
# Run: uv run pytest 05-functions -k checkpoint


def word_stats(text, *, min_length=1, stop_words=None):
    """Return a dict mapping each word in `text` to how many times it
    appears, after lower-casing and stripping the punctuation
    `.,!?;:"'` from each word's edges.

    - `min_length` (keyword-only): skip words shorter than this.
    - `stop_words` (keyword-only): a set of words to exclude entirely.
      Defaults to `None`, meaning "exclude nothing" — use the
      None-sentinel pattern so no mutable default is shared across
      calls.

    word_stats("the cat sat on the mat")
        -> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
    word_stats("a bb ccc", min_length=2) -> {"bb": 1, "ccc": 1}
    word_stats("the cat sat", stop_words={"the"}) -> {"cat": 1, "sat": 1}
    word_stats("Cat, cat! dog.") -> {"cat": 2, "dog": 1}
    """
    raise NotImplementedError


def make_formatter(prefix, suffix=""):
    """Return a function of one argument, `value`, that returns
    f"{prefix}{value}{suffix}". A closure factory — each call to
    `make_formatter` must produce an independent formatter.

    bracket = make_formatter("[", "]")
    bracket("info") -> "[info]"

    shout = make_formatter(">> ")
    shout("hello") -> ">> hello"
    """
    raise NotImplementedError


def apply_all(value, *funcs):
    """Thread `value` through every function in `funcs`, left to right
    — the result of each call becomes the input to the next — and
    return the final result. With no `funcs`, return `value` unchanged.

    apply_all(3, lambda x: x + 1, lambda x: x * 2) -> 8
    apply_all(5) -> 5
    """
    raise NotImplementedError
