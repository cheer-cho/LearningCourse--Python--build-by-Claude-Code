"""open(path, "w") creates the FILE, but never the FOLDERS above it.

Run: uv run python playground/06-errors-files/open_missing_parent.py
"""

import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp())          # an empty scratch folder
path = root / "test" / "notes.txt"       # "test/" does not exist yet

try:
    with open(path, "w", encoding="utf-8") as f:
        f.write("hi\n")
except FileNotFoundError as e:
    print(f"1) FileNotFoundError: {e.strerror}")

path.parent.mkdir(parents=True, exist_ok=True)   # make the folder first
with open(path, "w", encoding="utf-8") as f:
    f.write("hi\n")
print(f"2) after mkdir: {path.read_text(encoding='utf-8')!r}")

print(f"3) './test' means: {Path('./test').resolve()}")
