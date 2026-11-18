# Set methods: which one do I want?

```mermaid
flowchart TD
    Q{What do you want to do?} --> Add[Add items]
    Q --> Rem[Remove items]
    Q --> Cmp[Compare two sets]
    Q --> Comb[Combine two sets]
    Add --> A1["one item → add(x)"]
    Add --> A2["many items → update(iterable)"]
    Rem --> R1{"Is a missing item a bug?"}
    R1 -- yes --> R2["remove(x) → KeyError"]
    R1 -- no --> R3["discard(x) → silent"]
    Cmp --> C1["issubset / issuperset / isdisjoint → bool"]
    Comb --> K1{"Change the original set?"}
    K1 -- "no, give me a new set" --> K2["union / intersection /<br/>difference / symmetric_difference"]
    K1 -- "yes, in place" --> K3["update / intersection_update /<br/>difference_update / symmetric_difference_update"]
```

_Caption: pick a set method by the question you are asking. Combining
methods come in pairs: one returns a new set, its `_update` twin changes
the set in place and returns `None`._

Runnable demo: `uv run python playground/04-collections/set_methods.py`
