"""Path(".") is where you RAN python from. Path(__file__).parent is where this FILE lives.

Run it from two different places and compare:
    uv run python playground/06-errors-files/dot_vs_file_dir.py
    cd playground && uv run python 06-errors-files/dot_vs_file_dir.py
"""

from pathlib import Path

print(f'Path(".")              -> {Path(".").resolve()}')
print(f"Path.cwd()             -> {Path.cwd()}")
print(f"Path(__file__).parent  -> {Path(__file__).resolve().parent}")
