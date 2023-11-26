from dataclasses import dataclass, field


class Thing:
    """Пример обычного класса, объекты которого хранят некоторые данные..."""
    def __init__(self, name: str, weight: int, price: float):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = []  # независимая коллекция...

    def __repr__(self):
        """Добавляем более информативный вывод..."""
        return f'Thing: {self.__dict__}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)  # Чтобы создать независимую коллекцию, нужно воспользоваться field()...


if __name__ == '__main__':
    t = Thing('Freezer', 80, 3500)
    td = ThingData('Freezer', 80, 3500)
    td.dims.append(2)
    t.dims.append(1)
    print(t.dims)
    print(td.dims)
    t2 = Thing('Cooler', 8, 500)
    td2 = ThingData('Cooler', 8, 500)
    print(t2.dims)
    print(td2.dims)

