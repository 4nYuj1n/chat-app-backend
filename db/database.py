import mysql.connector # type: ignore


class db_connect:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="db",
            user="root",
            password="quantum123",
            database="quantum_chat"
        )
        self.cursor=self.conn.cursor()
        
    def get_conn_and_cursor(self):
        return self.conn,self.cursor
    def close_db(self):
        self.cursor.close()
        self.conn.close()

