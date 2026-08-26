# Scenario: a drawing app needs shapes that each know how to compute
# their own area. Concepts: a base class with a method subclasses must
# override, super().__init__, polymorphism.
# Run: uv run pytest 08-oop -k ex06


class Shape:
    """A named shape. Subclasses must provide an `area` property."""

    def __init__(self, name):
        """Store the shape's name."""
        raise NotImplementedError

    @property
    def area(self):
        """Subclasses override this. The base Shape has no area of its
        own, so calling it here raises NotImplementedError.
        """
        raise NotImplementedError

    def describe(self):
        """Return "<name>: area=<area, 2 decimal places>", using
        whichever subclass's `area` the instance actually has.

        Circle("c", 2).describe() -> "c: area=12.57"
        """
        raise NotImplementedError


class Circle(Shape):
    """A circle, given its radius."""

    def __init__(self, name, radius):
        """Set up the shared Shape state via super().__init__, then
        store radius.
        """
        raise NotImplementedError

    @property
    def area(self):
        """pi * radius ** 2. Needs `import math` at the top of the file
        (math.pi).
        """
        raise NotImplementedError


class Rectangle(Shape):
    """A rectangle, given its width and height."""

    def __init__(self, name, width, height):
        """Set up the shared Shape state via super().__init__, then
        store width and height.
        """
        raise NotImplementedError

    @property
    def area(self):
        """width * height."""
        raise NotImplementedError


def total_area(shapes):
    """Return the sum of `.area` across every shape in `shapes`, no
    matter which Shape subclass each one is.

    total_area([Circle("c", 1), Rectangle("r", 2, 3)]) -> approx 9.14
    """
    raise NotImplementedError
