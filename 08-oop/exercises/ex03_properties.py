# Scenario: a weather station stores temperatures and must reject
# physically impossible values, in either unit. Concepts: @property,
# validation on set, a property that reads/writes a different unit.
# Run: uv run pytest 08-oop -k ex03

ABSOLUTE_ZERO_CELSIUS = -273.15


class Temperature:
    """A temperature, stored internally as celsius."""

    def __init__(self, celsius=0):
        """Store the initial reading. Go through the celsius setter
        below so an impossible starting value is rejected too.

        Temperature(100).celsius -> 100
        """
        raise NotImplementedError

    @property
    def celsius(self):
        """Return the stored temperature in celsius."""
        raise NotImplementedError

    @celsius.setter
    def celsius(self, value):
        """Set the temperature in celsius.

        Raise ValueError if `value` is below absolute zero
        (ABSOLUTE_ZERO_CELSIUS), since that's physically impossible.
        """
        raise NotImplementedError

    @property
    def fahrenheit(self):
        """Return the temperature converted to fahrenheit.

        Formula: celsius * 9 / 5 + 32.

        Temperature(0).fahrenheit -> 32.0
        Temperature(100).fahrenheit -> 212.0
        """
        raise NotImplementedError

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set the temperature from a fahrenheit value.

        Convert to celsius (formula: (value - 32) * 5 / 9) and store it
        through the celsius setter, so an impossible value still raises
        ValueError.

        t = Temperature(0)
        t.fahrenheit = 32
        t.celsius -> 0.0
        """
        raise NotImplementedError
