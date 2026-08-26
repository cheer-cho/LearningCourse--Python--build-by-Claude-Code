"""Read three tracebacks, then fix the bug each one points at.

Every function below is broken. The comment above each one is the real
traceback Python prints when you call it. Read a traceback bottom-up: the
last line is the error type and message, the line above it is the exact
line that failed, and the frames above that are the call chain that got
you there.

Run: uv run pytest 01-setup-tooling -k ex02
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

    Calling order_total(10, 3) currently raises:
        Traceback (most recent call last):
          File "ex02_tracebacks.py", line 34, in order_total
            return subtotl
                   ^^^^^^^
        NameError: name 'subtotl' is not defined. Did you mean: 'subtotal'?
    """
    subtotal = price * quantity
    return subtotl


def receipt_line(item_name, count):
    """Return a one-line receipt entry like "apples: 3".

    Params:
        item_name (str): the item's name.
        count (int): how many were bought.

    Returns:
        str: "<item_name>: <count>".

    Examples:
        receipt_line("apples", 3) -> "apples: 3"

    Calling receipt_line("apples", 3) currently raises:
        Traceback (most recent call last):
          File "ex02_tracebacks.py", line 57, in receipt_line
            return item_name + ": " + count
                   ~~~~~~~~~~~~~~~~~^~~~~~~
        TypeError: can only concatenate str (not "int") to str
    """
    return item_name + ": " + count


def average_score(scores):
    """Return the average of `scores`, or 0.0 if `scores` is empty.

    Params:
        scores (list[float]): scores to average.

    Returns:
        float: the mean of `scores`, or 0.0 for an empty list.

    Examples:
        average_score([10, 20, 30]) -> 20.0
        average_score([]) -> 0.0

    Calling average_score([]) currently raises:
        Traceback (most recent call last):
          File "ex02_tracebacks.py", line 80, in average_score
            return sum(scores) / len(scores)
                   ~~~~~~~~~~~~^~~~~~~~~~~~~
        ZeroDivisionError: division by zero
    """
    return sum(scores) / len(scores)
