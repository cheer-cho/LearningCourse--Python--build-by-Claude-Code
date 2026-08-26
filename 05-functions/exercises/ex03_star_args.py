# Scenario: a tiny toolkit for functions that accept a variable number
# of arguments. Concepts: *args (collecting extra positionals),
# **kwargs (collecting extra keywords), forwarding a call with * / **.
# Run: uv run pytest 05-functions -k ex03


def average(*nums):
    """Return the mean of `nums`, or None if no arguments were passed.

    average(1, 2, 3) -> 2.0
    average(5) -> 5.0
    average() -> None
    """
    raise NotImplementedError


def longest(*words):
    """Return the longest string in `words`. On a tie, return whichever
    one appears first. Return None if no arguments were passed.

    longest("cat", "elephant", "dog") -> "elephant"
    longest("aa", "bb") -> "aa"
    longest() -> None
    """
    raise NotImplementedError


def html_tag(tag_name, **attrs):
    """Build a self-closing-free opening HTML tag string from `tag_name`
    and keyword attributes, with attributes sorted alphabetically by
    name and each value double-quoted. `tag_name` is its own parameter
    (not folded into `**attrs`) so a caller can still pass an HTML
    `name` attribute without colliding with it.

    html_tag("a", href="x", id="y") -> '<a href="x" id="y">'
    html_tag("input", type="text", name="q") -> '<input name="q" type="text">'
    html_tag("br") -> "<br>"
    """
    raise NotImplementedError


def forward_call(func, *args, **kwargs):
    """Call `func` with `args` and `kwargs` forwarded unchanged, and
    return whatever `func` returns. Use `*args` / `**kwargs` to unpack
    when calling `func`.

    forward_call(max, 1, 5, 3) -> 5
    forward_call(sorted, [3, 1, 2], reverse=True) -> [3, 2, 1]
    """
    raise NotImplementedError
