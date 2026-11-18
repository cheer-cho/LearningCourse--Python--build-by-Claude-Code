def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def flatten_head_tail(nested):
    # ❌ Head/tail version: correct output, but it doesn't scale. Kept to
    # compare against `flatten` below.
    #
    # Problem 1: one stack frame PER ITEM. It recurses on `rest` even when
    #   every item is a plain value, so the stack grows with the list's
    #   LENGTH, not its nesting. Python has no tail-call optimization and
    #   allows about 1000 frames, so flatten_head_tail(list(range(2000)))
    #   raises RecursionError, even though that list is only 1 level deep.
    # Problem 2: `first, *rest = nested` copies the tail on every call,
    #   which adds up to O(n^2) copying.
    if not nested:
        return []
    first, *rest = nested
    if isinstance(first, list):
        return flatten_head_tail(first) + flatten_head_tail(rest)
    return [first] + flatten_head_tail(rest)


def flatten(nested):
    # ✅ Fix: recurse on DEPTH, iterate over BREADTH.
    # The `for` loop walks the items at this level without adding stack
    # frames. We recurse only when an item is itself a list, so the stack
    # depth equals the nesting depth (e.g. 3 for [[[1]]]), however long the
    # list is. There's no slicing or unpacking, so no copying: O(n) total.
    # See playground/05-functions/recursion_depth.md.
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))  # go one level deeper
        else:
            result.append(item)  # plain value: no new frame
    return result


def count_down_up(n):
    if n == 1:
        return "1 1"
    return f"{n} {count_down_up(n - 1)} {n}"
