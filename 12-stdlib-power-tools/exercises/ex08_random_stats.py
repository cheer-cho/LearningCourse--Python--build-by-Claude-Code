# Scenario: generating and summarizing synthetic test-score data for a
# demo dataset. Concepts: an injected random.Random (never the global
# `random` module, so results are reproducible) plus the statistics
# module.
# Run: uv run pytest 12-stdlib-power-tools -k ex08

import random
import statistics  # noqa: F401 — needed once functions are implemented


def sample_scores(rng: random.Random, n: int) -> list[int]:
    """Return `n` random integer scores in [0, 100], drawn from the
    injected `rng`. Never call the global `random` module functions
    directly — an injected Random instance is what makes this
    reproducible and testable.

    sample_scores(random.Random(0), 3) -> the same 3 ints every time,
    since seed 0 always produces the same sequence.
    """
    raise NotImplementedError


def summarize(nums: list[float]) -> dict[str, float | None]:
    """Return {"mean": ..., "median": ..., "stdev": ...} for `nums`.
    "stdev" is None when there are fewer than 2 values (sample stdev is
    undefined for a single point).

    summarize([1, 2, 3]) -> {"mean": 2.0, "median": 2.0, "stdev": 1.0}
    summarize([5]) -> {"mean": 5.0, "median": 5.0, "stdev": None}
    """
    raise NotImplementedError


def weighted_pick(rng: random.Random, options: dict[str, float]) -> str:
    """Pick and return one key from `options` (key -> weight), using
    `rng` for a weighted random choice. Weights don't need to sum to 1;
    larger weight means more likely to be picked.

    weighted_pick(random.Random(1), {"a": 1.0, "b": 9.0}) -> one of
    "a"/"b", "b" far more often across repeated calls with fresh seeds.
    """
    raise NotImplementedError
