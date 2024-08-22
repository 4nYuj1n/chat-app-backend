
from db.delete_user_register import delete_user_register
from db.select_user_register import select_user_register
from db.insert_user import insert_user
from service.generate_jwt import generate_jwt
from auth.utils import generate_uid
from datetime import datetime
import jwt
def register_user(request,user):
    email = request.state.user_data['email']
    _,email,_ = select_user_register(email)
    if email==None:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "Failed registering user"
        }
        
    uid=generate_uid()
    if insert_user(uid,user.username,user.password,email,None,datetime.now()) == "OK":
        delete_user_register(email)
        jwt = generate_jwt({"uid":uid})
        print(jwt)
        return {
            "code" : "200",
            "status" : "success",
            "message" : "Sucessfully registered user",
            "authorization" : jwt
        }
    else:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "Failed registering user"
        }

    

