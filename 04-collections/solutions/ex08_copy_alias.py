import copy


def broken_reset(scores: list[int]) -> list[int]:
    return list(scores)


def deep_trap(board: list[list[int]]) -> list[list[int]]:
    return copy.deepcopy(board)


def safe_flat_copy(base: list[int], extra: int) -> list[int]:
    result = list(base)
    result.append(extra)
    return result


def independent_deep_copy(board: list[list[int]], row: int, value: int) -> list[list[int]]:
    result = copy.deepcopy(board)
    result[row].append(value)
    return result
