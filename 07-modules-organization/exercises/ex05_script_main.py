# Scenario: a runnable CLI-style script — the `if __name__ ==
# "__main__":` guard in action. Concepts: `sys.argv`, `sys.exit` with a
# process exit code, testing a script both as a plain function call and
# as a real subprocess.
# Run: uv run pytest 07-modules-organization -k ex05

import sys


def run(argv):
    """Compute count/total/average over the numbers in `argv` and print
    a small report, one stat per line. Return 0 on success.

    If `argv` is empty, print "error: provide at least one number" and
    return 1. If any item can't be parsed as a number, print
    "error: invalid number: <that item>" and return 1. Neither error
    case should raise.

    run(["10", "20", "30"]) -> prints
        count: 3
        total: 60.0
        average: 20.0
      and returns 0
    run([]) -> prints "error: provide at least one number", returns 1
    run(["a"]) -> prints "error: invalid number: a", returns 1
    """
    raise NotImplementedError


def main():
    """Entry point for running this file as a script: parse
    `sys.argv[1:]`, call `run`, and exit the process with its return
    code.
    """
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
