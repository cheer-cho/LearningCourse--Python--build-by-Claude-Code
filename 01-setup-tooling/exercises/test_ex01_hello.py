"""Tests for ex01_hello.

Run: uv run pytest 01-setup-tooling -k ex01
"""

from ex01_hello import greet


def test_greet_returns_hello_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_with_a_different_name():
    assert greet("Grace") == "Hello, Grace!"


def test_greet_returns_a_string():
    assert isinstance(greet("Bo"), str)
