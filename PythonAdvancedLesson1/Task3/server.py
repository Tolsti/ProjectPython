import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('127.0.0.1', 8888))
    server.listen(5)

    while True:
        client, addr = server.accept()
        result = list(map(int, client.recv(1024).decode('utf-8').replace(' ', '').split(',')))

        client.sendall(str(sum(result)).encode())
        print('Numbers from the client:', *result)
