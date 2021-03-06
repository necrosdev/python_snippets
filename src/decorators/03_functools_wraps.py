import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(name):
    msg = f"Hello {name}"
    print(msg)
    return msg


greet("cuak")
