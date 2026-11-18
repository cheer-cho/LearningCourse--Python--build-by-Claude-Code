def squares(n: int) -> list[int]:
    return [i * i for i in range(n)]


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}


def rectangle_info(width: float, height: float) -> tuple[float, float]:
    return width * height, 2 * (width + height)


def all_scores(*scores: int) -> tuple[int, ...]:  # any length
    return scores


def unique_tags(tags: list[str]) -> set[str]:
    return set(tags)


print(squares(4))
print(word_lengths(["hi", "hello"]))
print(rectangle_info(3, 4))
print(all_scores(90, 85, 77))
print(unique_tags(["py", "ts", "py"]))
