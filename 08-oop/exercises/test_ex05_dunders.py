import pytest
from ex05_dunders import Money, Playlist


def test_repr_shows_amount_and_currency():
    assert repr(Money(500, "USD")) == "Money(500, 'USD')"


def test_eq_true_for_same_amount_and_currency():
    assert Money(500, "USD") == Money(500, "USD")


def test_eq_false_for_different_amount():
    assert Money(500, "USD") != Money(600, "USD")


def test_eq_false_for_different_currency():
    assert Money(500, "USD") != Money(500, "EUR")


def test_eq_false_against_unrelated_type():
    assert (Money(500, "USD") == "500 USD") is False


def test_add_same_currency_sums_amounts():
    total = Money(500, "USD") + Money(150, "USD")
    assert total == Money(650, "USD")


def test_add_different_currency_raises_value_error():
    with pytest.raises(ValueError):
        Money(500, "USD") + Money(150, "EUR")


def test_playlist_starts_empty_by_default():
    assert len(Playlist()) == 0


def test_playlist_accepts_initial_songs():
    playlist = Playlist(["Song A", "Song B"])
    assert len(playlist) == 2


def test_two_default_playlists_do_not_share_a_list():
    a = Playlist()
    b = Playlist()
    a.add_song("Song A")
    assert len(b) == 0


def test_add_song_increases_length():
    playlist = Playlist()
    playlist.add_song("Song A")
    playlist.add_song("Song B")
    assert len(playlist) == 2


def test_contains_true_for_added_song():
    playlist = Playlist()
    playlist.add_song("Song A")
    assert "Song A" in playlist


def test_contains_false_for_missing_song():
    playlist = Playlist(["Song A"])
    assert "Song Z" not in playlist
