from fastapi import FastAPI
from model.base_model import *
import service.otp_utils as otp_utils
import auth.register as register
from fastapi.responses import JSONResponse
from service.generate_jwt import generate_jwt
import json

app = FastAPI()


@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.post("/send-email")
async def email_verifier(email:Email):
    content = otp_utils.send_otp(email.email)
    
    if content['status']=='success':
        content.update({"jwt_bearer": generate_jwt({"email":email.email})})
    response = JSONResponse(content=content)
    return response


@app.post("/verify-otp")
async def otp_verifier(otp:OTP):
    return otp_utils.verify_otp(otp)
    
@app.post("/register")
async def user_register(user:User):
    uid,content,jwt_token = register.register_user(user)
    response = JSONResponse(content=content)
    response.set_cookie(key = "jwt_bearer", value = jwt_token )
    print(response)

@app.post("/publish_key")
async def publish_key(keyBundle:KeyBundle):
    return "ya"
