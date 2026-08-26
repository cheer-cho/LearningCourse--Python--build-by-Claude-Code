# Idiom drill: manual accumulator/flag loops -> sum/any/all/max with a
# generator expression or key=. The clunky "before" for the first one
# (kept out here, not inside any function, since tests inspect each
# function's own source):
#
#     def _cart_total_clunky(cart):
#         total = 0
#         for item in cart:
#             total += item["price"] * item["quantity"]
#         return total
#
#     def _has_failing_score_clunky(scores, passing):
#         found = False
#         for score in scores:
#             if score < passing:
#                 found = True
#         return found
#
# Your job: replace each `raise NotImplementedError` with a one-liner
# built from sum()/any()/all()/max(key=...) over a generator
# expression — no `.append()` building an intermediate list anywhere in
# your rewrite.
# Run: uv run pytest 09-pythonic-deep-dive -k drill02


def cart_total(cart):
    """Sum `price * quantity` across every item in `cart` (dicts with
    "price" and "quantity" keys), computed in one pass with no
    intermediate list.

    cart_total([{"price": 2.0, "quantity": 3}, {"price": 5.0, "quantity": 1}])
    -> 11.0
    cart_total([]) -> 0
    """
    raise NotImplementedError


def has_failing_score(scores, passing):
    """True if any score in `scores` is below `passing`.

    has_failing_score([90, 55, 88], 60) -> True
    has_failing_score([90, 95], 60) -> False
    has_failing_score([], 60) -> False
    """
    raise NotImplementedError


def all_even(nums):
    """True if every number in `nums` is even (vacuously True when
    `nums` is empty).

    all_even([2, 4, 6]) -> True
    all_even([2, 3, 4]) -> False
    all_even([]) -> True
    """
    raise NotImplementedError


def top_student(students):
    """Return the name of the student (dicts with "name" and "score")
    with the highest score.

    top_student([{"name": "Ada", "score": 91}, {"name": "Bo", "score": 88}])
    -> "Ada"
    """
    raise NotImplementedError
