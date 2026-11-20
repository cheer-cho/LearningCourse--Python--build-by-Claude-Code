"""writelines does NOT add newlines. It is just write() called on each item.

Run: uv run python playground/06-errors-files/writelines_no_newline.py
"""

import io

f = io.StringIO()                 # a fake file in memory, works like open(...)
f.writelines(["a", "b", "c"])
print(f"1) writelines(['a','b','c'])  -> {f.getvalue()!r}")

f = io.StringIO()
f.writelines("abc")               # a str is an iterable of characters!
print(f"2) writelines('abc')          -> {f.getvalue()!r}")

f = io.StringIO()
for ch in "abc":
    f.write(ch)                   # same as 2): one write per character
print(f"3) write() each char          -> {f.getvalue()!r}")
