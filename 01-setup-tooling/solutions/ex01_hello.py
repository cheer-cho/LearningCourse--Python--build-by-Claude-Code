"""Reference solution for ex01_hello. Not imported by tests directly —
scripts/verify_solutions.py overlays this onto the exercise stub.
"""


def greet(name):
    """Return a friendly greeting for `name`.

    Params:
        name (str): the person to greet.

    Returns:
        str: "Hello, <name>!".

    Examples:
        greet("Ada") -> "Hello, Ada!"
        greet("Grace") -> "Hello, Grace!"
    """
    return f"Hello, {name}!"
