# for/else with an empty list: the loop body never runs, so break never runs.
# Run: uv run python playground/03-control-flow/for_else_empty.py

for n in []:
    print("inside loop")  # never printed
    if n % 2 == 0:
        break
else:
    print("no evens found")  # printed! no break happened
