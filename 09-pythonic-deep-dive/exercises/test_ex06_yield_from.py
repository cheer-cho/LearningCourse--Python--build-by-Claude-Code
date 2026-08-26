import inspect

from ex06_yield_from import concat_all, flatten


def test_flatten_nested_lists():
    assert list(flatten([1, [2, 3, [4]], 5])) == [1, 2, 3, 4, 5]


def test_flatten_empty_is_empty():
    assert list(flatten([])) == []


def test_flatten_handles_tuples_too():
    assert list(flatten([1, (2, 3)])) == [1, 2, 3]


def test_flatten_deeply_nested():
    assert list(flatten([[[[1]]], 2])) == [1, 2]


def test_flatten_is_a_generator_function():
    assert inspect.isgeneratorfunction(flatten)


def test_concat_all_chains_in_order():
    assert list(concat_all([1, 2], "ab", (9,))) == [1, 2, "a", "b", 9]


def test_concat_all_no_args_is_empty():
    assert list(concat_all()) == []


def test_concat_all_exhausts_one_source_before_the_next():
    def source(label, values):
        for v in values:
            yield f"{label}{v}"

    result = list(concat_all(source("a", [1, 2]), source("b", [1, 2])))
    assert result == ["a1", "a2", "b1", "b2"]
