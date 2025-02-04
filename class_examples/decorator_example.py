from functools import wraps

# Original decorator implementation

def hello(text):
    return f"Hello, {text}"

def italic(f):
    def wrapper(text):
        return f(f"<i>{text}</i>")
    return wrapper

hello_italic = italic(hello)
print(hello_italic("Tony"))

# Version using Python wraps from functools

def italic(f):
    @wraps(f)
    def wrapper(text):
        return f(f"<i>{text}</i>")
    return wrapper

@italic
def hello(text):
    return f"Hello, {text}"

print(hello("Tony"))