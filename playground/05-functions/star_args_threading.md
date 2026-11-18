# Threading a value through `*funcs`

Run: `uv run python playground/05-functions/star_args_threading.py`

## What "thread through" means

```mermaid
flowchart LR
    V["value = 3"] --> F1["lambda x: x + 1"]
    F1 -- "4" --> F2["lambda x: x * 2"]
    F2 -- "8" --> R["return 8"]
```
*Each function's output is the next function's input. The last output is the answer.*

## Star when defining vs star when calling

```mermaid
flowchart TB
    subgraph DEF["def apply_all(value, *funcs)  — star PACKS"]
        A["apply_all(3, f1, f2, f3)"] --> T["funcs = (f1, f2, f3)<br/>one tuple"]
    end
    subgraph CALL["at the call site — star SPREADS"]
        L["rest = [f2, f3]"] --> N["apply_all(x, rest)<br/>→ funcs = ([f2, f3],)<br/>1 arg: a list ❌"]
        L --> S["apply_all(x, *rest)<br/>→ funcs = (f2, f3)<br/>2 args ✅"]
    end
```
*In a `def`, `*` collects separate arguments into one tuple. In a call, `*` unpacks a list or tuple back into separate arguments.*

## Annotating `*args`

The annotation on `*funcs` describes **one item**, not the whole tuple:

| TypeScript | Python |
|---|---|
| `...funcs: Fn[]` (annotates the array) | `*funcs: Callable[[Any], Any]` (annotates each item) |

`*funcs: list[Callable]` means "every argument is itself a list", which is wrong.

Check it with mypy: `uv run mypy playground/05-functions/star_args_hints.py`

```
def total(*nums: int)        -> nums is tuple[int, ...]
def wrong(*nums: list[int])  -> nums is tuple[list[int], ...]
```

`Callable` has two slots: `Callable[[arg types], return type]`. `...` in the
first slot means "any arguments". The return slot can never be left empty.

## Recursion vs loop: same values, different machinery

```mermaid
flowchart TB
    subgraph REC["Recursion: one new call per function"]
        R1["apply_all(3, f1, f2)"] --> R2["apply_all(4, f2)"] --> R3["apply_all(8)"] --> R4["return 8"]
    end
    subgraph LOOP["Loop: one call, one variable updated in place"]
        L0["value = 3"] --> L1["pass 1: value = f1(value) → 4"] --> L2["pass 2: value = f2(value) → 8"] --> L3["return value"]
    end
```
*Both produce 8. The recursive version stacks up one frame per function, so
around 1000 functions raise `RecursionError`. The loop reuses one name.*

## Don't mix the two

```mermaid
flowchart LR
    Q{"How do I reach<br/>the next function?"} -- recursion --> R["func, *rest = funcs<br/>call yourself with *rest"]
    Q -- loop --> L["for fn in funcs:<br/>fn already IS the next function"]
    R & L --> X["Pick ONE. Doing both means each pass<br/>also starts a full recursive chain"]
```
*A loop and recursion are two ways of doing the same walk. Using both at once
does the work over and over: 8 functions make 623,530 calls
(`hybrid_call_count.py`).*
