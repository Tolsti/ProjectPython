import socket

host = '127.0.0.1'
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
client = []
print('Start Server')

while True:
    data, address = sock.recvfrom(1024)
    print(address[0], address[1])
    if address not in client:
        client.append(address)
    for clients in client:
        if clients == address:
            continue
        sock.sendto(data, clients)
