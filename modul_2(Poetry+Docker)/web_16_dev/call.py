from typing import Callable


Number = int | float  # Union[str, float]


def foo():
    return 'Hello world'


def calc(x: Number, y: Number) -> Number:
    return x + y


def call_func(func: Callable[[], str]) -> int:
    return len(func())


def call_func_1(func: Callable[[Number, Number], Number], a: Number, b: Number ) -> int:
    return func(a, b)


def call_func_2(func: Callable[..., int], *args):
    return func(*args)


if __name__ == '__main__':
    print(call_func(foo))
    print(call_func_1(calc, a=5, b=10))
    print(call_func_2(calc, 5, 5))
