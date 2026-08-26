def top_three(scores: list[int]) -> list[int]:
    return sorted(scores, reverse=True)[:3]


def insert_sorted(items: list[int], x: int) -> list[int]:
    position = 0
    while position < len(items) and items[position] < x:
        position += 1
    items.insert(position, x)
    return items


def without_negatives(nums: list[int]) -> list[int]:
    result = []
    for n in nums:
        if n >= 0:
            result.append(n)
    return result
