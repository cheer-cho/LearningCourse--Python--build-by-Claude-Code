# Idiom drill: a Java-style getter/setter class -> @property. The
# clunky "before" (kept out here, not inside the class, since the test
# inspects the class's own source for `get_`/`set_`):
#
#     class TemperatureClunky:
#         def __init__(self, celsius):
#             self._celsius = celsius
#
#         def get_celsius(self):
#             return self._celsius
#
#         def set_celsius(self, value):
#             if value < -273.15:
#                 raise ValueError("temperature below absolute zero")
#             self._celsius = value
#
#         def get_fahrenheit(self):
#             return self._celsius * 9 / 5 + 32
#
# Your job: rewrite it below as `Temperature`, using @property /
# @celsius.setter instead of get_*/set_* methods — no `get_` or `set_`
# substring anywhere in your class.
# Run: uv run pytest 09-pythonic-deep-dive -k drill04


class Temperature:
    """A temperature stored internally in Celsius, exposed through
    @property instead of Java-style getter/setter methods. `celsius`
    is a normal, validated read/write attribute; `fahrenheit` is a
    read-only value derived from it on every access.

    t = Temperature(20)
    t.celsius -> 20
    t.fahrenheit -> 68.0
    t.celsius = 100
    t.fahrenheit -> 212.0
    Temperature(-300) raises ValueError   # below absolute zero
    """

    def __init__(self, celsius):
        raise NotImplementedError

    # TODO: a `celsius` property (getter) and its @celsius.setter
    # (validating against absolute zero), plus a read-only
    # `fahrenheit` property derived from self.celsius.
