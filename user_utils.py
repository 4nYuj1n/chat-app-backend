import db_utils
from datetime import datetime
import bcrypt

def register_user(user):
    conn=db_utils.db_connect()
    id,email,password,username,curr_time=conn.select_register_token(user.authorization)
    if auth_token==user.authorization:
        conn.register_user(user.username,user.password,email,datetime.now())

def user_login(user):
    conn=db_utils.db_connect()
    print(user)
    id,email,password,curr_time=conn.select_username(user.username)
    if email==None and id==None:
        return{
            "code" : "200",
            "status" : "failed",
            "message" : "Login failed"
        }
    if bcrypt.checkpw(user.password.encode(),password):
        
        return{
            "code" : "200",
            "status" : "success",
            "message" : "Login successfully",
        }
