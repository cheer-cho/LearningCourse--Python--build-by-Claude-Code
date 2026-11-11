# Scenario: rewrite drills. Each function already has a working loop
# version in a comment above its body — replace `raise NotImplementedError`
# with the equivalent one-line comprehension. Concepts: list/dict/set
# comprehensions with an `if` filter.
# Run: uv run pytest 04-collections -k ex06


def squares_of_evens(nums: list[int]) -> list[int]:
    """Return the square of every even number in `nums`, in order.

    # loop version:
    # result = []
    # for n in nums:
    #     if n % 2 == 0:
    #         result.append(n * n)
    # return result

    squares_of_evens([1, 2, 3, 4]) -> [4, 16]
    """
    return [num * num for num in nums if num % 2 == 0]


def name_lengths(names: list[str]) -> dict[str, int]:
    """Return a dict mapping each name to its length.

    # loop version:
    # result = {}
    # for name in names:
    #     result[name] = len(name)
    # return result

    name_lengths(["Ada", "Grace"]) -> {"Ada": 3, "Grace": 5}
    """
    return {name: len(name) for name in names}


def first_letters(words: list[str]) -> set[str]:
    """Return the set of first letters across all non-empty `words`.

    # loop version:
    # result = set()
    # for word in words:
    #     if word:
    #         result.add(word[0])
    # return result

    first_letters(["cat", "car", "dog"]) -> {"c", "d"}
    """
    return {word[0] for word in words if word}


def celsius_table(start: int, stop: int) -> dict[int, float]:
    """Return a dict mapping each Celsius degree in range(start, stop) to
    its Fahrenheit equivalent (`c * 9 / 5 + 32`).

    # loop version:
    # result = {}
    # for c in range(start, stop):
    #     result[c] = c * 9 / 5 + 32
    # return result

    celsius_table(0, 2) -> {0: 32.0, 1: 33.8}
    """
    return {c: c * 9 / 5 + 32 for c in range(start, stop)}


if __name__ == "__main__":
    print(squares_of_evens([1, 2, 3, 4]))
    print(first_letters(["cat", "car", "dog"]))
    print(celsius_table(0, 2))
