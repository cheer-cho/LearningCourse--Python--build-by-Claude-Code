# Anatomy of a custom exception

Runnable demo: `uv run python playground/06-errors-files/custom_exception_anatomy.py`

```python
class InsufficientFunds(Exception):
    def __init__(self, needed, available):
        super().__init__(f"need {needed}, only have {available}")
        self.needed = needed
        self.available = available
```

```mermaid
flowchart TD
    R["raise InsufficientFunds(100, 30)"] --> I["__init__(self, needed=100, available=30)"]
    I --> S["super().__init__('need 100, only have 30')<br/>the Exception part stores the message"]
    I --> A["self.needed = 100<br/>self.available = 30<br/>our own data"]
    S --> O[(one exception object)]
    A --> O
    O --> P["print(e) / str(e)<br/>→ 'need 100, only have 30'<br/>for humans"]
    O --> D["e.needed - e.available<br/>→ 70<br/>for code"]
```

*Caption: one object carries two things. The message (set by
`super().__init__`) is for humans. The attributes (set with `self.x = ...`)
are for code that wants to react.*

| Line | What it does | Who uses it |
|---|---|---|
| `class InsufficientFunds(Exception)` | "is a kind of" Exception, so `raise` and `except` accept it | Python |
| `def __init__(self, needed, available)` | runs when you create it: `InsufficientFunds(100, 30)` | Python |
| `super().__init__(msg)` | gives the message to the parent `Exception` | humans: logs, tracebacks, `print(e)` |
| `self.needed = needed` | stores raw data on the object | code: `e.needed` in an `except` block |

If you forget `super().__init__(msg)`, `str(e)` falls back to the raw
arguments: `'(100, 30)'`. It's not empty, but nobody can read it.
