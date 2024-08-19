
from db import delete_user_register,select_user_register,insert_user
from auth.utils import generate_uid
from datetime import datetime
import jwt
def register_user(user):
    _,auth_token,email,_ = select_user_register(user.authorization)
    if auth_token==user.authorization:
        delete_user_register(auth_token)
        uid=generate_uid()
        insert_user(uid,user.username,user.password,email,None,datetime.now())

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

    

