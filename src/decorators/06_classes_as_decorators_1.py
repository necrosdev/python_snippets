import functools


class CountCalls:
    def __init__(self, func, *args, **kwargs):
        print(f"args={args} kwargs={kwargs}")
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")


say_whee()
say_whee()
say_whee()
