class CountCalls:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self._args = args
        self._kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if len(self._args) == 1 and len(self._kwargs) == 0:
            # No tiene argumentos el decorador.
            return self._args[0]()

        else:
            # Tiene argumentos.
            func = args[0]

            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper


@CountCalls
def say_whaa():
    print("Whaa!")


@CountCalls
def say_whee(*args, **kwargs):
    print(f"Whee! args={args} kwargs={kwargs}")


@CountCalls(cuak=2)
def say_whoo(*args, **kwargs):
    print(f"Whoo! args={args} kwargs={kwargs}")


say_whaa()
say_whee()
say_whoo()
