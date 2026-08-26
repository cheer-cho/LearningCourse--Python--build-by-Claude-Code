# Scenario: tagging system for blog posts — dedupe tags, compare
# interests between two users. Concepts: set literals, dedupe, |, &, -,
# ^, membership speed.
# Run: uv run pytest 04-collections -k ex04


def unique_tags(tags: list[str]) -> set[str]:
    """Return the distinct tags in `tags` as a set.

    unique_tags(["python", "web", "python", "cli"]) -> {"python", "web", "cli"}
    """
    raise NotImplementedError


def common_interests(a: set[str], b: set[str]) -> set[str]:
    """Return the interests present in both `a` and `b`.

    common_interests({"chess", "hiking"}, {"hiking", "reading"}) -> {"hiking"}
    """
    raise NotImplementedError


def only_in_first(a: set[str], b: set[str]) -> set[str]:
    """Return the interests in `a` that are NOT in `b`.

    only_in_first({"chess", "hiking"}, {"hiking", "reading"}) -> {"chess"}
    """
    raise NotImplementedError


def has_duplicates(items: list[int]) -> bool:
    """Return True if `items` contains any repeated value.

    has_duplicates([1, 2, 3]) -> False
    has_duplicates([1, 2, 2]) -> True
    has_duplicates([]) -> False
    """
    raise NotImplementedError
