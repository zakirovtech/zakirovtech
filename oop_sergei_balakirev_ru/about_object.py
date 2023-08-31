class Base:
    def __str__(self):
        return 'Redefined __str__()'


class Child(Base):
    ...


if __name__ == '__main__':
    b = Base()
    c = Child()
    print(c.__dir__())  # Child имеет доступ ко всем методам object, через Base.
    print(c.__str__())  # Если в базовом переопределить магические методы, дочерние наследуют их.
    print(issubclass(Child, object))  # True
