from ex02_stdlib_pick import gcd_of, most_common_word, shuffle_deterministic


def test_gcd_of_typical():
    assert gcd_of(12, 18) == 6


def test_gcd_of_coprime_numbers():
    assert gcd_of(7, 13) == 1


def test_gcd_of_one_divides_the_other():
    assert gcd_of(4, 12) == 4


def test_most_common_word_typical():
    assert most_common_word("a b a c a b") == "a"


def test_most_common_word_single_word():
    assert most_common_word("hello") == "hello"


def test_most_common_word_ignores_repeated_whitespace():
    assert most_common_word("x   y x") == "x"


def test_shuffle_deterministic_same_seed_same_order():
    first = shuffle_deterministic([1, 2, 3, 4, 5], seed=1)
    second = shuffle_deterministic([1, 2, 3, 4, 5], seed=1)
    assert first == second


def test_shuffle_deterministic_returns_a_permutation():
    result = shuffle_deterministic([1, 2, 3, 4, 5], seed=2)
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_shuffle_deterministic_does_not_mutate_input():
    items = [1, 2, 3]
    shuffle_deterministic(items, seed=1)
    assert items == [1, 2, 3]


def test_shuffle_deterministic_different_seeds_can_differ():
    a = shuffle_deterministic([1, 2, 3, 4, 5, 6, 7, 8], seed=1)
    b = shuffle_deterministic([1, 2, 3, 4, 5, 6, 7, 8], seed=2)
    assert a != b
