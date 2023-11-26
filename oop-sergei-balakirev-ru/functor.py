class Some:
    SOME_CONST = None

    def __call__(self, *args, **kwargs):
        print('__call__ is calling')
        return object.__call__(*args, **kwargs)


class Functor:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step, *args, **kwargs):
        """Функция, которая что-то делает, вызывается в __call__.
        Это простейший пример. Могут быть несколько функций и они будут вызываться при разных условиях."""
        self.__count(step)
        return self.__counter  # Возвращается необходимый результат. Здесь это атрибут класса.

    def __count(self, step):
        """Есть функция, которая что-то делает.
        В этом примере меняет свойство класса."""
        self.__counter += step


class Counter:
    """Есть некоторый класс, где нужно применить функтор"""
    def __init__(self):
        self.count = Functor()  # У каждого объекта будет доступ к функтору по заданному имени

    def do_count(self, step: int = 1):  # использование функтора можно скрыть в методе [опционально]
        return self.count(step=step)


if __name__ == '__main__':
    s = Some()
    s()  # экземпляр функтора теперь можно вызвать как функцию

    obj = Counter()
    print(obj.do_count(2))  # Теперь объект этого класса может вызывать функтор
    print(obj.__dict__)
