# Tuple sort keys — "sort by A, then by B"

A tuple key sorts by its first item. It only looks at the next item when
the first items tie. That's how a phone book works: last name first, then
first name for people with the same last name.

```mermaid
flowchart TD
    A["Compare two keys:<br/>(last₁, first₁) vs (last₂, first₂)"] --> B{"last₁ == last₂?"}
    B -- No --> C["Order decided by last name"]
    B -- Yes --> D{"first₁ == first₂?"}
    D -- No --> E["Order decided by first name"]
    D -- Yes --> F["Equal — keep original order<br/>(sorted is stable)"]
```

*Caption: Python compares tuples left to right; later items only break ties.*

Runnable demo: [tuple_sort_keys.py](tuple_sort_keys.py)

## Not special syntax — just `key=` + tuple `<`

```mermaid
flowchart LR
    A["record"] -->|"key(record)"| B["key value<br/>(int, str, tuple...)"]
    B -->|"compared with <"| C["sorted order"]
```

*Caption: `sorted` only asks "is key A < key B?" — the key's type decides what `<` means. Tuples define `<` item by item.*
