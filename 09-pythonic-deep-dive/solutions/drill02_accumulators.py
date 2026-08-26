def cart_total(cart):
    """Sum `price * quantity` across every item in `cart` (dicts with
    "price" and "quantity" keys), computed in one pass with no
    intermediate list.

    cart_total([{"price": 2.0, "quantity": 3}, {"price": 5.0, "quantity": 1}])
    -> 11.0
    cart_total([]) -> 0
    """
    return sum(item["price"] * item["quantity"] for item in cart)


def has_failing_score(scores, passing):
    """True if any score in `scores` is below `passing`.

    has_failing_score([90, 55, 88], 60) -> True
    has_failing_score([90, 95], 60) -> False
    has_failing_score([], 60) -> False
    """
    return any(score < passing for score in scores)


def all_even(nums):
    """True if every number in `nums` is even (vacuously True when
    `nums` is empty).

    all_even([2, 4, 6]) -> True
    all_even([2, 3, 4]) -> False
    all_even([]) -> True
    """
    return all(n % 2 == 0 for n in nums)


def top_student(students):
    """Return the name of the student (dicts with "name" and "score")
    with the highest score.

    top_student([{"name": "Ada", "score": 91}, {"name": "Bo", "score": 88}])
    -> "Ada"
    """
    return max(students, key=lambda student: student["score"])["name"]
