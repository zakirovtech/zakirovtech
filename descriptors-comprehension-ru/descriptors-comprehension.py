from custom_descriptors import NameString, PassportString, PositiveInt, GenderString


class Person:
    name = NameString()
    last_name = NameString()
    age = PositiveInt()
    gender = GenderString()

    def __init__(self, name: str, last_name: str, age: int, gender: str) -> None:
        """Локальные атрибуты создаются через сеттеры соответствующих дескрипторов"""
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    @property
    def main_info(self) -> tuple:
        """Здесь объект property выступает, как вычисляемое значение"""
        return self.name.capitalize(), self.last_name.capitalize(), self.age, self.gender.capitalize()


class Employee(Person):
    passport = PassportString()

    def __init__(self, name: str, last_name: str, age: int, gender: str, passport_data: str) -> None:
        """Здесь паспортные данные создаются без участия дескриптора. Но они доступны только для чтения"""
        super().__init__(name, last_name, age, gender)
        self.__passport = passport_data


if __name__ == '__main__':
    """Entry point for some tests"""
    e1 = Employee("John", "Doe", 14, "Female", "1234567890")
    e1.age = 15  # __set__
    print(e1.age)  # __get__
    print(e1.last_name)
    print(e1.name)
    print(e1.passport)
    print(e1.__dict__)
