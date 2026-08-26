class InsufficientFunds(Exception):
    def __init__(self, needed, available):
        super().__init__(f"need {needed}, only have {available}")
        self.needed = needed
        self.available = available


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(needed=amount, available=balance)
    return balance - amount
