import sqlite3

class DbController:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect('movies.sqlite', check_same_thread=False)
        self.cursor = self.conn.cursor()
        # dictcursor

    def connect_to_row(self):
        self.conn = sqlite3.connect('movies.sqlite', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)

    def fetch_all(self):
        return self.cursor.fetchall()
    
    def fetch_one(self):
        return self.cursor.fetchone()
    
    def commit(self):
        return self.conn.commit()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()