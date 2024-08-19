import db.database as database
from auth.utils import generate_uid
from datetime import datetime
import jwt
def register_user(user):
    conn=database.db_connect()
    _,auth_token,email,_=conn.select_register_token(user.authorization)
    if auth_token==user.authorization:
        conn.delete_register_token(auth_token)
        uid=generate_uid(conn)
        conn.register_user(uid,user.username,user.password,email,None,datetime.now())
        jwt_token = jwt.encode({"uid":uid,"exp":datetime.now()},"this_is_a_secret_token_indeed")
        return ({
            "code" : "200",
            "status" : "success",
            "message" : "Sucessfully registered user"
        },jwt_token)
    else:
        return ({
            "code" : "200",
            "status" : "failed",
            "message" : "Invalid authorization token"
        },None)

    

