import pytest
from ex08_decorator_args import clamp_result, retry


def test_retry_succeeds_on_the_third_attempt():
    attempts = []

    @retry(3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ValueError("not yet")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 3


def test_retry_returns_immediately_on_first_success():
    attempts = []

    @retry(3)
    def always_ok():
        attempts.append(1)
        return "ok"

    assert always_ok() == "ok"
    assert len(attempts) == 1


def test_retry_reraises_after_exhausting_attempts():
    attempts = []

    @retry(2)
    def always_fails():
        attempts.append(1)
        raise ValueError("nope")

    with pytest.raises(ValueError):
        always_fails()
    assert len(attempts) == 2


def test_retry_preserves_metadata():
    @retry(2)
    def flaky():
        """Docs."""
        return "ok"

    assert flaky.__name__ == "flaky"
    assert flaky.__doc__ == "Docs."


def test_clamp_result_caps_above_hi():
    @clamp_result(0, 100)
    def score(x):
        return x

    assert score(150) == 100


def test_clamp_result_floors_below_lo():
    @clamp_result(0, 100)
    def score(x):
        return x

    assert score(-5) == 0


def test_clamp_result_leaves_in_range_values_alone():
    @clamp_result(0, 100)
    def score(x):
        return x

    assert score(50) == 50


def test_clamp_result_preserves_metadata():
    @clamp_result(0, 10)
    def score(x):
        """Docs."""
        return x

    assert score.__name__ == "score"
    assert score.__doc__ == "Docs."
