from accessify import private


class Point:
    _NAME = 'POINT'

    def __init__(self, x: int, y: int):
        if self.__check_coord(x) and self.__check_coord(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны иметь числовые значения!')

    @private
    @classmethod
    def __check_coord(cls, value):  # Приватный метод класса, который делает валидацию координаты
        return type(value) in (int, float)

    def set_coords(self, x: int, y: int):  # Setter
        if self.__check_coord(x) and self.__check_coord(y):
            self.__x = x  # В пространстве имен класса можно взаимодействовать с приватными атрибутами
            self.__y = y
        else:
            raise ValueError('Координаты должны иметь числовые значения!')

    def get_coords(self):  # Getter
        return self.__x, self.__y


if __name__ == '__main__':
    p = Point(1, 2)  # Инициализация объекта с локальными атрибутами
    print(p._NAME)  # Подсказка, что атрибут является защищенным
    try:
        print(p.__x, p.__y)  # Интерпретатор не находит приватные атрибуты из глобального пространства имен.
    except AttributeError:
        print('Доступ к координате вне класса запрещен')
    # Интерфейсные методы
    p.set_coords(10, 20)  # Переопределение атрибутов с помощью сеттера
    print(p.get_coords())  # (10, 20) Так как атрибуты приватные, доступ к ним можно получить только через геттер.
    print(dir(p))  # Если декорировать приватный метод, он будет в списке. Поэтому лучше применять к публичному методу.
