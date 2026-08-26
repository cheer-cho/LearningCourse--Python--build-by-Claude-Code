"""Checkpoint 1 — About-me card.

Combines everything from this module: a function with a docstring, the
red/green loop, and the main-guard pattern. Passing this file's tests
completes module 01.

Run: uv run pytest 01-setup-tooling -k checkpoint
"""


def build_card(name, age):
    """Return a small "About Me" card as a multi-line string.

    Params:
        name (str): the person's name.
        age (int): the person's age.

    Returns:
        str: two lines joined by "\\n": "Name: <name>" then "Age: <age>".

    Examples:
        build_card("Ada", 28) -> "Name: Ada\\nAge: 28"
    """
    raise NotImplementedError


def main():
    """Print an About Me card for a sample person.

    Params:
        None.

    Returns:
        None. Prints the card built by `build_card("Ada", 28)`.
    """
    print(build_card("Ada", 28))


if __name__ == "__main__":
    main()
