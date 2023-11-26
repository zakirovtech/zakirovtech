from string import ascii_letters


class Person:
    S_RU = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RU_UPPER = S_RU.upper()

    def __init__(self, fio: str, old: int, ps: str, weight: float):
        self.fio = fio
        self.old = old
        self.passport = ps
        self.weight = weight

    # Блок методов проверки вводимых данных
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        fio_list = fio.split()
        if len(fio_list) != 3:
            raise TypeError('Неверный формат ФИО')
        allowed_chars = cls.S_RU + cls.S_RU_UPPER + ascii_letters
        for item in fio_list:
            if len(item) < 1:
                raise TypeError('Каждый элемент ФИО должен содержать содержать символы')
            if len(item.strip(allowed_chars)) > 0:
                raise TypeError('В ФИО можно использовать буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or 14 > old or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14 - 120]")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должен быть вещественным числом не меньше 20")

    @classmethod
    def verify_passport(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        if len(ps) != 11 or ps.count(' ') != 1 or ps.index(' ') != 4:
            raise TypeError("Неверный формат паспорта")
        if not ps.replace(' ', '').isdigit():
            raise TypeError("Серия и номер паспорта должны быть числами")

    # Объекты property
    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)  # Проверка на корректность данных
        self.__fio = fio.split()

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)  # Проверка на корректность данных перед переопределением свойства
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_passport(ps)  # Проверка на корректность данных
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)  # Проверка на корректность данных
        self.__weight = weight


if __name__ == '__main__':
    p = Person('Doe John Unknown', 14, '1234 567890', 80.0)
    print(p.__dict__)
    p.fio = 'Doe Jane Unknown'
    p.old = 29
    p.passport = '4567 123890'
    p.weight = 69.0
    p._Person__weight = 49
    print(p.weight)
    print(p.__dict__)
