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
        self.celsius = celsius  # routed through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
