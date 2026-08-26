# Reference solution for ex06_match — see exercises/ex06_match.py for
# the scenario.


def command(action: tuple) -> str:
    """Interpret a game-command tuple with match/case.

    action -> result
    ("go", "north") -> "moving north"
    ("go", "up") -> "can't go up"
    ("quit",) -> "goodbye"
    ("help",) -> "commands: go, quit, help, repeat"
    ("repeat", 3) -> "repeating 3 times"
    ("repeat", 0) -> "nothing to repeat"
    ("dance",) -> "unknown command"
    """
    match action:
        case ("go", "north" | "south" | "east" | "west" as direction):
            return f"moving {direction}"
        case ("go", other):
            return f"can't go {other}"
        case ("quit",):
            return "goodbye"
        case ("help",) | ("?",):
            return "commands: go, quit, help, repeat"
        case ("repeat", n) if n > 0:
            return f"repeating {n} times"
        case ("repeat", _):
            return "nothing to repeat"
        case _:
            return "unknown command"
