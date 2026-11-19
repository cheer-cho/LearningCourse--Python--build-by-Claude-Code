# try / except / else / finally — which blocks run?

Runnable demo: `uv run python playground/06-errors-files/unmatched_exception_flow.py`

```mermaid
flowchart TD
    T[try body] -->|no exception| E[else]
    T -->|exception raised| M{does an except<br/>match it?}
    M -->|yes| X[that except block]
    M -->|no| F2[finally]
    E --> F1[finally]
    X --> F1
    F1 --> A[code after the try statement]
    F2 --> P[exception keeps propagating<br/>to the caller]
```

*Caption: `else` runs only when the `try` body raised nothing. `finally`
runs on every path. An unmatched exception skips `except` and `else`, runs
`finally`, then escapes. The code after the `try` statement never runs.*

| Case | try | except | else | finally | code after |
|---|---|---|---|---|---|
| No error | ✅ (all of it) | ❌ | ✅ | ✅ | ✅ |
| Error, `except` matches | ✅ (up to the error) | ✅ | ❌ | ✅ | ✅ |
| Error, no match | ✅ (up to the error) | ❌ | ❌ | ✅ | ❌ (the exception escapes) |
