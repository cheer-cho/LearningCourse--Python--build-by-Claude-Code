from ex06_match import command


def test_command_go_known_direction():
    assert command(("go", "north")) == "moving north"


def test_command_go_unknown_direction():
    assert command(("go", "up")) == "can't go up"


def test_command_quit():
    assert command(("quit",)) == "goodbye"


def test_command_help():
    assert command(("help",)) == "commands: go, quit, help, repeat"


def test_command_help_alias_question_mark():
    assert command(("?",)) == "commands: go, quit, help, repeat"


def test_command_repeat_with_guard_passing():
    assert command(("repeat", 3)) == "repeating 3 times"


def test_command_repeat_with_guard_failing():
    assert command(("repeat", 0)) == "nothing to repeat"


def test_command_unknown_falls_through():
    assert command(("dance",)) == "unknown command"
