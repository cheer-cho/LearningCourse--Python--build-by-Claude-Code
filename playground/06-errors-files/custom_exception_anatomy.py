"""Anatomy of a custom exception with extra attributes."""


class InsufficientFunds(Exception):
    def __init__(self, needed, available):
        super().__init__(f"need {needed}, only have {available}")
        self.needed = needed
        self.available = available


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(needed=amount, available=balance)
    return balance - amount


# 1. What did super().__init__(...) give us?
exc = InsufficientFunds(100, 30)
print("str(exc)  ->", str(exc))       # the message
print("exc.args  ->", exc.args)       # Exception stores the message here
print("needed    ->", exc.needed)     # our own attributes
print("available ->", exc.available)

# 2. Catching it: read the data, don't parse the string
try:
    withdraw(balance=30, amount=100)
except InsufficientFunds as e:
    short_by = e.needed - e.available
    print(f"\ncaught: {e}  (short by {short_by})")

# 3. It's still an Exception, so a broad handler catches it too
try:
    withdraw(30, 100)
except Exception as e:
    print("broad handler:", type(e).__name__, "-", e)


# 4. What if we forgot super().__init__?
class Forgetful(Exception):
    def __init__(self, needed, available):
        self.needed = needed
        self.available = available


print("\nforgot super():", repr(str(Forgetful(100, 30))))  # empty message!
