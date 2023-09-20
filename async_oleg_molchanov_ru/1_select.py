"""Асинхронность при помощи событийного цикла и простых функций..."""
import socket
from select import select
# select системная функция для мониторинга состояний переданных системных-файловых объектов | есть в любой системе
# файловый объект, это объект с методом fileno(), который возвращает файловый дескриптор --- номер файла (целое число)

# Коллекция с файлами, состояния которых нужно мониторить. Будет передан в select()...
to_monitor = []

# Серверный сокет
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

to_monitor.append(server_socket)


def accept_connection(ss: socket):
    # accept() блокирующая операция...
    client_socket, addr = ss.accept()
    print(f'Connection from {addr}...')

    to_monitor.append(client_socket)  # каждый новый клиент добавляется в список для мониторинга доступности для чтения


def send_message(cs: socket):
    # recv() блокирующая операция...
    request = cs.recv(4096)  # размер буфера для сообщения

    if request:
        print(f'Received a message: {request.decode()}')
        response = 'Hello world!\n'.encode()  # ответ для пользователя в байтах
        cs.send(response)
    else:
        print(f'Client is disabled... ')
        to_monitor.remove(cs)  # удаление сокета из списка мониторинга в случае отсоединения...
        cs.close()


def event_loop():
    while True:
        # блокирующая операция select() ждет, когда в переданные файлы изменят состояние и будут готовы к действию...
        to_read, _, _ = select(to_monitor, [], [])

        for sock in to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    event_loop()
