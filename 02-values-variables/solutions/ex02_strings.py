"""Reference solution for ex02_strings. See exercises/ex02_strings.py."""

from __future__ import annotations


def shout(s: str) -> str:
    return s.upper() + "!"


def initials(full_name: str) -> str:
    first, last = full_name.split()
    return ".".join([first[0].upper(), last[0].upper()]) + "."


def clean_username(raw: str) -> str:
    return raw.strip().lower().replace(" ", "_")
