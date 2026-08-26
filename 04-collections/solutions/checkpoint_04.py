def add_score(book: dict[str, list[int]], student: str, score: int) -> None:
    if student not in book:
        book[student] = []
    book[student].append(score)


def averages(book: dict[str, list[int]]) -> dict[str, float]:
    return {student: sum(scores) / len(scores) for student, scores in book.items()}


def honor_roll(book: dict[str, list[int]], threshold: float) -> list[str]:
    avgs = averages(book)
    return sorted(student for student, avg in avgs.items() if avg >= threshold)


def _average_value(item: tuple[str, float]) -> float:
    _student, average = item
    return average


def class_stats(book: dict[str, list[int]]) -> tuple[int, str, float]:
    count = len(book)
    avgs = averages(book)
    best_student, _best_avg = max(avgs.items(), key=_average_value)
    all_scores = [score for scores in book.values() for score in scores]
    overall_avg = sum(all_scores) / len(all_scores)
    return count, best_student, overall_avg
