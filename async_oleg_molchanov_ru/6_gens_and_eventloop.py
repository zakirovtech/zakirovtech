"""Нужно понимать, что в основе асинхронности лежит концепция генераторов и корутин, а также событийного цикла, который
определяет какую задачу, в какой момент выполнять. Не нужно думать, что синтаксис async / await автоматически делает
функцию асинхронной. Это лишь более высокоуровневый синтаксис, разработанный для удобства разработки.
Асинхронное выполнение двух функций, без использования модуля asyncio...
2 генератора и eventloop.
"""
import time
from collections import deque


def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield  # передает контроль управления в глобальную область


def print_message():
    count = 0
    while True:

        print('Some message')

        count += 1
        yield


def main():
    while True:
        task = tasks.popleft()
        next(task)
        tasks.append(task)



if __name__ == '__main__':
    tasks = deque()
    c = counter()  # объект генератора counter
    tasks.append(c)
    p = print_message()  # объект генератора print_message
    tasks.append(p)
    main()
