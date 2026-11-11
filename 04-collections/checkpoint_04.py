# Checkpoint 04 — Gradebook
#
# A gradebook stores every student's scores as a dict[str, list[int]]:
# {"Ada": [90, 85], "Bo": [70]}. Build the four operations below.
# This combines dicts, comprehensions, sorted(), and tuple unpacking —
# everything from this module.
# Run: uv run pytest 04-collections -k checkpoint


def add_score(book: dict[str, list[int]], student: str, score: int) -> None:
    """Record `score` for `student` in `book`, mutating `book` in place.

    If `student` has no scores yet, create their list first. Returns
    nothing — this function only mutates `book`.

    book = {}
    add_score(book, "Ada", 90)  -> book is now {"Ada": [90]}
    add_score(book, "Ada", 85)  -> book is now {"Ada": [90, 85]}
    """
    student_score = book.get(student, [])
    student_score.append(score)
    book[student] = student_score


def averages(book: dict[str, list[int]]) -> dict[str, float]:
    """Return a new dict mapping each student to the mean of their
    scores. Must NOT modify `book` — every list in `book` stays exactly
    as it was, in the same order, before and after the call.

    averages({"Ada": [90, 80], "Bo": [70]}) -> {"Ada": 85.0, "Bo": 70.0}
    """
    return {student: sum(scores) / len(scores) for student, scores in book.items()}


def honor_roll(book: dict[str, list[int]], threshold: float) -> list[str]:
    """Return the names of every student whose average score is >=
    `threshold`, sorted alphabetically. Build the result with a
    comprehension plus `sorted`.

    honor_roll({"Ada": [95, 91], "Bo": [60]}, 90) -> ["Ada"]
    """
    return sorted([student for student, avg_score in averages(book).items() if avg_score >= threshold])


def _average_scores(item: dict[str, float]) -> float:
    _, avg_score = item
    return avg_score


def class_stats(book: dict[str, list[int]]) -> tuple[int, str, float]:
    """Return `(count, best_student, overall_avg)`:
    - `count`: number of students in `book`.
    - `best_student`: the name with the highest average score.
    - `overall_avg`: the mean of EVERY individual score in `book`
      (not the average of the per-student averages).

    `book` has at least one student, and every student has at least one
    score.

    class_stats({"Ada": [100], "Bo": [50, 50]}) -> (2, "Ada", 66.66666666666667)
    """
    count = len(book)
    avgs = averages(book)
    best_student, _ = max(avgs.items(), key=_average_scores)
    all_scores = [score for scores in book.values() for score in scores]
    overall_avg = sum(all_scores) / len(all_scores)

    return (count, best_student, overall_avg)
