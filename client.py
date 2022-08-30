import socket

class Client():
    HOST = '10.125.24.63'    # The remote host
    PORT =  12000     # The same port as used by the server
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
        print('Download starting', data.decode())

    def close(self):
        self.s.close()