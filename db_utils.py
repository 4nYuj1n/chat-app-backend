import mysql.connector
import bcrypt

class db_connect:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chat_app"
        )
        self.cursor=self.conn.cursor()
    
    def get_max_id(self,table_name):
        try:
            q=f"SELECT MAX(id) FROM {table_name} LIMIT 1"
            self.cursor.execute(q)
            return int(self.cursor.fetchall()[0][0])+1
        except Exception as err:
            print(err)
    
    def insert_data(self,query,params=None):
        try:
            if params:
                self.cursor.execute(query,params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return None
        except Exception as e:
            print(f"getting error {e}")
            return e

    def delete_otp_token(self,id):
        try:
            q="DELETE FROM otp_verify_tbl WHERE id=%s"
            p=(id,)
            self.cursor.execute(q,p)
            self.conn.commit()
            return 'OK'
        except Exception as err:
            print(err)
            return err

    def select_data(self,query,params):
        self.cursor.execute(query,params)
        return self.cursor.fetchall()

    def delete_register_token(self,auth_token):
        try:
            q="DELETE FROM user_register_tbl WHERE verif_token=%s"
            p=(auth_token,)
            self.cursor.execute(q,p)
            self.conn.commit()
            return 'OK'
        except Exception as err:
            return err

    def select_register_token(self,auth_token):
        try:
            q="SELECT * FROM user_register_tbl WHERE verif_token=%s"
            p=(auth_token,)
            self.cursor.execute(q,p)
            return self.cursor.fetchall()[0]
        except Exception as err:
            return err

    def select_username(self,username):
        try:
            q="SELECT * FROM user WHERE username=%s"
            p=(username,)
            self.cursor.execute(q,p)
            return self.cursor.fetchall()[0]
        except Exception as err:
            return None,None,None,None

    def register_user(self,username,password,email,curr_time):
        try:
            id=self.get_max_id("user")
            print(id)
            if id==None:
                id=1
            print(id)
            q="INSERT INTO user VALUES(%s,%s,%s,%s,%s)"
            p=(id,email,bcrypt.hashpw(password.encode(), bcrypt.gensalt(16)),username,curr_time)
            self.cursor.execute(q,p)
            self.conn.commit()
            return 'OK'
        except Exception as err:
            print(err)
            return err

    def insert_register_token(self,email,auth_token,curr_time):
        try:
            id=self.get_max_id('user_register_tbl')
            q="INSERT INTO user_register_tbl VALUES(%s,%s,%s,%s)"
            p=(id,auth_token,email,curr_time)
            self.cursor.execute(q,p)
            self.conn.commit()
            return 'OK'
        except Exception as err:
            print(err)
            return err

    def close_db(self):
        self.cursor.close()
        self.conn.close()

