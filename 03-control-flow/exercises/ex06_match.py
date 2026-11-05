# Scenario: a text-adventure engine needs to interpret command tuples.
# Covers: match/case with literals, | alternatives, capture patterns,
# `_` fallback, and a guard clause.
# Run: uv run pytest 03-control-flow -k ex06

DIRECTIONS = ("north", "south", "east", "west")

def command(action: tuple) -> str:
    """Interpret a game-command tuple with match/case.

    action -> result
    ("go", "north") -> "moving north"   (valid: north, south, east, west)
    ("go", "up") -> "can't go up"       (any other direction)
    ("quit",) -> "goodbye"
    ("help",) -> "commands: go, quit, help, repeat"
    ("?",) -> "commands: go, quit, help, repeat"   (alias for help)
    ("repeat", 3) -> "repeating 3 times"
    ("repeat", 0) -> "nothing to repeat"
    ("dance",) -> "unknown command"
    """
    match action:
        case ("go", direction) if direction in DIRECTIONS:
            return f"moving {direction}"

        case ("go", direction):
            return f"can't go {direction}"

        case ("quit",):
            return "goodbye"

        case ("help",) | ("?",):
            return "commands: go, quit, help, repeat"

        case ("repeat", times) if times > 0:
            return f"repeating {times} times"

        case ("repeat", _):
            return "nothing to repeat"

        case _:
            return "unknown command"
