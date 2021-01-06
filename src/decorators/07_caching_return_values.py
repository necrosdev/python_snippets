import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())

        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# fibonacci(cuak=10)


@functools.lru_cache(maxsize=4)
def lru_fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return lru_fibonacci(num - 1) + lru_fibonacci(num - 2)


print("Start number 10", lru_fibonacci(10))
print("Start number 8", lru_fibonacci(8))
print("Start number 5", lru_fibonacci(5))
print("Start number 8", lru_fibonacci(8))
print("Start number 5", lru_fibonacci(5))
print("Start number 8", lru_fibonacci(8))
print("Start number 5", lru_fibonacci(5))
