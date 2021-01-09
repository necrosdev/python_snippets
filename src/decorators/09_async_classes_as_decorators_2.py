import asyncio
import functools


class DecoClass:
    def __init__(self, *args, **kwargs):
        func = args[0]
        functools.update_wrapper(self, func)
        self.func = func
        self._args = args[1:] if len(args) > 1 else []
        self._kwargs = kwargs

    async def __call__(self, *args, **kwargs):
        return await self.func(*args, **kwargs)


def deco_func(*args, **kwargs):
    func = args[0]
    if callable(func):
        return DecoClass(func)
    else:

        def wrapper(func):
            return DecoClass(func, *args, **kwargs)

        return wrapper


@deco_func
async def func_1(*args, **kwargs):
    print(f"func_1: I'm a decorated function! args={args} kwargs={kwargs}")


@deco_func("deco_arg", deco_kwarg=2)
async def func_2(*args, **kwargs):
    print(f"func_2: I'm a decorated function! args={args} kwargs={kwargs}")


asyncio.get_event_loop().run_until_complete(func_1("arg", kwarg=20))
asyncio.get_event_loop().run_until_complete(func_2("arg", kwarg=30))
