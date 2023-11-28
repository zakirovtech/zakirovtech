class SecConverter:
    """Класс конвертер секунд в дни:часы:минуты:секунды."""
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise AttributeError('Секунды должны принимать целочисленное значение!')
        self.seconds = seconds

    def get_time(self):
        s = self.seconds % 60  # Целые числа уйдут в минуты, остаток в секундах
        m = (self.seconds // 60) % 60  # Целые числа уйдут в часы, остаток в минутах
        h = (self.seconds // 3600) % 24  # Целые числа уйдут в дни, остаток в часах
        d = self.seconds // self.__DAY
        return f'{d}:{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):  # instance = instance + 100 --> instance.__add__(other)
        if not isinstance(other, (int, SecConverter)):
            raise ArithmeticError('Операнд должен иметь целочисленный тип или тип Clock!')

        item = other
        if isinstance(item, SecConverter):  # instance3 = instance1 + instance 2 - сложение двух экземпляров между собой
            item = other.seconds

        return SecConverter(self.seconds + item)

    def __radd__(self, other):  # instance = other + instance
        return self + other

    def __iadd__(self, other):  # instance += other
        if not isinstance(other, (int, SecConverter)):
            raise ArithmeticError('Операнд должен иметь целочисленный тип или тип Clock!')

        item = other
        if isinstance(item, SecConverter):  # instance3 = instance1 + instance2 -- сложение двух экземпляров между собой
            item = other.seconds
        self.seconds += item
        return self

    def __sub__(self, other):
        ...

    def __mul__(self, other):
        ...

    def __truediv__(self, other):
        ...

    def __mod__(self, other):
        ...


if __name__ == '__main__':
    c1 = SecConverter(86400001)
    c2 = SecConverter(1800)
    c1 = 3600 + c1  # срабатывает _radd_()
    c2 += 3600  # срабатывает _iadd_()
    c3 = c1 + c2  # срабатывает _add_() с проверкой на класс
    print(c3.get_time())
