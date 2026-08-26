# Scenario: a text-adventure engine needs to interpret command tuples.
# Covers: match/case with literals, | alternatives, capture patterns,
# `_` fallback, and a guard clause.
# Run: uv run pytest 03-control-flow -k ex06


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
    raise NotImplementedError
