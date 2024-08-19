from fastapi import FastAPI,Request
from model.base_model import *
import service.otp_utils as otp_utils
import auth.register as register
from fastapi.responses import JSONResponse
from service.generate_jwt import generate_jwt
from middleware.jwt_handler import JWTAuthMiddleware
import json

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
async def user_register(user:User):
    content = register.register_user(user)
    response = JSONResponse(content=content)
    return response

@app.post("/publish_key")
async def publish_key(keyBundle:KeyBundle):
    return "ya"
