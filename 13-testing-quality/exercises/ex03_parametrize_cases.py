# Scenario: a password-strength checker (already implemented, given
# below) needs a case table that exercises it thoroughly. Concepts:
# parametrize case tables, ids, covering edges on purpose.
# Run: uv run pytest 13-testing-quality -k ex03


def password_strength(pw: str) -> str:
    """Rate a password. Given — fully implemented, not part of the
    exercise. Read it to understand what cases matter.

    Rules, checked in order:
    - "" (empty string)          -> "empty"
    - len(pw) < 8                -> "too-short"
    - no digit anywhere in pw    -> "weak"
    - otherwise (len >= 8, has a digit) -> "strong"

    password_strength("") -> "empty"
    password_strength("abc") -> "too-short"
    password_strength("longenough") -> "weak"
    password_strength("longenough1") -> "strong"
    """
    if not pw:
        return "empty"
    if len(pw) < 8:
        return "too-short"
    if not any(char.isdigit() for char in pw):
        return "weak"
    return "strong"


# TODO: replace this placeholder with a real case table. Each tuple is
# (password, expected_rating) where expected_rating is whatever
# `password_strength` would return for that password.
#
# Your table must include at least one case from EACH of these
# categories (the meta-test checks for them by inspecting the inputs,
# not by trusting a label):
#   - empty:      pw == ""
#   - too-short:  0 < len(pw) < 8
#   - no-digit:   len(pw) >= 8 and no character in pw is a digit
#   - strong:     len(pw) >= 8 and at least one digit
#   - unicode:    at least one non-ASCII character anywhere in pw
# (a single password may satisfy more than one category at once)
STRENGTH_CASES: list[tuple[str, str]] = []
