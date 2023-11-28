import datetime


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # вызывается конструктор следующего базового класса, а не object.
        self.name = name
        self.weight = weight
        self.price = price

    def print_data(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    """Важно, чтобы класс примесь не наследовался ни от кого..."""
    ID = 0

    def __init__(self):
        """Важно, чтобы конструктор миксина принимал только один параметр..."""
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def print_log(self):
        print(f'Товар {self.id} быд продан {datetime.datetime.now()} ')


class Notebook(Goods, MixinLog):
    pass


if __name__ == '__main__':
    n1 = Notebook("Acer", 2, 3000)
    n2 = Notebook('Asus', 3, 1200)
    n1.print_log()
    n2.print_log()
