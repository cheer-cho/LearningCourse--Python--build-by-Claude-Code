# Scenario: a pizzeria wants named presets, an order parser, and a
# topping validator. Concepts: @classmethod as an alternative
# constructor, @staticmethod for a helper with no instance/class state.
# Run: uv run pytest 08-oop -k ex04

VALID_TOPPINGS = {  # given: the toppings the pizzeria stocks
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
    """A pizza is just a list of toppings."""

    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        """Build the classic margherita: tomato, cheese, basil (in that order).

        Pizza.margherita().toppings -> ["tomato", "cheese", "basil"]
        """
        raise NotImplementedError

    @classmethod
    def hawaiian(cls):
        """Build a hawaiian: ham, pineapple, cheese (in that order).

        Pizza.hawaiian().toppings -> ["ham", "pineapple", "cheese"]
        """
        raise NotImplementedError

    @classmethod
    def from_string(cls, text):
        """Build a Pizza from a comma-separated topping string.

        Split on commas and strip whitespace around each topping; drop
        any empty pieces (e.g. a trailing comma).

        Pizza.from_string("pepperoni,olives").toppings -> ["pepperoni", "olives"]
        Pizza.from_string("ham, pineapple").toppings -> ["ham", "pineapple"]
        """
        raise NotImplementedError

    @staticmethod
    def valid_topping(name):
        """Return True if `name` (case-insensitive) is in VALID_TOPPINGS.

        Pizza.valid_topping("cheese") -> True
        Pizza.valid_topping("Cheese") -> True
        Pizza.valid_topping("anchovy") -> False
        """
        raise NotImplementedError
