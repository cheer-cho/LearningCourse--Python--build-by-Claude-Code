"""Why `find_py_files` wraps `folder.glob(...)` in `sorted(...)`.

Run: uv run python playground/06-errors-files/glob_iterator.py
"""

import tempfile
from pathlib import Path

folder = Path(tempfile.mkdtemp())
for name in ["b.py", "a.py", "B.py", "notes.txt"]:
    (folder / name).touch()

# 1. glob returns a lazy iterator, not a list.
matches = folder.glob("*.py")
print("1. glob returns:", type(matches).__name__)

# 2. Each item is a full Path: folder / name is already joined.
first = next(folder.glob("*.py"))
print("2. item type:", type(first).__name__, "| parent is folder?", first.parent == folder)

# 3. An iterator never equals a list, even with the same items in the same order.
expected = sorted([folder / "B.py", folder / "a.py", folder / "b.py"])
print("3. iterator == list?", folder.glob("*.py") == expected)

# 4. An iterator is single-use: the second pass is empty.
once = folder.glob("*.py")
print("4. first pass: ", [p.name for p in once])
print("   second pass:", [p.name for p in once])

# 5. glob order is whatever the OS gives; sorted() makes it deterministic.
print("5. raw glob order:", [p.name for p in folder.glob("*.py")])
print("   sorted:        ", [p.name for p in sorted(folder.glob("*.py"))])

# 6. Paths sort by string, so capitals come first. Use key= for case-insensitive.
print(
    "6. case-insensitive:",
    [p.name for p in sorted(folder.glob("*.py"), key=lambda p: p.name.lower())],
)

# 7. sorted() fixes it all: consumes the iterator, orders it, returns a real list.
result = sorted(folder.glob("*.py"))
print("7. sorted returns:", type(result).__name__, "| == expected?", result == expected)
