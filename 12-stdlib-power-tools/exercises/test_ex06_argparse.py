import pytest
from ex06_argparse import build_parser, run


def test_build_parser_parses_add_with_tag():
    args = build_parser().parse_args(["add", "milk", "--tag", "shop"])
    assert args.action == "add"
    assert args.text == "milk"
    assert args.tag == ["shop"]
    assert args.limit == 10


def test_build_parser_tag_is_repeatable():
    args = build_parser().parse_args(["add", "eggs", "--tag", "shop", "--tag", "urgent"])
    assert args.tag == ["shop", "urgent"]


def test_build_parser_limit_defaults_and_overrides():
    default_args = build_parser().parse_args(["list"])
    assert default_args.limit == 10
    custom_args = build_parser().parse_args(["list", "--limit", "5"])
    assert custom_args.limit == 5


def test_build_parser_help_exits_cleanly():
    with pytest.raises(SystemExit) as exc_info:
        build_parser().parse_args(["--help"])
    assert exc_info.value.code == 0


def test_run_add_returns_confirmation():
    assert run(["add", "milk", "--tag", "shop"], []) == "Added: milk"


def test_run_add_then_list_shows_note_with_tags():
    notes: list[dict[str, object]] = []
    run(["add", "milk", "--tag", "shop"], notes)
    assert run(["list"], notes) == "milk [shop]"


def test_run_list_with_no_notes():
    assert run(["list"], []) == "No notes."


def test_run_list_respects_limit():
    notes: list[dict[str, object]] = []
    run(["add", "a"], notes)
    run(["add", "b"], notes)
    run(["add", "c"], notes)
    assert run(["list", "--limit", "2"], notes) == "a []\nb []"


def test_run_add_without_tag_gives_empty_brackets():
    notes: list[dict[str, object]] = []
    run(["add", "bread"], notes)
    assert run(["list"], notes) == "bread []"
