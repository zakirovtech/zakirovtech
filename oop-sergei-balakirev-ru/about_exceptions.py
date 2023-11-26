class PrintError(Exception):
    """Класс исключения при отправке данных принтеру для печати."""
    def __init__(self, *args):
        self.message = args[0] if args else None  # Пользовательская логика формирования сообщения.

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise PrintError('Принтер не отвечает')

    def send_to_print(self, data):
        return False


if __name__ == '__main__':
    p = PrintData()
    p.print('data')

