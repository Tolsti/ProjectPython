# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.sendto(b'Test message', ('127.0.0.1', 8888))

import random
import socket
import string

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.connect(('127.0.0.1', 8880))
    unique_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    client.send(('id: '+str(unique_id)).encode())
