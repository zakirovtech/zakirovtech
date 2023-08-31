"""Синхронное подключение и ответы сокетов """
import socket
# socket --> ip:port
# AF_INET --> ipV4
# SOCK_STREAM --> TCP
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# настройки, чтобы можно было переиспользовать сокет...
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# привязка сокета к домену и порту...
server_socket.bind(('localhost', 5000))
# сокет слушает буфер на входящие подключения...
server_socket.listen()

# бесконечный цикл, так как сервер постоянно должен ждать входящие данные
while True:
    print('Waiting a connection...')  # бесконечное ожидание подключения, и если оно есть программа продолжает работу...
    # accept() блокирующая операция...
    client_socket, addr = server_socket.accept()  # ждет подключения / затем --> (клиентский сокет, адрес клиента)
    print(f'Connection from {addr}...')
    # есть подключение, теперь ждем сообщения...
    while True:
        print('Waiting a request...')  # ждем от клиентского сокета запроса
        # recv() блокирующая операция...
        request = client_socket.recv(4096)  # размер буфера для сообщения

        # условие прерывания цикла
        if not request:
            break
        else:  # на запрос от клиента формируется и отправляется ответ
            print(request.decode())
            response = 'Hello world!\n'.encode()  # ответ для пользователя в байтах
            client_socket.send(response)

    print(f'Client {addr} is disabled... ')
    client_socket.close()
