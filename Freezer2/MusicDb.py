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
        self.db_connect()
        self.cur = self.conn.cursor()

    def db_insert(self,Artist,Song,User):
        self.cur.execute("INSERT INTO Music (Artist,Song,User) VALUES (?,?,?)",(Artist,Song,User))

    def db_search(self,Artist,Song,User):
        self.cur.execute("SELECT * FROM Music WHERE Artist LIKE ? HAVING User = ? ",(Artist,Song,User))

    def db_GetAll(self,User):
        self.cur.execute("SELECT * FROM Music WHERE User = ? ",(User))

    

    #conn.commit()
    #cur.execute("SELECT * FROM machines;")