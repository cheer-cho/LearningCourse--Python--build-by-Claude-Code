"""mod07_geo package — the LEARNING TARGET of ex04.

Thin wiring only — edit `ex04_init_api.py` (flat, in exercises/), not
this file (same "_impl" reason as `mod07_shop/`: verify_solutions can
only overlay flat files).

This re-exports every name listed in `ex04_init_api.__all__`, WITHOUT
using `from ex04_init_api import *`. That's the point: `__all__` is how
a module author decides its public API on purpose, name by name,
instead of leaving it to whatever `import *` happens to grab.
"""

import ex04_init_api as _impl

for _name in _impl.__all__:
    globals()[_name] = getattr(_impl, _name)

__all__ = list(_impl.__all__)
