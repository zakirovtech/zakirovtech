"""Асинхронность при помощи модуля selectors, путем вызова коллбеков..."""
import socket
import selectors


def server():
    """Серверный сокет"""
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    # Регистрация файлового объекта для последующего мониторинга...
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(ss: socket):
    # accept() блокирующая операция...
    client_socket, addr = ss.accept()
    print(f'Connection from {addr}...')
    # Регистрация файлового объекта для последующего мониторинга...
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(cs: socket):
    # recv() блокирующая операция...
    request = cs.recv(4096)  # размер буфера для сообщения

    if request:
        print(f'Received a message: {request.decode()}')
        response = 'Hello world!\n'.encode()  # ответ для пользователя в байтах
        cs.send(response)
    else:
        selector.unregister(cs)  # перед закрытием нужно снять с регистрации...
        print(f'Client is disabled... ')
        cs.close()


def event_loop():
    while True:
        # select() блокирующая операция / ждет изменения состояния
        events = selector.select()  # --> [(key, events), ...], где key это NamedTuple с данными файловых объектов...
        # ... key(fileobj: socket, events: read or write, data: function)
        for key, _ in events:
            callback = key.data  # по ключу data лежит нужная функция...
            callback(key.fileobj)  # по ключу fileobj лежит нужный сокет...


if __name__ == '__main__':
    selector = selectors.DefaultSelector()  # выбирает стандартный модуль системы для мониторинга файловых объектов...
    server()
    event_loop()
