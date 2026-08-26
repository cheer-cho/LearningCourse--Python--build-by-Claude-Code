import itertools

from ex05_lazy_pipelines import evens, first_n_even_squares, naturals, take


def test_naturals_starts_at_one():
    gen = naturals()
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3


def test_take_pulls_exactly_n_values():
    assert take(naturals(), 3) == [1, 2, 3]


def test_take_zero_pulls_nothing():
    assert take(naturals(), 0) == []


def test_take_leaves_the_generator_positioned_after_n():
    gen = naturals()
    take(gen, 3)
    assert next(gen) == 4


def test_evens_filters_lazily():
    assert take(evens(naturals()), 3) == [2, 4, 6]


def test_evens_only_pulls_as_many_source_values_as_needed():
    pulled = []

    def spy():
        for n in itertools.count(1):
            pulled.append(n)
            yield n

    result = take(evens(spy()), 2)
    assert result == [2, 4]
    # Must not have scanned far past the 4th natural number.
    assert len(pulled) <= 4


def test_first_n_even_squares_typical():
    assert first_n_even_squares(3) == [4, 16, 36]


def test_first_n_even_squares_zero():
    assert first_n_even_squares(0) == []


def test_first_n_even_squares_stays_lazy_for_a_large_n():
    # If this pulled all of naturals() into a list first, this would
    # hang or blow memory. It must return quickly.
    result = first_n_even_squares(50)
    assert len(result) == 50
    assert result[0] == 4
    assert result[-1] == (2 * 50) ** 2
