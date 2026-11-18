# Any regular parameter can be passed by name, in any order.
def greet(name, greeting="Hi", punct="!"):
    return f"{greeting}, {name}{punct}"


print(greet("Ada"))                          # all positional
print(greet(name="Ada", greeting="Yo"))      # all keyword
print(greet(punct="?", name="Ada"))          # keyword order doesn't matter
print(greet("Ada", punct="?"))               # skip greeting, keep its default

try:
    eval('greet(name="Ada", "Yo")')          # positional AFTER keyword
except SyntaxError as e:
    print("SyntaxError:", e.msg)
