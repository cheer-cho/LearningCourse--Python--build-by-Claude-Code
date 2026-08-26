"""checkpoint_07_pkg package — public API.

Thin wiring only: re-exports the inventory and reporting functions so
callers write `from checkpoint_07_pkg import add_item, low_stock_report`
etc. The real logic lives in `checkpoint_07.py` at the module root —
edit THAT file, not this package (verify_solutions can only overlay
flat files, not ones nested inside a package).
"""

from checkpoint_07_pkg.inventory import add_item, remove_item, stock_count
from checkpoint_07_pkg.reports import low_stock_report

__all__ = ["add_item", "low_stock_report", "remove_item", "stock_count"]
