import asyncio


def decorator(*args, **kwargs):
    print(args, kwargs)  # ('asd',) {'cuak': 'asd'}

    def wrap(func):
        async def wrapper(*args, **kwargs):
            print(args, kwargs)  # ('Party!',) {}
            print("Something is happening before the function is called.")
            return await func(*args, **kwargs)
            print("Something is happening after the function is called.")

        return wrapper

    return wrap


@decorator("asd", cuak="asd")
async def whee(msg):
    print(f"Whee! {msg}")
    return msg


print(asyncio.get_event_loop().run_until_complete(whee("Party!")))
