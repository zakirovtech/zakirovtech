import inspect
from typing import Callable, Generator


class CustomException(Exception):
    """Some Exception description"""


def coroutine(gen_foo: Callable):
    """Coroutine init decorator..."""
    def wrapper(*args, **kwargs):
        gen = gen_foo(*args, **kwargs)  # generator object
        gen.send(None)  # init
        return gen
    return wrapper


def gen_average():
    average = 0
    count = 0
    summ = 0
    while True:
        try:
            item = yield
            if isinstance(item, int):
                summ += item
                count += 1
                average = round(summ / count)
        except StopIteration:
            break
    return average  # результат обработается в делегирующем генераторе...
    # если не использовать yield from нужно было бы перехватывать StopIteration, и забирать return через value...


@coroutine
def translator(subgen: Generator):
    """Delegating generator --- живет пока есть ресурсы у подгенератора..."""
    res = yield from subgen  # yield from обрабатывает return в подгенераторе | await in asyncio from Python 3.5
    if res:
        yield res


if __name__ == '__main__':
    sub = gen_average()
    main = translator(sub)
    main.send(1)
    main.send(2)
    main.send(3)
    main.send(4)
    main.send(5)
    result = main.throw(StopIteration)
    print(result)
    main.send(2)
