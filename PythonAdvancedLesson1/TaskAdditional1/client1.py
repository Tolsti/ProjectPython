import socket
import threading


def read_sok():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


host = '127.0.0.1'
port = 8888
alias = input()
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
potok = threading.Thread(target=read_sok)
potok.start()
while True:
    mensahe = input()
    sor.sendto(('[' + alias + '] ' + mensahe).encode('utf-8'), (host, port))
