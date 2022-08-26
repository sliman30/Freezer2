import mariadb

class Music_db():
    def __init__(self) -> None:
        pass

    def db_connect(self):
        try:
            self.conn = mariadb.connect(
                user="Freezer",
                password="freezer",
                host="127.0.0.1",
                database="FreezerDb"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def db_insert(self,Artist,Song,User):
        self.db_connect()
        cur = self.conn.cursor()
        statement = "INSERT INTO Music (Artist,Song,User) VALUES (%s,%s,%s);"
        data = (str(Artist),str(Song),str(User))
        cur.execute(statement, data)
        print('Insertion Complete !')
    
    def db_search(self,Artist,Song,User):
        self.db_connect()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Music WHERE Artist LIKE ? HAVING User = ? ",(Artist,Song,User))

    def db_GetAll(self,User):
        self.db_connect()
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM Music ",(User))

    

    #conn.commit()
    #cur.execute("SELECT * FROM machines;")