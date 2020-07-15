import socket
import threading


def read_sok():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


host = '127.0.0.1'
port = 8888

sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))

alias = input()
pot = threading.Thread(target=read_sok)
pot.start()

while True:
    message = input()
    sor.sendto(('[' + alias + '] ' + message).encode('utf-8'), (host, port))
