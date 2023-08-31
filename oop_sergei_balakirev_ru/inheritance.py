class Base:
    NAME = 'Base'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = 0

    def set_attrs(self, x, y):
        print(self.NAME)  # Для каждого дочернего класса будет выведен свой атрибут, так как self принимает их ссылку.
        self.x = x
        self.y = y


class Line(Base):
    NAME = 'Line'

    def foo(self):
        ...


class Rect(Base):
    NAME = 'Rect'

    def foo(self):
        ...


if __name__ == '__main__':
    b = Base()
    line = Line()
    rect = Rect()
    line.set_attrs(1, 2)
    rect.set_attrs(10, 20)
    print(b.__dict__, line.__dict__, rect.__dict__, sep='\n')
