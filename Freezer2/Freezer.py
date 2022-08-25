from multiprocessing.dummy.connection import Client
from turtle import clear
from zipapp import get_interpreter
import playsound
import client
import MusicDb
import FTP


Ftp = FTP.MyFTP()
Ftp.FTP_UPdatelist()
Ftp.FTP_list()

SONG = input("What song w'd you like to listen to ? ")
Ftp.FTP_GetLocally(SONG)

###################################################

if Ftp.flag == 1:
    Ans = input('Do you want to play it ? ')
    if Ans == 'yes':
        Song_path2 = Ftp.dirFTP+Ftp.Song_name
        playsound.playsound(Song_path2)
else:
    print('Song does not exist in your Library. Download started')    
    ClientLocal = client.Client()
    ClientLocal.connect("Get "+ Ftp.USER +" "+ SONG)
    ClientLocal.close()
    Ftp.FTP_UPdatelist()
    Ftp.FTP_Get()