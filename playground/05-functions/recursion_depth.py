"""How deep does the call stack get? Measure it.

Run: uv run python playground/05-functions/recursion_depth.py
"""

import sys

max_depth = 0


def count_head_tail(items, depth=1):
    """Count items by peeling off the head and recursing on the tail."""
    global max_depth
    max_depth = max(max_depth, depth)
    if not items:
        return 0
    _first, *rest = items  # also copies the list each call: O(n^2) total
    return 1 + count_head_tail(rest, depth + 1)


print("recursion limit:", sys.getrecursionlimit())

for n in (10, 500, 2000):
    max_depth = 0
    try:
        count_head_tail(list(range(n)))
        print(f"n={n:<5} ok, max stack depth = {max_depth}")
    except RecursionError:
        print(f"n={n:<5} RecursionError at depth ~{max_depth}")

# Takeaway: head/tail recursion uses ONE stack frame PER ITEM.
# The list is flat (nesting depth 1), yet the stack grows with its length.
