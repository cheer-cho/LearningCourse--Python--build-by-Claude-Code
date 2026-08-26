from checkpoint_03 import guess_feedback, play_round


def test_guess_feedback_correct():
    assert guess_feedback(42, 42, 1, 5) == "correct!"


def test_guess_feedback_too_high():
    assert guess_feedback(42, 50, 1, 5) == "too high"


def test_guess_feedback_too_low():
    assert guess_feedback(42, 10, 1, 5) == "too low"


def test_guess_feedback_game_over_on_last_attempt():
    assert guess_feedback(42, 10, 5, 5) == "game over — the number was 42"


def test_guess_feedback_correct_on_last_attempt_still_wins():
    assert guess_feedback(42, 42, 5, 5) == "correct!"


def test_guess_feedback_out_of_range_high():
    assert guess_feedback(42, 500, 1, 5) == "out of range"


def test_guess_feedback_out_of_range_low():
    assert guess_feedback(42, 0, 1, 5) == "out of range"


def test_play_round_win_on_second_guess():
    transcript = play_round(42, [10, 42])
    assert transcript == "attempt 1: guess 10 -> too low\nattempt 2: guess 42 -> correct!"


def test_play_round_win_on_first_guess_stops_immediately():
    transcript = play_round(42, [42, 99, 99])
    assert transcript == "attempt 1: guess 42 -> correct!"


def test_play_round_loss_reports_game_over_on_final_line():
    transcript = play_round(42, [10, 20, 30])
    lines = transcript.split("\n")
    assert len(lines) == 3
    assert lines[-1] == "attempt 3: guess 30 -> game over — the number was 42"


def test_play_round_out_of_range_guess_included_in_transcript():
    transcript = play_round(42, [500, 42])
    lines = transcript.split("\n")
    assert lines[0] == "attempt 1: guess 500 -> out of range"
    assert lines[1] == "attempt 2: guess 42 -> correct!"
