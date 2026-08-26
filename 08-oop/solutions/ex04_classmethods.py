VALID_TOPPINGS = {
    "tomato",
    "cheese",
    "basil",
    "ham",
    "pineapple",
    "pepperoni",
    "olives",
    "mushroom",
}


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(["tomato", "cheese", "basil"])

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple", "cheese"])

    @classmethod
    def from_string(cls, text):
        toppings = [piece.strip() for piece in text.split(",")]
        return cls([topping for topping in toppings if topping])

    @staticmethod
    def valid_topping(name):
        return name.lower() in VALID_TOPPINGS
