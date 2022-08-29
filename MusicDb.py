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
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def db_insert(self,Artist,Song,User):
        self.db_connect()
        statement = "INSERT INTO Music (Artist,Song,User) VALUES (%s,%s,%s);"
        data = (str(Artist),str(Song),str(User))
        self.cur.execute(statement, data)
        self.conn.commit()
        print('Insertion Complete !')
    
    def db_search(self,Artist,Song,User):
        self.db_connect()
        self.cur.execute("SELECT * FROM Music WHERE Artist LIKE ? HAVING User = ? ",(Artist,Song,User))

    def db_GetAll(self):
        self.db_connect()
        self.cur.execute("SELECT * FROM Music ")

    

    #conn.commit()
    #cur.execute("SELECT * FROM machines;")