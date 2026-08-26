import inspect

import pytest
from ex04_generators import chunks, countdown_gen, running_total


def test_countdown_gen_counts_down():
    assert list(countdown_gen(3)) == [3, 2, 1]


def test_countdown_gen_zero_is_empty():
    assert list(countdown_gen(0)) == []


def test_countdown_gen_is_a_generator_function():
    assert inspect.isgeneratorfunction(countdown_gen)


def test_countdown_gen_restarts_on_a_new_call():
    assert list(countdown_gen(2)) == list(countdown_gen(2)) == [2, 1]


def test_chunks_splits_evenly():
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunks_leaves_a_short_final_chunk():
    assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_chunks_of_empty_input_is_empty():
    assert list(chunks([], 2)) == []


def test_chunks_rejects_non_positive_size():
    with pytest.raises(ValueError):
        list(chunks([1, 2], 0))


def test_running_total_accumulates():
    assert list(running_total([1, 2, 3])) == [1, 3, 6]


def test_running_total_of_empty_is_empty():
    assert list(running_total([])) == []


def test_running_total_is_lazy_one_value_at_a_time():
    gen = running_total([1, 2, 3, 4])
    assert next(gen) == 1
    assert next(gen) == 3
