import asyncio


def decorator(*args, **kwargs):
    print(args, kwargs)  # ('test_string',) {'test_kwarg': 'test_kwargs'}

    def wrap(func):
        async def wrapper(*args, **kwargs):
            print(args, kwargs)  # ('Party!',) {}
            return await func(*args, **kwargs)

        return wrapper

    return wrap


@decorator("test_string", test_kwarg="test_kwargs")
async def whee(msg):
    print(f"Whee! {msg}")
    return msg


print(asyncio.get_event_loop().run_until_complete(whee("Party!")))
