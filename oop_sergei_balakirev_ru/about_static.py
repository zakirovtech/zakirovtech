class Vector:
    MIN_COORD = 0  # Свойства класса с заглавных букв
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """"Метод имеющий доступ только к атрибутам класса"""
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        """Дополнительная функция / сервис, который не имеет доступа ни к каким атрибутам."""
        return x * x + y * y

    def __init__(self, x, y):
        self.x, self.y = 0, 0
        if self.validate(x) and self.validate(y):  # Хорошая практика вызывать метод класса через объект
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y
