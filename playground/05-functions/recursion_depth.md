# Recursion depth: length vs nesting

Demo: `uv run python playground/05-functions/recursion_depth.py`

Python has no tail-call optimization. Every recursive call adds a stack
frame, and the default limit is about 1000 frames.

```mermaid
flowchart TB
    subgraph A["Head/tail: frames grow with LENGTH"]
        a1["f([1,2,3,…,5000])"] --> a2["f([2,3,…,5000])"] --> a3["f([3,…,5000])"] --> a4["… 5000 frames 💥"]
    end
    subgraph B["Recurse only into sublists: frames grow with NESTING"]
        b1["f([1,[2,[3]],4])"] -->|"item is a list"| b2["f([2,[3]])"] -->|"item is a list"| b3["f([3])"]
        b1 -.->|"plain items: no new frame"| bx["1, 4"]
    end
```

*Caption: A flat list of 5000 items is only 1 level deep. If each item
costs a frame, it still overflows. Spend a frame only when you go one
level deeper.*

| Strategy | Stack depth | Copies per call |
|---|---|---|
| `first, *rest` head/tail | length of list | whole tail (O(n²) total) |
| recurse only on nested lists | nesting depth | none |

**Rule of thumb:** use recursion for the *shape* of the data (depth) and
iteration for its *size* (breadth). (Coming from TypeScript: JS engines
mostly skip TCO too, so you'd hit the same wall there.)
