class Geom:
    NAME = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self._fill = True

    def get__coords(self):
        return self._x1, self._y1, self._x2, self._y2


if __name__ == '__main__':
    r = Rect(0, 0, 10, 20)
    print(r.__dict__)  # Приватные свойства объекта субкласса носят префикс родителя {..., _Geom__x1, ...}
    print(r.get__coords())
