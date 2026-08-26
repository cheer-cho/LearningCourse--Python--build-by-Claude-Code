# Scenario: input validators for a signup form. Concepts: `raise`,
# ValueError with a helpful message, validating before using a value.
# Run: uv run pytest 06-errors-files -k ex01


def require_positive(n):
    """Return `n` if it is strictly greater than 0.

    Otherwise raise ValueError with a message that includes the bad
    value, e.g. "expected a positive number, got -3".

    require_positive(5) -> 5
    require_positive(-3) -> raises ValueError("expected a positive number, got -3")
    require_positive(0) -> raises ValueError("expected a positive number, got 0")
    """
    raise NotImplementedError


def parse_age(text):
    """Parse `text` (a string) into a non-negative age (int).

    Raise ValueError if `text` isn't a valid integer at all (let the
    message explain what was received), and raise ValueError if it
    parses but is negative.

    parse_age("30") -> 30
    parse_age("abc") -> raises ValueError("invalid age: 'abc'")
    parse_age("-5") -> raises ValueError("age cannot be negative: -5")
    """
    raise NotImplementedError
