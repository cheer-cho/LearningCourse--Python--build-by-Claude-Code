"""Root pytest conftest.

Every module folder (``01-setup-tooling/``, ``02-values-variables/``, ...)
holds a ``checkpoint_NN.py`` at its root and exercise files under
``exercises/``. Tests import those directly, e.g.
``from ex01_hello import greet`` or ``from checkpoint_02 import ...``.

For that to work, each module dir AND its ``exercises/`` subdir must be on
``sys.path``. We do that once, here, at collection time. This is safe only
because CONVENTIONS.md enforces course-wide unique filenames for every
importable module (``exNN_<topic>.py``, ``checkpoint_NN.py``).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

for module_dir in sorted(ROOT.glob("[0-9][0-9]-*")):
    if not module_dir.is_dir():
        continue
    for candidate in (module_dir, module_dir / "exercises"):
        if candidate.is_dir():
            path_str = str(candidate)
            if path_str not in sys.path:
                sys.path.insert(0, path_str)
