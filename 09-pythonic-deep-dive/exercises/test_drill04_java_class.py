import inspect

import pytest
from drill04_java_class import Temperature


def test_celsius_readable_after_construction():
    assert Temperature(20).celsius == 20


def test_fahrenheit_is_derived_from_celsius():
    assert Temperature(20).fahrenheit == 68.0


def test_setting_celsius_updates_fahrenheit():
    t = Temperature(0)
    t.celsius = 100
    assert t.fahrenheit == 212.0


def test_celsius_setter_validates_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-300)


def test_setting_celsius_below_absolute_zero_also_raises():
    t = Temperature(0)
    with pytest.raises(ValueError):
        t.celsius = -300


def test_fahrenheit_has_no_setter():
    t = Temperature(0)
    with pytest.raises(AttributeError):
        t.fahrenheit = 100


def test_rewrite_avoids_getter_setter_methods():
    source = inspect.getsource(Temperature)
    assert "get_" not in source, "use a @property instead of a get_* method"
    assert "set_" not in source, "use a @x.setter instead of a set_* method"
