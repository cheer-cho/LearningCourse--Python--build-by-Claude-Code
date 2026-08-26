import itertools

import pytest
from checkpoint_09 import Corpus, memoized, tokens, unique


def test_tokens_splits_and_lowercases():
    assert list(tokens(["Hello, world!", "Bye world"])) == ["hello", "world", "bye", "world"]


def test_tokens_empty_lines_is_empty():
    assert list(tokens([])) == []


def test_tokens_stays_lazy_over_an_infinite_line_stream():
    def infinite_lines():
        n = 0
        while True:
            yield f"word{n}"
            n += 1

    first_five = list(itertools.islice(tokens(infinite_lines()), 5))
    assert first_five == ["word0", "word1", "word2", "word3", "word4"]


def test_unique_preserves_first_seen_order():
    assert list(unique([1, 2, 1, 3, 2])) == [1, 2, 3]


def test_unique_empty_is_empty():
    assert list(unique([])) == []


def test_unique_stays_lazy_over_an_infinite_repeating_stream():
    def repeating_forever():
        while True:
            yield from [1, 1, 2, 2, 3, 3]

    first_three = list(itertools.islice(unique(repeating_forever()), 3))
    assert first_three == [1, 2, 3]


def test_memoized_caches_repeat_calls():
    calls = []

    @memoized
    def add(a, b):
        calls.append((a, b))
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert len(calls) == 1


def test_memoized_distinguishes_different_arguments():
    calls = []

    @memoized
    def add(a, b):
        calls.append((a, b))
        return a + b

    add(1, 2)
    add(2, 1)
    assert len(calls) == 2


def test_memoized_cache_clear_forces_recompute():
    calls = []

    @memoized
    def add(a, b):
        calls.append((a, b))
        return a + b

    add(1, 2)
    add.cache_clear()
    add(1, 2)
    assert len(calls) == 2


def test_corpus_len_counts_lines():
    assert len(Corpus(["Hello world", "hello there"])) == 2


def test_corpus_iter_yields_unique_tokens_lazily():
    corpus = Corpus(["Hello world", "hello there"])
    assert list(corpus) == ["hello", "world", "there"]


def test_corpus_iter_can_be_used_more_than_once():
    corpus = Corpus(["Hello world"])
    assert list(corpus) == list(corpus)


def test_corpus_contains_is_case_insensitive():
    corpus = Corpus(["Hello world", "hello there"])
    assert "world" in corpus
    assert "WORLD" in corpus
    assert "bye" not in corpus


def test_corpus_vocabulary_is_sorted_and_deduped():
    corpus = Corpus(["Hello world", "hello there"])
    assert corpus.vocabulary == ["hello", "there", "world"]


def test_corpus_vocabulary_is_a_property_not_a_method():
    corpus = Corpus(["a a b"])
    assert corpus.vocabulary == ["a", "b"]
    with pytest.raises(TypeError):
        corpus.vocabulary()
