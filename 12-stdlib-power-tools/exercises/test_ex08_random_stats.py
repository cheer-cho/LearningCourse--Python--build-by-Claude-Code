import random

import pytest
from ex08_random_stats import sample_scores, summarize, weighted_pick


def test_sample_scores_is_deterministic_for_a_given_seed():
    assert sample_scores(random.Random(0), 5) == [49, 97, 53, 5, 33]


def test_sample_scores_different_seed_different_sequence():
    assert sample_scores(random.Random(42), 3) == [81, 14, 3]


def test_sample_scores_length_matches_n():
    assert len(sample_scores(random.Random(1), 10)) == 10


def test_sample_scores_within_range():
    scores = sample_scores(random.Random(5), 50)
    assert all(0 <= score <= 100 for score in scores)


def test_summarize_typical():
    assert summarize([1, 2, 3]) == {"mean": 2.0, "median": 2.0, "stdev": 1.0}


def test_summarize_stdev_none_for_single_value():
    assert summarize([5]) == {"mean": 5.0, "median": 5.0, "stdev": None}


def test_summarize_even_count_median():
    result = summarize([1, 2, 3, 4])
    assert result["mean"] == 2.5
    assert result["median"] == 2.5
    assert result["stdev"] == pytest.approx(1.2909944487)


def test_weighted_pick_returns_a_valid_key():
    result = weighted_pick(random.Random(1), {"a": 1.0, "b": 9.0})
    assert result in {"a", "b"}


def test_weighted_pick_is_deterministic_for_a_given_seed():
    assert weighted_pick(random.Random(7), {"a": 1.0, "b": 9.0}) == "b"


def test_weighted_pick_heavier_weight_wins_more_often():
    rng = random.Random(1)
    picks = [weighted_pick(rng, {"a": 1.0, "b": 9.0}) for _ in range(10)]
    assert picks.count("b") > picks.count("a")
