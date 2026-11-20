# pytest's `tmp_path` fixture

Demo: `uv run pytest playground/06-errors-files/test_tmp_path_demo.py -s`

```mermaid
flowchart TD
    A["pytest sees a test function<br/>def test_x(tmp_path)"] --> B{"Is a parameter named<br/>like a fixture?"}
    B -- "yes: tmp_path" --> C["pytest makes a new empty folder<br/>/tmp/pytest-of-you/pytest-N/test_x0/"]
    C --> D["Passes it in as a pathlib.Path"]
    D --> E["Test runs: tmp_path / 'notes.txt'"]
    E --> F["Test ends: folder is left alone<br/>(pytest keeps the last 3 runs, deletes older ones)"]
```

*Caption: pytest matches the parameter name `tmp_path` to a built-in fixture,
creates a fresh folder for that one test, and hands it in as a `Path`.*

| Without `tmp_path` | With `tmp_path` |
|---|---|
| Tests write into your real project folder | Tests write into a throwaway folder |
| Leftover files leak into the next test | Every test gets its own empty folder |
| You must clean up by hand | pytest cleans up old runs for you |
