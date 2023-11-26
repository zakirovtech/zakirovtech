
class Point:
    """Кратко о том, как устроен __new__"""

    def __new__(cls, *args, **kwargs):
        print('__new__ is calling to ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('__init__ is calling to ' + str(self))
        self.x = x
        self.y = y


class MetaSingleton(type):
    """Пример реализации Singleton через метакласс.
       Паттерн Singleton предоставляет механизм для создания только одного экземпляра класса.
       При попытке создания нового объекта этого класса, будет возвращаться уже созданный ранее экземпляр.
       При каждой попытке создания нового (происходит вызов класса) экземпляра класса, будет вызываться __call__
       метакласса и возвращать уже ранее созданный объект...
       Можно сказать, что создав пользовательский метакласс, можно переопределять стандартное поведение всех встроенных
       магических методов...
       """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    def __init__(self, user, psw, port):
        print(self, '__init__ is calling...')
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Connection to DB: {self.user}, {self.psw}, {self.port}')


if __name__ == '__main__':
    db = DataBase('root', '1234', 80)
    print(db.__dict__)
    db2 = DataBase('user', 'user', 45)  # при попытке создать новый экземпляр, свойства не обновляются...
    print(id(db), id(db2), sep='\n')  # ...и новый объект не создается
    print(db2.__dict__)
    db.connect()
    db2.connect()
