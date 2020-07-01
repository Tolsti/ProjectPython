import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - IP протокол версии 4, SOCK_STREAM протокол TCP
sock.bind(('127.0.0.1', 8888))  # резервируем порт
sock.listen(5)  # размер очереди, сколько соединений мы хотим слушать

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
