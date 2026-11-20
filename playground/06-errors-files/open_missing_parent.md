# `open(path, "w")` and missing folders

Demo: `uv run python playground/06-errors-files/open_missing_parent.py`

```mermaid
flowchart TD
    A["open('test/notes.txt', 'w')"] --> B{"Does folder test/ exist?"}
    B -- no --> C["FileNotFoundError<br/>No such file or directory"]
    B -- yes --> D{"Does notes.txt exist?"}
    D -- no --> E["Create notes.txt"]
    D -- yes --> F["Empty it (overwrite)"]
    C -. fix .-> G["path.parent.mkdir(parents=True, exist_ok=True)"]
    G --> A
```

*Caption: "w" mode can create the file, but never the folders above it.*

A relative path like `./test` starts from the folder you **run** Python
from (the current working directory), not from the folder the `.py` file
lives in.
