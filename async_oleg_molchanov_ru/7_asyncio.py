"""Реализация асинхронного выполнения двух функций, используя модуль asyncio..."""
import asyncio
from collections import deque


async def counter():  # в Python 3.4 использовался декоратор @asyncio.coroutine
    count = 0
    while True:
        print(count)
        count += 1
        await asyncio.sleep(0.1)  # корутины запускаются через await | Python 3.4 yield from


async def print_message():
    count = 0
    while True:
        if count % 3 == 0:
            print('Some message')
        count += 1
        await asyncio.sleep(0.1)


async def main():
    tasks = deque()
    tasks.append(counter())
    tasks.append(print_message())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
