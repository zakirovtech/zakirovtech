class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError("Секунды -- целые числа!")
        self.seconds = seconds % self.__DAY

    @staticmethod
    def __verify_data(other):
        if not isinstance(other, (Clock, int)):
            raise AttributeError('Сравнивать можно только int или объект Clock!')
        item = other if isinstance(other, int) else other.seconds
        return item

    def __eq__(self, other):
        item = self.__verify_data(other)
        return self.seconds == item

    def __lt__(self, other):
        item = self.__verify_data(other)
        return self.seconds < item

    def __gt__(self, other):
        item = self.__verify_data(other)
        return self.seconds > item

    def __le__(self, other):
        item = self.__verify_data(other)
        return self.seconds <= item


if __name__ == '__main__':
    c1 = Clock(1000)
    c2 = Clock(1200)
    print(c1 == c2)
    print(c1 == 1200)
    print(1000 == c1)
    print(c1 != c2)  # срабатывает __eq__() применяя инверсию, так как не определен __ne__().
    print(c1 < c2)
    print(c2 < c1)
    print(c1 >= c2)  # срабатывает __le__() применяя инверсию, так как не определен __ge__().
