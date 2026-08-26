import math


class Shape:
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.name}: area={self.area:.2f}"


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


def total_area(shapes):
    return sum(shape.area for shape in shapes)
