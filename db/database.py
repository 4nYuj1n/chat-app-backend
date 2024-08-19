import mysql.connector
import bcrypt
import datetime

class db_connect:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quantum_chat"
        )
        self.cursor=self.conn.cursor()
        return self.conn,self.cursor

    
    def check_uid(self,uid):
        try:
            q=f"SELECT * FROM user WHERE uid=%s"
            p=(uid,)
            self.cursor.execute(q,p)
            temp=self.cursor.fetchall()
            return temp
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

<<<<<<< HEAD:db/database.py
    def register_user(self,uid,username,password,email,profile_url,curr_time):
=======
    def select_username(self,username):
        try:
            q="SELECT * FROM user WHERE username=%s"
            p=(username,)
            self.cursor.execute(q,p)
            return self.cursor.fetchall()[0]
        except Exception as err:
            return None,None,None,None

    def register_user(self,username,password,email,curr_time):
>>>>>>> e45bd02374a06e74b8b76a9383baf5b627506c6b:db_utils.py
        try:
            q="INSERT INTO user VALUES(%s,%s,%s,%s,%s)"
            p=(uid,username,email,bcrypt.hashpw(password.encode(), bcrypt.gensalt(16)),profile_url,curr_time)
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
        
    def save_otp_to_db(self,email,token,OTP):
        current_time = datetime.now()
        max_id=self.get_max_id("otp_verify_tbl")
        q="INSERT INTO otp_verify_tbl VALUES(%s,%s,%s,%s,%s)"
        p=(email,token,OTP,current_time,max_id)
        simpan=self.insert_data(q,p)
        return simpan
    
    def get_otp_from_db(self,auth_token):
        q="SELECT * FROM otp_verify_tbl WHERE verif_token = %s"
        p=(auth_token,)
        data=self.select_data(q,p)
        data=list(data[0])
        return data[0],data[2],data[3],data[4]
    
    def close_db(self):
        self.cursor.close()
        self.conn.close()

