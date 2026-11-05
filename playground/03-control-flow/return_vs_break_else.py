# Three ways to write "does this list contain a negative number?"
# Same shape as is_prime: search a loop, stop at the first hit.
# Run: uv run python playground/03-control-flow/return_vs_break_else.py


# --- A: your current style -------------------------------------------
# `return` inside the loop leaves the WHOLE function.
# So the `else` can only run when the loop finished normally...
# ...which is exactly when code after the loop would run anyway.
# The `else` adds nothing.
def has_negative_a(nums: list[int]) -> bool:
    for n in nums:
        if n < 0:
            return True
    else:
        return False


# --- B: quick fix — return, no else ------------------------------------
# Same behaviour as A, one less thing to read.
# The most common Pythonic way when you can return early.
def has_negative_b(nums: list[int]) -> bool:
    for n in nums:
        if n < 0:
            return True
    return False  # only reached if the loop never returned


# --- C: break + else — the pattern ex05 is teaching --------------------
# `break` leaves only the LOOP, not the function.
# So we can't return from inside; we store the answer in a variable.
#   - found a hit  -> set found = True, break  (else is SKIPPED)
#   - no hit       -> loop runs out             (else RUNS)
# Then one return at the end.
def has_negative_c(nums: list[int]) -> bool:
    for n in nums:
        if n < 0:
            found = True
            break
    else:
        found = False
    return found


for nums in ([3, -1, 4], [3, 1, 4], []):
    print(nums, has_negative_a(nums), has_negative_b(nums), has_negative_c(nums))
