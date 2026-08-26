def squares_of_evens(nums: list[int]) -> list[int]:
    return [n * n for n in nums if n % 2 == 0]


def name_lengths(names: list[str]) -> dict[str, int]:
    return {name: len(name) for name in names}


def first_letters(words: list[str]) -> set[str]:
    return {word[0] for word in words if word}


def celsius_table(start: int, stop: int) -> dict[int, float]:
    return {c: c * 9 / 5 + 32 for c in range(start, stop)}
