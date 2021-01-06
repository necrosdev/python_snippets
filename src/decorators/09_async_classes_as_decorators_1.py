import asyncio
import functools


class DecoClass:
    def __init__(self, func, *args, **kwargs):
        print("The init", func, args, kwargs)
        functools.update_wrapper(self, func)
        self.func = func

    async def __call__(self, *args, **kwargs):
        print("The call", args, kwargs)
        return await self.func(*args, **kwargs)


@DecoClass
async def function(*args, **kwargs):
    print(f"I'm a decorated function! args={args} kwargs={kwargs}")


asyncio.get_event_loop().run_until_complete(function("asd", cuak="qwe"))
