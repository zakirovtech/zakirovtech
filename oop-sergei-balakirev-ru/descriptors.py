
class Integer:  # Класс дескриптор-данных
    @classmethod
    def verify_coord(cls, coord):
        """Валидатор"""
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        """Принимает ссылку на объект-дескриптор - self, на класс где он будет объявлен - owner и
        имя со ссылкой на объект-дескриптор - name, на основе которого создается локальное свойство объекта-дескриптора.
        """
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        """Магический getter, который возвращает локальное свойство экземпляра класса, где объявлен объект-дескриптор.
        """
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Принимает ссылку на объект-дескриптор - self, на экземпляр класса, где объявлен объект-дескриптор - instance
         и значение, переданное в инициализатор при создании этого экземпляра - value.
         Далее создает локальный атрибут экземпляра класса, используя setattr(). В качестве имени назначается
         локальное свойство объекта-дескриптора."""
        self.verify_coord(coord=value)  # Проверка перед назначением.
        setattr(instance, self.name, value)


class Point3D:
    """При создании объекта-дескриптора срабатывает метод __set_name__(). X это имя, которое принимает ссылку на
    объект-дескриптор и передается в __set_name__() и представляет собой атрибут класса."""
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z, a):
        """Параметры переданные в  __init__() передаются в __set__() как value"""
        self.x = x
        self.y = y
        self.z = z
        self.__a = a


if __name__ == '__main__':
    p = Point3D(10, 20, 30, 1)
    print(p.__dict__)
    print(p.x)
    p.x = 45
    print(p.x)
    print(p.__dict__)

