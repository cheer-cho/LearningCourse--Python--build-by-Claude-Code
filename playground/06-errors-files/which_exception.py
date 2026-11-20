"""Find out which exception a call raises: run it and look at the type."""

import json

samples = ["not json", "{'single': 'quotes'}", '{"Ada": }', b"\xff\xfe".decode("latin-1")]

for text in samples:
    try:
        json.loads(text)
    except Exception as e:
        print(f"{text!r:28} -> {type(e).__module__}.{type(e).__name__}")

# Where does it sit in the hierarchy? (__mro__ = the class and all its parents)
err_type = type(json.decoder.JSONDecodeError("x", "", 0))
print([cls.__name__ for cls in err_type.__mro__])
print([cls.__name__ for cls in UnicodeDecodeError.__mro__])
