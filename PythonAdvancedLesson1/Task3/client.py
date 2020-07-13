import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(('127.0.0.1', 8888))

    client.send(input('Enter two comma separated numbers: ').encode())
    data = client.recv(1024).decode()

print('Server returned the sum of these numbers:', data)
