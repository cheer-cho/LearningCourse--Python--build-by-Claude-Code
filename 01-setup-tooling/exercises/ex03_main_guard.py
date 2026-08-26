"""This file prints its banner even when another file just IMPORTS it —
that's a bug. A script should only run its "do the work" code when it is
executed directly, not every time something imports it to reuse a function.

Fix it: guard the call to `main()` with `if __name__ == "__main__":` so
importing this module is silent, and running it (`uv run python
ex03_main_guard.py`) still prints the banner.

Run: uv run pytest 01-setup-tooling -k ex03
"""


def main():
    """Print a short banner introducing this module.

    Params:
        None.

    Returns:
        None. Prints "=== Setup & Tooling ===" to stdout.

    Examples:
        main() -> prints "=== Setup & Tooling ===", returns None.
    """
    print("=== Setup & Tooling ===")


main()
