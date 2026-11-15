# Scope, `global`, `nonlocal`, closures — diagrams

Runnable companions: `legb_global_nonlocal.py` and `closure_cells.py`.

## 1. Is `x` local? Python decides before the function runs

```mermaid
flowchart TD
    A["Function body uses name x"] --> B{"Is x assigned anywhere<br/>in this body?"}
    B -- No --> C["x is looked up via LEGB<br/>(read-only access to outer x)"]
    B -- Yes --> D{"Declared global x<br/>or nonlocal x?"}
    D -- No --> E["x is LOCAL for the whole body"]
    D -- "global x" --> F["x means the module-level x"]
    D -- "nonlocal x" --> G["x means the enclosing function's x"]
    E --> H{"Read before the<br/>first assignment?"}
    H -- Yes --> I["UnboundLocalError"]
    H -- No --> J["Works: a new local,<br/>outer x untouched"]
```

*What to notice: a single assignment anywhere in the body makes the
name local everywhere in that body.*

## 2. Where each keyword points

```mermaid
flowchart LR
    subgraph Module["module (Global)"]
        G["debug = False"]
        subgraph Outer["def make_limiter() (Enclosing)"]
            E["remaining = 2"]
            subgraph Inner["def allow() (Local)"]
                N["nonlocal remaining"]
            end
        end
        subgraph Other["def enable_debug()"]
            K["global debug"]
        end
    end
    N -. rebinds .-> E
    K -. rebinds .-> G
```

*What to notice: `nonlocal` goes up one function and stops there.
`global` jumps straight to the module.*

## 3. Each factory call gets its own cell

```mermaid
flowchart LR
    F["make_step_counter(step)"] -- "step=1" --> A["by_one"]
    F -- "step=10" --> B["by_ten"]
    A --> C1[("cells: step=1, value")]
    B --> C2[("cells: step=10, value")]
```

*What to notice: calling `by_one()` never changes `by_ten`'s cells.*
