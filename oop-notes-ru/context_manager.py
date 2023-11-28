class SecuredVector:
    def __init__(self, v: list):
        if isinstance(v, list):
            self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # создаем копию для дальнейшей обработки...
        return self.__temp  # возвращаем ссылку на эту копию в объявленное глобальном пространстве имя...

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Если возникают исключения, они передаются в качестве параметров."""
        print(exc_val, exc_type, exc_tb)  # Check!
        if exc_type is None:
            # если в ходе работы менеджера не возникло ошибок, заменяем элементы оригинала содержимым временной копии
            self.__v[:] = self.__temp
        return False  # Если ложь, значит исключения не обрабатываются и наоборот...


if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [1, 2]
    v3 = [2, 4, 6]
    try:
        with SecuredVector(v1) as dv:
            for i, val in enumerate(dv):
                dv[i] += v2[i]
            print("Ошибки нет. Список обновил значения...")
    except IndexError:
        print("Возникла ошибка. Список не изменился...")

    print(v1)  # Если возникнет исключение, данные в списке сохранятся без изменений...

    with SecuredVector(v1) as dv:
        for i, val in enumerate(dv):
            dv[i] += v3[i]
        print("Ошибки нет. Список обновил значения...")

    print(v1)  # Если менеджер контекста завершит работу без ошибок, оригинальные данные изменятся...

