import psycopg2

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="mydb",
            user="user",
            password="pass",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()