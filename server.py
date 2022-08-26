import socket
import re
import sys
import os
import MusicDb
import subprocess
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
        data = con.recv(1024).decode()
        print(addr,": ", data)
        print()
        ret=""
        get="Download complete ! Sending via FTP."
        result =re.search("^([A-z0-9\-@]+) ?([0-9\.A-z\-]+)? ?(.+)?$",data)
        if result.group(1) == "Get":
            USER = result.group(2);SONG = result.group(3)
            os.chdir("/home/"+USER+"/Music")
            var=subprocess.check_output("spotdl '" + SONG + "'",shell=True).decode()
            resulta=re.search('Found YouTube URL for "(.+)"',var)

            Artist = resulta.groups()[0].split("-")[0]
            Song = resulta.groups()[0].split("-")[1]
            print(str(Artist));print(str(Song));print(type(USER))
            Mydb.db_insert(str(Artist),str(Song),str(USER))
            Mydb.db_GetAll(USER)

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