# Scenario: a phonebook app and a word-frequency counter. Concepts: dict
# literals, d[k] vs d.get(k, default), adding/updating/deleting keys,
# .items(), the counting idiom.
# Run: uv run pytest 04-collections -k ex03


def add_contact(phonebook: dict[str, str], name: str, number: str) -> dict[str, str]:
    """Add `name` -> `number` to `phonebook` (overwriting if `name` is
    already present), then return `phonebook`.

    add_contact({}, "Ada", "555-0100") -> {"Ada": "555-0100"}
    """
    raise NotImplementedError


def lookup(phonebook: dict[str, str], name: str) -> str:
    """Return the phone number for `name`, or "unknown" if `name` isn't
    in `phonebook`. Use `.get` with a default — no `if`/`in` check.

    lookup({"Ada": "555-0100"}, "Ada") -> "555-0100"
    lookup({"Ada": "555-0100"}, "Grace") -> "unknown"
    """
    raise NotImplementedError


def count_words(text: str) -> dict[str, int]:
    """Return a dict mapping each word in `text` to how many times it
    appears. Split on whitespace with `.split()`; words are compared
    exactly as they appear (no case-folding, no punctuation stripping).

    count_words("a b a c b a") -> {"a": 3, "b": 2, "c": 1}
    count_words("") -> {}
    """
    raise NotImplementedError
