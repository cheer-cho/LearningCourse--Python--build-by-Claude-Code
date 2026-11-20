"""A value of None in the config: does load_setting return None?"""

import sys

sys.path.insert(0, "06-errors-files/exercises")
from ex05_chaining import load_setting  # noqa: E402

for raw in [{"retries": "3"}, {"retries": "many"}, {"retries": None}]:
    try:
        print(f"{raw!r:22} -> returned {load_setting(raw, 'retries')!r}")
    except Exception as e:
        print(f"{raw!r:22} -> raised {type(e).__name__}: {e}")
