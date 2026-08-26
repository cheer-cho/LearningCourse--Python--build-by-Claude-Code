import math
import string as s
from statistics import median


def circle_area(radius):
    return math.pi * radius**2


def middle_value(numbers):
    return median(numbers)


def alphabet_position(letter):
    return s.ascii_lowercase.index(letter) + 1
