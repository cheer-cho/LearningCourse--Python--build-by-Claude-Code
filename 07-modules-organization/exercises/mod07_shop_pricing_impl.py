# Scenario: pricing logic for the tiny shop package `mod07_shop/`. This
# file backs `mod07_shop/pricing.py` — edit HERE, not the package file
# (see its header for why: verify_solutions can't overlay files nested
# inside a package). Concepts: the "_impl" pattern for testable package
# internals.
# Run: uv run pytest 07-modules-organization -k ex03


def discounted(price, percent_off):
    """Return `price` reduced by `percent_off` percent, rounded to 2
    decimal places.

    discounted(100, 25) -> 75.0
    discounted(50, 0) -> 50.0
    """
    raise NotImplementedError
