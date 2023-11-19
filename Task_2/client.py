from socket import *


class Client:
    def __init__(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((ip, port))

    def connect(self):
        try:
            msg = self.client.recv(1024).decode('utf-8')
        except Exception as e:
            print(f'ERROR: {str(e)}')
            exit()
        if msg == 'You are connected':
            print(msg)
            self.listen()
        else:
            exit()

    def sender(self, text):
        self.client.send(text.encode('utf-8'))
        while self.client.recv(1024).decode('utf-8') != 'data getted':
            self.client.send(text.encode('utf-8'))

    def listen(self):
        is_work = True
        while is_work:
            data = input('Send message to server: ')
            if data:
                if data == 'disconnect':
                    self.sender(data)
                    print(self.client.recv(1024).decode('utf-8'))
                    is_work = False
                else:
                    self.sender(data)
                    print(self.client.recv(1024).decode('utf-8'))


Client('192.168.0.109', 5000).connect()
