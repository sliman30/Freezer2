import socket
import re
import os
import MusicDb

Mydb = MusicDb.Music_db()

class Server():
    def __init__ (self, host , port):
        # https://docs.python.org/3/library/socket.html
        self.HOST=host
        self.PORT=port
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)

    def wait(self):
        con, addr = self.s.accept()
        print('Connected by', addr)
        self.conn(con,addr) 

    # fonction qui gere 1 client connecté
    def conn(self,con,addr):
        client = True
        data = con.recv(1024).decode()
        print(addr,": ", data)
        print()
        ret=""
        get="ok"
        result =re.search("^([A-z0-9\-@]+) ?([0-9\.A-z\-]+)? ?([0-9\.A-z\ \-]+)?$",data)
        if result.group(1) == "Get":
            USER = result.group(2)
            SONG = result.group(3)
            os.system("spotdl " + SONG + " -p '/home/"+USER+"/Music/{title}_{artist}.{ext}'")
            Songs = os.listdir("/home/"+USER+"/Music/")
            for f in Songs:
                if SONG in f:
                    print(f)
                    Song  = f.split("_")[0]
                    Artist = f.split("_")[1]
                    print(Song)
                    print(Artist)
            #Mydb.db_insert(self,Artist,Song,User)
        msg=""
        for i in get:
            msg+=str(i)+ret

        # on envoie une reponse au client
        con.sendall(msg.encode())
        con.close()
        self.s.close()
        
serv = Server("127.0.0.1",12010)
serv.wait()
serv.s.close()