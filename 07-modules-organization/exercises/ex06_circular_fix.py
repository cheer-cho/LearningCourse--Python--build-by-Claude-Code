# Scenario: the shared-code module that fixes the circular import
# between `mod07_orders.py` and `mod07_customers.py` — read their
# headers for the full story. Concepts: circular imports, the standard
# fix (extract shared code into a third module both sides can depend
# on), and WHY it works.
# Run: uv run pytest 07-modules-organization -k ex06


def format_money(cents):
    """Format a non-negative integer number of `cents` as a dollar
    string like "$19.99".

    format_money(1999) -> "$19.99"
    format_money(0) -> "$0.00"
    format_money(5) -> "$0.05"
    """
    raise NotImplementedError


def pick_fix(options):
    """`options` is a dict[str, str] mapping short keys to descriptions
    of candidate fixes for a circular import between two modules A and
    B. Return the key whose description is the STANDARD fix —
    extracting the shared code both modules need into a new module
    neither A nor B has to import the other for. That description
    always contains the phrase "new module" or "third module". The
    other entries describe real but non-standard workarounds (e.g. a
    lazy import inside a function body, or merging both files into
    one) — don't match those.

    pick_fix({
        "delay": "move the import inside the function that needs it",
        "extract": "move the shared code both modules need into a new module",
        "merge": "combine both modules into a single file",
    }) -> "extract"
    """
    raise NotImplementedError
