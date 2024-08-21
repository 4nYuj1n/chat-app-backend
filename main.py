from fastapi import FastAPI,Request
from model.base_model import *

import service.otp_utils as otp_utils
import auth.register as register
from middleware.jwt_handler import JWTAuthMiddleware
from service.key_publish.check_key import check_key
from service.key_publish.verify_identity_key import verify_identity_key
from service.key_publish.verify_key import verify_key

from typing import Union


app = FastAPI()

app.add_middleware(JWTAuthMiddleware)

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/send-email")
async def email_verifier(email:Email):
    content = otp_utils.send_otp(email.email)

    return content


@app.post("/verify-otp")
async def otp_verifier(request:Request,otp:OTP):
    return otp_utils.verify_otp(request,otp)
    
@app.post("/register")
async def user_register(request:Request,user:User):
    response = register.register_user(request,user)
    return response

@app.post("/publish-key")
async def publish_key(request:Request,key_bundle:Union[IdentityKey,SignedKey]):
    if isinstance(key_bundle,IdentityKey):
        print(key_bundle)
        response = verify_identity_key(request,key_bundle)
        return response
    elif isinstance(key_bundle,SignedKey):
        response = verify_key(request,key_bundle)
        return response

@app.get("/check-key")
async def check_key(request:Request,_type:int):
    response = check_key(request,_type)
    return response