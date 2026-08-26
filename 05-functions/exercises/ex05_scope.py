# Scenario: LEGB name-lookup drills, a nonlocal-based counter, and a
# global-scope bug to fix. Concepts: Local/Enclosing/Global/Builtins
# lookup order, `global`, `nonlocal`.
# Run: uv run pytest 05-functions -k ex05

LEVEL = "global"
total_clicks = 0


def shadowed_local():
    """LEGB prediction: a module-level `LEVEL = "global"` is defined
    above. Define a LOCAL variable also named `LEVEL`, set it to
    `"local"`, and return it — a local name always shadows a global one
    of the same name inside its own function.

    shadowed_local() -> "local"
    """
    raise NotImplementedError


def read_global_total():
    """LEGB prediction: `total_clicks` is defined at module scope above,
    currently `0`. Reading a global needs no special keyword — just use
    the name. Return `total_clicks + 1` (do NOT reassign `total_clicks`
    here).

    read_global_total() -> 1
    """
    raise NotImplementedError


def make_id_generator(start=1):
    """Return a zero-argument function that returns `start`, then
    `start + 1`, then `start + 2`, ... on each successive call — using
    a `nonlocal` counter captured in a closure (no module-level state).

    next_id = make_id_generator()
    next_id() -> 1
    next_id() -> 2
    next_id() -> 3

    other = make_id_generator(100)
    other() -> 100   # a separate, independent counter
    """
    raise NotImplementedError


def register_click():
    """BUG: this should increment the module-level `total_clicks`
    counter and return the new value. As written, it's missing the
    `global` declaration — because this function ASSIGNS to
    `total_clicks`, Python treats it as a brand-new LOCAL variable for
    the whole function body, so the line below tries to read a local
    `total_clicks` that doesn't exist yet and raises UnboundLocalError.
    Add the missing `global total_clicks` declaration to fix it.

    starting from total_clicks == 0:
    register_click() -> 1
    register_click() -> 2   (called again right after, keeps counting)
    """
    total_clicks = total_clicks + 1
    return total_clicks
