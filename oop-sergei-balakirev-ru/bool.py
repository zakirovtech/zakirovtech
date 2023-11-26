class Point:
    BOOL_DEFINE = False  # Поменяй состояние, чтобы увидеть, когда срабатывает __len__, когда __bool__

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ is calling')
        return self.x ** 2 + self.y ** 2

    if BOOL_DEFINE:
        def __bool__(self):
            """Переопределили метод таким образом, что логическое состояние объекта определяется в зависимости
            от значения заданных локальных свойств.
            Если равны True и наоборот."""
            print('__bool__ is calling')
            return self.x == self.y


if __name__ == '__main__':
    p = Point(12, 10)
    print(bool(p))
    print(bool(p))  # Локальные свойства не равны -- False.

    if p:
        print('переданные данные равны')
    else:
        print('переданные данные НЕ равны')
