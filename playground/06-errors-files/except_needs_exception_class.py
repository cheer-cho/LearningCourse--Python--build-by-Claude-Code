"""`except X` only works if X is an exception class, and Python checks that late."""

import json

print(issubclass(json.JSONEncoder, BaseException))     # False: it's the encoder tool
print(issubclass(json.JSONDecodeError, BaseException))  # True: it's an error

# The bad clause is harmless... until something is actually raised.
try:
    pass
except json.JSONEncoder:
    pass
print("no error raised -> bad except clause never checked")

try:
    json.dumps({"s": {1, 2}})  # a set isn't JSON-serializable
except json.JSONEncoder:
    pass
