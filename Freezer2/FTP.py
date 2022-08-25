import maskpass
import ftplib
import os
import shutil

class MyFTP():
    def __init__(self):
        self.flag = 0
        self.dirFTP = "/home/imane/Musique/"
        self.Songs = []
        self.Song_name = ""

    def FTP_conn(self):
        # Open ftp connection
        self.USER   = 'guest'#input("Enter your username : ")
        PASSWD = 'guest'#maskpass.askpass("Enter your password : ")
        HOST   = "10.125.24.84"
        self.ftps = ftplib.FTP_TLS(HOST,self.USER,PASSWD)

    def FTP_UPdatelist(self):
        self.FTP_conn()
        # List The Distant Music Directory
        try:
            self.Songs = self.ftps.nlst()
        except ftplib.error_perm as resp:
            if str(resp) == "550 No files found":
                print("No Songs in this directory")
            else:
                raise

    def FTP_list(self):
        self.FTP_conn()
        try:
            for s in self.Songs:
                print(s)
        except:
            pass
            
    def FTP_GetLocally(self,SONG):
        self.FTP_conn()
        for f in self.Songs:
            if SONG in f:
                print('Song exists')
                localfile = open(f, 'wb')        
                self.ftps.retrbinary('RETR ' + f, localfile.write, 1024)
                self.Song_name = str(localfile).split("'")[1]
                self.Song_path = os.path.abspath(str(self.Song_name))
                try:
                    shutil.move(self.Song_path,self.dirFTP)
                except:
                    pass
                self.flag = 1
    
    def FTP_Get(self):
        self.FTP_conn()
        for f in self.Songs:
            localfile = open(f, 'wb')        
            self.ftps.retrbinary('RETR ' + f, localfile.write, 1024)
            self.Song_name = str(localfile).split("'")[1]
            self.Song_path = os.path.abspath(str(self.Song_name))
            if self.Song_name in f:
                try:
                    shutil.move(self.Song_path,self.dirFTP)
                except:
                    pass
                self.flag = 1