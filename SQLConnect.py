import sqlite3


class SQLConnect:
    connection: sqlite3.connect
    cur: sqlite3.Cursor

    def __init__(self, name: str):
        self.connection = sqlite3.connect(f"{name}.db")
        self.cur = self.connection.cursor()

    def sql_query(self, query: str):
        self.cur.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def select_query(self, query: str) -> list:
        self.cur.execute(query)
        return self.cur.fetchall()
