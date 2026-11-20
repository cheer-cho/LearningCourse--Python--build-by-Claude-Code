"""What happens when an exception is raised but no `except` matches it?"""


def run(value: str) -> None:
    print(f"\n--- run({value!r}) ---")
    try:
        print("try: start")
        if value == "type":
            raise TypeError("not handled here!")  # no except matches this
        number = int(value)  # may raise ValueError
        print("try: end")
    except ValueError:
        print("except ValueError: handled")
    else:
        print(f"else: success, got {number}")
    finally:
        print("finally: always runs")
    print("after the try statement")  # only reached if nothing escaped


run("42")    # no error       -> try, else, finally, after
run("abc")   # matched error  -> try, except, finally, after
try:
    run("type")  # unmatched  -> try, finally, then the TypeError escapes
except TypeError as exc:
    print(f"caller caught: {exc!r}")
