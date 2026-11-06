# The four set operators side by side, using the ex04 interests example.
# Run: uv run python playground/04-collections/set_operators.py

alice = {"chess", "hiking"}
bob = {"hiking", "reading"}

print("alice | bob =", alice | bob)  # union: in either
print("alice & bob =", alice & bob)  # intersection: in both
print("alice - bob =", alice - bob)  # difference: in alice only
print("alice ^ bob =", alice ^ bob)  # symmetric difference: in exactly one

# ^ is "union minus intersection", or "each side's leftovers, combined"
assert alice ^ bob == (alice | bob) - (alice & bob)
assert alice ^ bob == (alice - bob) | (bob - alice)

# Unlike -, ^ is symmetric: swapping the sides gives the same answer
print("bob - alice =", bob - alice, "  (not the same as alice - bob)")
print("bob ^ alice =", bob ^ alice, "  (same as alice ^ bob)")
