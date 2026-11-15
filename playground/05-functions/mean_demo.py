"""Is there a built-in mean()? No — but the standard library has one."""

from statistics import mean, median, mode

scores = [90, 72, 85, 72, 100]

# 1. statistics.mean — the idiomatic answer
print("mean:  ", mean(scores))
print("median:", median(scores))
print("mode:  ", mode(scores))

# 2. The do-it-yourself version (sum and len ARE built-ins)
print("manual:", sum(scores) / len(scores))

# 3. Empty input: the two approaches fail differently
try:
    mean([])
except Exception as e:
    print("mean([]) ->", type(e).__name__, "-", e)

try:
    sum([]) / len([])
except Exception as e:
    print("sum/len on [] ->", type(e).__name__, "-", e)
