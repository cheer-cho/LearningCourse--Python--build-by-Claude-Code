# What does str(e) show when a custom exception skips super().__init__()?


class WithSuper(Exception):
    def __init__(self, needed, available):
        super().__init__(f"need {needed}, only have {available}")
        self.needed = needed
        self.available = available


class NoSuper(Exception):
    def __init__(self, needed, available):
        # no super().__init__() call
        self.needed = needed
        self.available = available


for label, exc in [
    ("WithSuper(150, 100)        ", WithSuper(150, 100)),
    ("NoSuper(150, 100)          ", NoSuper(150, 100)),
    ("NoSuper(needed=150, ...)   ", NoSuper(needed=150, available=100)),
]:
    print(f"{label} str={str(exc)!r:28} args={exc.args!r}")
