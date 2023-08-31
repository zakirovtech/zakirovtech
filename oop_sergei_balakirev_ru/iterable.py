class FloatRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step  # При каждом новой инициализации итератора, значение будет обнуляться
        return self

    def __next__(self):
        if self.value + self.step < self.stop:  # Установка границ окончания итерации / включить правую границу или нет.
            self.value += self.step
            return self.value
        else:
            raise StopIteration


if __name__ == '__main__':
    s = FloatRange(0, 11, 1)

    for item in s:
        print(item)
