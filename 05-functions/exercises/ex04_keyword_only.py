# Scenario: forcing a clear call site with keyword-only and
# positional-only parameters. Concepts: bare `*` (keyword-only), bare
# `/` (positional-only), TypeError on a misused call.
# Run: uv run pytest 05-functions -k ex04


def make_user(name, *, admin=False, active=True):
    """Return a dict describing a user: {"name": ..., "admin": ...,
    "active": ...}. `admin` and `active` are keyword-only — the `*`
    forces callers to name them, so a call site is never ambiguous
    about which flag is which.

    make_user("Ada") -> {"name": "Ada", "admin": False, "active": True}
    make_user("Bo", admin=True) -> {"name": "Bo", "admin": True, "active": True}
    make_user("Cy", True)  # TypeError — admin must be passed by keyword
    """
    raise NotImplementedError


def divide(a, b, /):
    """Return `a / b` (true division). `a` and `b` are positional-only
    — the `/` forbids callers from naming them, since "a" and "b" are
    just placeholders, not meaningful keyword names.

    divide(6, 3) -> 2.0
    divide(a=6, b=3)  # TypeError — a, b must be positional
    """
    raise NotImplementedError
