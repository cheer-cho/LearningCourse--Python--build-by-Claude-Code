"""Reference solution for ex02_tracebacks. Not imported by tests directly —
scripts/verify_solutions.py overlays this onto the exercise stub.
"""


def order_total(price, quantity):
    """Return `price * quantity`.

    Params:
        price (float): unit price.
        quantity (int): how many units.

    Returns:
        float: the order subtotal.

    Examples:
        order_total(10, 3) -> 30
    """
    subtotal = price * quantity
    return subtotal


def receipt_line(item_name, count):
    """Return a one-line receipt entry like "apples: 3".

    Params:
        item_name (str): the item's name.
        count (int): how many were bought.

    Returns:
        str: "<item_name>: <count>".

    Examples:
        receipt_line("apples", 3) -> "apples: 3"
    """
    return item_name + ": " + str(count)


def average_score(scores):
    """Return the average of `scores`, or 0.0 if `scores` is empty.

    Params:
        scores (list[float]): scores to average.

    Returns:
        float: the mean of `scores`, or 0.0 for an empty list.

    Examples:
        average_score([10, 20, 30]) -> 20.0
        average_score([]) -> 0.0
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
