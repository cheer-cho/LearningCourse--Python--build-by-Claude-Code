import pytest
from ex03_properties import Temperature


def test_init_stores_celsius():
    assert Temperature(100).celsius == 100


def test_init_defaults_to_zero():
    assert Temperature().celsius == 0


def test_celsius_setter_updates_value():
    t = Temperature(0)
    t.celsius = 20
    assert t.celsius == 20


def test_celsius_setter_rejects_below_absolute_zero():
    t = Temperature(0)
    with pytest.raises(ValueError):
        t.celsius = -300


def test_init_rejects_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-300)


def test_celsius_setter_accepts_exact_absolute_zero():
    t = Temperature(0)
    t.celsius = -273.15
    assert t.celsius == -273.15


def test_fahrenheit_freezing_point():
    assert Temperature(0).fahrenheit == pytest.approx(32.0)


def test_fahrenheit_boiling_point():
    assert Temperature(100).fahrenheit == pytest.approx(212.0)


def test_fahrenheit_setter_converts_and_stores_as_celsius():
    t = Temperature(0)
    t.fahrenheit = 32
    assert t.celsius == pytest.approx(0.0)


def test_fahrenheit_setter_goes_through_validation():
    t = Temperature(0)
    with pytest.raises(ValueError):
        t.fahrenheit = -500
