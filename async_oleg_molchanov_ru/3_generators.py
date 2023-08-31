"""Генератор это в первую очередь функция, которая отдает результат при помощи оператора yield и временно передает
контроль управления обратно интерпретатору до следующего вызова генератора. При следующем вызове он продолжит работу с
места остановки, а в случае исполнения всех инструкций и попытке вызвать генератор еще раз, выдаст ошибку
StopIteration...
"""
from typing import Sequence
from time import time


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
fav_months = ['December', 'January', 'July', 'August', 'September', 'October', 'November']


def gen_filename():
    """Также можно создать бесконечный генератор..."""
    i = 1
    while True:
        t = int(time() * 1000)
        yield f"file-{t}.jpeg"
        print(f'Остаток с {i}-й итерации...')  # инструкция отработает при следующем вызове, так как после yield...
        i += 1


# Round Robin --- карусель; генератор выполняет часть работы и встает в конец очереди, пока ресурсы не израсходованы...
def gen_day(week: Sequence):
    for day in week:
        yield day


def gen_month(months: Sequence):
    for month in months:
        yield month


g1 = gen_day(days)
g2 = gen_month(fav_months)


tasks = [g1, g2]  # два генератора выполняются по кругу, пока есть ресурсы...
while tasks:  # пока коллекция не пуста
    task = tasks.pop(0)  # выдергиваем задачу
    try:
        item = next(task)
        print(item)  # пока есть ресурс выполняется инструкция...
        tasks.append(task)  # добавляем задачу на переработку...
    except StopIteration:  # генератор исчерпал ресурсы...
        print('Ресурс генератора исчерпан...')
