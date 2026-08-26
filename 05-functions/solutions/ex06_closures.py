def make_multiplier(k):
    def multiply(n):
        return n * k

    return multiply


def make_accumulator():
    total = 0

    def add(amount):
        nonlocal total
        total += amount
        return total

    return add


def make_button_handlers(labels):
    handlers = []
    for i, label in enumerate(labels):

        def handler(i=i, label=label):
            return f"{label} clicked (button {i})"

        handlers.append(handler)
    return handlers
