# Scenario: a "guarded" processing step that logs exactly which phase it
# reached, useful for debugging pipelines. Concepts: try/except/else/
# finally branch order, appending to a shared log list.
# Run: uv run pytest 06-errors-files -k ex03


def guarded_process(data, log):
    """Process `data`, appending one event per phase to `log` (a list).

    `data` is a dict expected to have a "divisor" key; the function
    computes `100 / data["divisor"]`.

    Append, in order:
    - "start" right before the attempt.
    - "error" if computing the result raised (KeyError for a missing
      "divisor", ZeroDivisionError for a zero divisor) — then return
      None.
    - "ok" if the computation succeeded (in an `else` block, not the
      `try`) — then return the computed result.
    - "cleanup" always, no matter what happened (in a `finally` block).

    log = []
    guarded_process({"divisor": 4}, log) -> 25.0, log == ["start", "ok", "cleanup"]
    guarded_process({"divisor": 0}, log) -> None, log == ["start", "error", "cleanup"]
    guarded_process({}, log) -> None, log == ["start", "error", "cleanup"]
    """
    raise NotImplementedError
