import json
from socket import *


class Server:
    def __init__(self, ip, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(3)

    def sender(self, user, text):
        user.send(text.encode('utf-8'))

    def start_server(self):
        while True:
            user, address = self.server.accept()
            print(f'CONNECTED: \nIP: {address[0]} \nPORT:{address[1]}')
            self.listen(user)

    def validateJSON(self, msg):
        try:
            json.loads(msg)
        except ValueError as e:
            return False
        return True

    def listen(self, user):
        self.sender(user, 'You are connected')
        is_work = True
        while is_work:
            try:
                data = user.recv(1024)
                self.sender(user, 'data getted')
            except Exception as e:
                data = ''
                is_work = False
            if len(data) > 0:
                msg = data.decode('utf-8')
                if msg == 'disconnect':
                    self.sender(user, 'You are disconnceted')
                    user.close()
                    is_work = False
                else:
                    is_valid = str(self.validateJSON(msg))
                    self.sender(user, is_valid)

            else:
                print('Client disconnected')
                is_work = False


Server('192.168.0.109', 5000).start_server()
