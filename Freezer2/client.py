import socket

class Client():
    HOST = '127.0.0.1'    # The remote host
    PORT =  12010        # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self) -> None:
        pass

    def connect(self, Song):
        self.s.connect((self.HOST, self.PORT))
        Message = Song
        if Message == "":
                Message = "list"
        self.s.sendall(Message.encode())
        data = self.s.recv(1024)
        print('Received', data.decode())

    def close(self):
        self.s.close()