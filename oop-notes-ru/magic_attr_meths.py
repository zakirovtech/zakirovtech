class Point:
    MIN_COORD = 0  # Свойства класса с заглавных букв
    MAX_COORD = 100

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):  # Переопределяем базовый метод
        # Добавляем новый функционал
        print('__getattribute__ is calling for ' + item)  # Строчка, чтобы показать, что метод выполняется при обращении
        # Код ниже закрывает доступ к указанному атрибуту
        if item == 'a':
            raise ValueError('Access to the attribute is denied')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # Добавляем новый функционал
        print(f'__setattr__ is calling for {str(key)} with value {str(value)}')  # Строчка, чтобы показать, что метод выполняется при обращении
        if key == 'z':
            raise AttributeError('Unacceptable attribute name')
        else:
            return object.__setattr__(self, key, value)  # После переопределения нужно не забывать возвращать базовый метод

    def __getattr__(self, item):
        print('__getattr__ is calling for ' + item) # Строчка, чтобы показать, что метод выполняется при обращении
        return False  # Вместо ошибки возвращает ложь

    def __delattr__(self, item):
        # Добавляем новый функционал
        print('__delattr__ is calling for ' + item)
        return object.__delattr__(self, item)


if __name__ == '__main__':
    p = Point(1, 2)  # Инициализация объекта с локальными атрибутами / при инициализации также вызывается __setattr__
    print(p.x)  # Обращение / получение атрибута / вызывается __getattribute__
    p.x = 3  # Переопределение значения атрибута объекта / вызывается __setattr__
    try:
        p.z = 5  # Попытка создания атрибута с таким именем пресекается, так как переопределен __setattr__().
    except AttributeError:
        print('Попытка создания атрибута с таким именем пресекается, так как переопределен __setattr__()')
    print(p.z)  # Попытка обращения к несуществующему атрибуту / вызывается __getattr__().
    del p.x  # Удаление автоматически вызывает __delattr__().
    print(p.__dict__)  # {'y': 2}
