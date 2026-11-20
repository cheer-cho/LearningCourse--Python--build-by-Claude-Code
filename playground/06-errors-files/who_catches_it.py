"""An uncaught exception climbs the call stack until someone catches it."""

import sys

sys.path.insert(0, "06-errors-files/exercises")
from ex05_chaining import ConfigError, load_setting  # noqa: E402


def start_app(raw):
    retries = load_setting(raw, "retries")  # no try here: just passes it up
    return f"app started with {retries} retries"


def main():
    for raw in [{"retries": "3"}, {"retries": "many"}, {"retries": None}]:
        try:
            print(start_app(raw))
        except ConfigError as e:
            print(f"config problem, using default: {e}")
        except Exception as e:  # top-level safety net
            print(f"BUG, please report: {type(e).__name__}: {e}")


main()
print("program still running")

start_app({"retries": None})  # nobody catches this one -> traceback, exit code 1
print("never printed")
