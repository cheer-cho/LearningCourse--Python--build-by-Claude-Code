import random

from ex02_container_protocol import RANKS, SUITS, Deck


def test_len_is_52():
    assert len(Deck()) == 52


def test_getitem_by_index():
    assert Deck()[0] == ("2", "Clubs")


def test_getitem_by_slice_returns_a_list():
    assert Deck()[:4] == [("2", "Clubs"), ("2", "Diamonds"), ("2", "Hearts"), ("2", "Spades")]


def test_contains_true_for_a_real_card():
    assert ("A", "Spades") in Deck()


def test_contains_false_for_a_fake_card():
    assert ("Joker", "Clubs") not in Deck()


def test_iterates_every_card_exactly_once():
    cards = list(Deck())
    assert len(cards) == 52
    assert len(set(cards)) == 52


def test_every_rank_and_suit_combination_present():
    deck = set(Deck())
    assert deck == {(rank, suit) for rank in RANKS for suit in SUITS}


def test_random_choice_works_via_len_and_getitem():
    random.seed(0)
    card = random.choice(Deck())
    assert card in Deck()
