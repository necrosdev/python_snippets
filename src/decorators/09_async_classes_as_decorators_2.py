import asyncio


class DecoClass:
    def __init__(self, *args, **kwargs):
        print("INIT", args, kwargs)
        self._args = args
        self._kwargs = kwargs

    async def __call__(self, *args, **kwargs):
        print("The call", args, kwargs)
        if len(self._args) == 1 and len(self._kwargs) == 0:
            # No hay argumentos.
            return await self._args[0]()
        else:
            # Si que los hay.
            func = args[0]

            async def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper


@DecoClass
async def fun(*args, **kwargs):
    print(f"I'm a fun decorated function! args={args} kwargs={kwargs}")


@DecoClass("asd", cuak=2)
async def funny(*args, **kwargs):
    print(f"I'm a funny decorated function! args={args} kwargs={kwargs}")


asyncio.get_event_loop().run_until_complete(fun("asd", cuak="qwe"))
asyncio.get_event_loop().run_until_complete(funny("asd", cuak="qwe"))
