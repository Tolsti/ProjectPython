import socketserver


class EchoUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print('New connection')
        print('ID: {}'.format(data.decode()))


if __name__ == '__main__':
    with socketserver.UDPServer(('127.0.0.1', 8880), EchoUDPHandler) as server:
        server.serve_forever()
