class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # Хешируются локальные свойства объекта, а не объект в целом.


print('about_hash', __name__)
if __name__ == '__main__':
    p1 = Point(1, 2)  # по умолчанию объекты пользовательских классов имеют неизменяемые типы.
    p2 = Point(1, 2)
    print(p1 == p2)
    print(p1 is p2)
    print(id(p1), id(p2))
    print(hash(p1), hash(p2), hash((1, 2)))
