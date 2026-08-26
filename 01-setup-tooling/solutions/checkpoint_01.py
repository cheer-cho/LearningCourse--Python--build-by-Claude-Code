"""Reference solution for checkpoint_01. Not imported by tests directly —
scripts/verify_solutions.py overlays this onto the checkpoint stub.
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
    return f"Name: {name}\nAge: {age}"


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
