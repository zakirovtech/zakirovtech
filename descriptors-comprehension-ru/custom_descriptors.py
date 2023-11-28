"""Создание, чтение, удаление атрибутов происходит через эти классы. Добавляются некоторые ограничения и валидация.
Не стал добавлять документацию к каждому классу, так как интуитивно понятно "что за что" отвечает."""


class PositiveInt:
    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self._name, value)
        else:
            raise ValueError("Value must be only positive integer")

    def __delete__(self, instance):
        pass

    def __set_name__(self, owner, name):
        self._name = "_" + name


class GenderString:
    GENDERS = ["Male", "Female"]

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if value in self.GENDERS:
            setattr(instance, self._name, value)
        else:
            raise AttributeError("You specified not existing gender")

    def __delete__(self, instance):
        pass

    def __set_name__(self, owner, name):
        self._name = "_" + name


class NameString:
    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        setattr(instance, self._name, value)

    def __delete__(self, instance):
        pass

    def __set_name__(self, owner, name):
        self._name = "_" + name


class PassportString:
    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        raise AttributeError("Passport information must not be changed")

    def __delete__(self, instance):
        pass

    def __set_name__(self, owner, name):
        self._name = "_" + owner.__name__ + "__" + name
