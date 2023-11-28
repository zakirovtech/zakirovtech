import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count(self):
        s = self.x + self.y
        for i in range(1000):
            s += 1


class Point2D:
    __slots__ = ('x', 'y')  # Названия допустимых ЛОКАЛЬНЫХ атрибутов.

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count(self):
        s = self.x + self.y
        for i in range(1000):
            s += 1


class Point3D(Point2D):
    pass


if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point2D(10, 20)
    del p2.x
    p2.x = 10
    # p2.z = 30  # Attribute Error

    p3 = Point3D(10, 20)
    print(p3.x)
    p3.z = 30  # Ошибки не будет, так как не наследуется __slots__.
    print(p3.__dict__)  # Перечисленные в __slots__ имена отсутствуют
