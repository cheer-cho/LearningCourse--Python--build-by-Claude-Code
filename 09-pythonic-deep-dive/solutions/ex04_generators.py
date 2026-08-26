def countdown_gen(n):
    """Generator version of Countdown: yield n, n-1, ..., 1. Compare
    the line count to ex03 — this is what generators buy you.

    list(countdown_gen(3)) -> [3, 2, 1]
    list(countdown_gen(0)) -> []
    """
    while n > 0:
        yield n
        n -= 1


def chunks(items, size):
    """Yield successive lists of at most `size` items from `items`. The
    last chunk may be shorter than `size` if `items` doesn't divide
    evenly.

    list(chunks([1, 2, 3, 4, 5], 2)) -> [[1, 2], [3, 4], [5]]
    list(chunks([], 2)) -> []
    chunks([1], 0) raises ValueError
    """
    if size <= 0:
        raise ValueError("size must be positive")
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def running_total(nums):
    """Yield the running (cumulative) sum of `nums`, lazily — one
    partial sum per input value, computed only as it's requested.

    list(running_total([1, 2, 3])) -> [1, 3, 6]
    list(running_total([])) -> []
    """
    total = 0
    for n in nums:
        total += n
        yield total
