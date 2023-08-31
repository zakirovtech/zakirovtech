"""Пример асинхронности с использованием генераторов...
Если при использовании обычных функций, интерпретатор сталкивался с блокирующей операцией, которая ждет подключения
или ответа, в случае с генератором, эти операции вызываются к сокетам уже готовым что-то принять или отдать...
Yield возвращает сокет и метку, сокет передается в select(), когда сокет готов вызывается генератор и доделывает
оставшиеся инструкции...
Единственной блокирующей функцией будет select(), которая ждет изменения состояния файловых объектов в какой-либо
из переданных в нее коллекций..."""
import socket
from collections import deque
from select import select


def server():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield 'read', server_socket  # до блокирующей операции возвращает кортеж с меткой о действии и сокетом
        cs, addr = server_socket.accept()  # состояние read
        print(f'Connection from {addr}...')
        tasks.append(client(cs))  # создается объект генератора и добавляется в очередь задач...


def client(client_socket: socket) -> tuple:
    while True:
        yield 'read', client_socket  # возвращает кортеж с меткой о действии и сокетом
        # операция больше не блокирует выполнение, так как вызывается в момент, когда сокет готов к чтению
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()

            yield 'write', client_socket  # возвращает кортеж с меткой о действии и сокетом
            # операция больше не блокирует выполнение, так как вызывается в момент, когда сокет готов к записи
            client_socket.send(response)  # write

    print(f'Client is disabled... ')
    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        """если хотя бы один из элементов переданных в any() True, any --> True..."""
        while not tasks:
            # блокирующая операция select() ждет изменения состояния какого-либо сокета...
            ready_to_read, ready_to_write, mistakes = select(to_read, to_write, [])
            for sock in ready_to_read:
                # из словаря извлекается нужный генератор по ключу, добавляется в список и удаляется пара ключ-значение
                tasks.append(to_read.pop(sock))
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
        try:
            gen = tasks.popleft()  # первый в очереди генератор извлекается
            sock_cond, sock = next(gen)  # генератор запускается и забираются данные
            # в зависимости от метки, добавляются в нужную коллекцию...
            if sock_cond == 'read':
                to_read[sock] = gen
            elif sock_cond == 'write':
                to_write[sock] = gen
        except StopIteration:
            print('По какой-то причине ресурс генератора исчерпан!')


if __name__ == '__main__':
    tasks = deque()  # коллекция задач для мониторинга / в данном случае это объекты генераторов
    # так как у сокетов два состояния, создается два словаря, в качестве ключей будет сокет, а генератор в значении...
    to_read = {}
    to_write = {}

    tasks.append(server())  # создается объект генератора и добавляется в очередь задач...
    event_loop()
