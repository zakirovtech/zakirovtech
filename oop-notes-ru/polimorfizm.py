class Geom:
    """Базовый класс"""
    def get_perimeter(self):
        """"Имитация поведения абстрактного метода"""
        raise NotImplemented(f'Метод не переопределен в {self.__class__} ')


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return self.a * 4


class Rectangle(Geom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return (self.a + self.b) * 2


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self. c


if __name__ == '__main__':
    s = Square(3)
    r = Rectangle(2, 4)
    t = Triangle(2, 3, 5)

    for item in [s, r, t]:
        print(item.get_perimeter())  # Механизм параметрического полиморфизма
