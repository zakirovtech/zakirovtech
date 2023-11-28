class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<instance_{self.name}>_{self.__class__}'

    def __str__(self):
        return self.name


class Point:
    NAME = 'Point'

    def __init__(self, *args):
        self.__coords = args

    def __repr__(self):
        """ Отображение информации о классе в режиме отладки."""
        return f'<instance_{self.NAME}>_{self.__class__}'

    def __str__(self):
        """Отображение информации о классе для пользователя."""
        return self.NAME

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return tuple(map(abs, self.__coords))


if __name__ == '__main__':
    p = Point(1, -2)
    print(p)
    print(len(p), abs(p))
