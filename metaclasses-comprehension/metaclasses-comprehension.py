# Динамическое создание класса
Point = type("Point", (), {"x": 1, "y": 2})
p = Point()

print(type(p))
print(type(Point))


class Singleton(type):
    """Custom metaclass"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """При каждом вызове класса, активируется __call__()"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        
        return cls._instances[cls]


class EternalPoint(object, metaclass=Singleton):
    def __init__(self, x: int, y: int):
        self.x, self. y = x, y


p1 = EternalPoint(1, 2)
p2 = EternalPoint(1, 3)

print(id(p1))
print(id(p2))

print(p1.__dict__)
print(p2.__dict__)
