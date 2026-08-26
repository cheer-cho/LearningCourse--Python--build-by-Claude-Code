# ✦ CHECKPOINT 3 — Control Flow
#
# A number-guessing game engine, as pure functions. Combines: if/elif/
# else, early-return validation, and for/break/else. Each function
# carries its own scenario below.
#
# Passing `uv run pytest 03-control-flow` completes this module.

MIN_GUESS = 1
MAX_GUESS = 100


def guess_feedback(secret: int, guess: int, attempt: int, max_attempts: int) -> str:
    """Give feedback for one guess in a number-guessing game.

    Validates guess is in range [MIN_GUESS, MAX_GUESS] first (early
    return). Then checks for a win. Then checks whether this was the
    last allowed attempt and it was wrong (game over). Otherwise reports
    which direction to adjust.

    secret, guess, attempt, max_attempts -> result
    42, 42, 1, 5 -> "correct!"
    42, 50, 1, 5 -> "too high"
    42, 10, 1, 5 -> "too low"
    42, 10, 5, 5 -> "game over — the number was 42"
    42, 500, 1, 5 -> "out of range"
    """
    raise NotImplementedError


def play_round(secret: int, guesses) -> str:
    """Walk a fixed sequence of guesses through one game round.

    guesses is a list of ints, tried in order as attempts 1, 2, 3, ...
    (max_attempts is the number of guesses given). Breaks the moment a
    guess is correct. The for/else covers the "never broke out" case —
    either the round ran out of guesses, or no guesses were given at
    all — and makes sure the transcript never comes back empty.

    secret, guesses -> result
    42, [10, 42] -> "attempt 1: guess 10 -> too low\\nattempt 2: guess 42 -> correct!"
    """
    raise NotImplementedError
