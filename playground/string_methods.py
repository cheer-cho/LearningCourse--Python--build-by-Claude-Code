"""String methods cheat sheet. Run: uv run python playground/string_methods.py

Each line prints `expression=result`, thanks to the f-string `=` spec.
Strings are immutable: every method returns a NEW string.
"""

print("--- case ---")
print(f'{"ada LOVELACE".upper()=}')
print(f'{"ada LOVELACE".lower()=}')
print(f'{"ada LOVELACE".title()=}')
print(f'{"ada LOVELACE".capitalize()=}')
print(f'{"ada LOVELACE".swapcase()=}')

print("\n--- strip: removes a SET of characters from the ends ---")
print(f'{"  hi  ".strip()=}')
print(f'{"  hi  ".lstrip()=}')
print(f'{"  hi  ".rstrip()=}')
print(f'{"$$5".lstrip("$")=}')            # every leading $
print(f'{"xyhiyx".strip("xy")=}')         # any x or y, not the substring "xy"

print("\n--- removeprefix / removesuffix: remove an exact substring, once ---")
print(f'{"$$5".removeprefix("$")=}')      # only one $
print(f'{"report.txt".removesuffix(".txt")=}')
print(f'{"report.txt".removesuffix(".csv")=}')  # no match: unchanged

print("\n--- split & join ---")
print(f'{"  ada   lovelace ".split()=}')     # any whitespace run, ends ignored
print(f'{"  ada   lovelace ".split(" ")=}')  # every single space
print(f'{"a,b,,c".split(",")=}')
print(f'{"a,b,c".split(",", 1)=}')           # at most 1 split
print(f'{"line1\nline2".splitlines()=}')
print(f'{"-".join(["a", "b", "c"])=}')
print(f'{"".join(["a", "b", "c"])=}')

print("\n--- search ---")
print(f'{"banana".count("a")=}')
print(f'{"banana".find("n")=}')       # first index
print(f'{"banana".find("z")=}')       # -1 when missing
print(f'{"nan" in "banana"=}')        # usually what you want instead of find
print(f'{"Ada".startswith("A")=}')
print(f'{"photo.png".endswith((".png", ".jpg"))=}')  # a tuple checks any of them

print("\n--- replace ---")
print(f'{"a-b-c".replace("-", "+")=}')
print(f'{"a-b-c".replace("-", "+", 1)=}')  # only the first one

print("\n--- checks (return bool) ---")
print(f'{"42".isdigit()=}')
print(f'{"-42".isdigit()=}')       # False: "-" is not a digit
print(f'{"abc".isalpha()=}')
print(f'{"abc123".isalnum()=}')
print(f'{"   ".isspace()=}')
print(f'{"Hi".isupper()=}')

print("\n--- padding & alignment ---")
print(f'{"7".zfill(3)=}')
print(f'{"hi".center(8, "*")=}')
print(f'{"hi".ljust(5, ".")=}')
print(f'{"hi".rjust(5, ".")=}')
print(f'{f"{'hi':>5}"=}')          # f-string spec does the same job

print("\n--- length, indexing, repetition ---")
s = "Python"
print(f"{len(s)=}")
print(f"{s[0]=}")
print(f"{s[-1]=}")                 # negative index counts from the end
print(f"{s[0:2]=}")                # slicing: full detail in module 04
print(f'{"ab" * 3=}')
print(f'{"ab" + "cd"=}')

print("\n--- gotcha: methods don't change the original ---")
name = "  ada  "
name.strip()
print(f"{name=}")                  # still has spaces
name = name.strip()                # rebind the name to keep the result
print(f"{name=}")

print("\n--- chaining: order matters ---")
raw = " $12.00 "
print(f'{raw.strip().removeprefix("$")=}')
print(f'{raw.removeprefix("$").strip()=}')  # $ wasn't at the start yet!
