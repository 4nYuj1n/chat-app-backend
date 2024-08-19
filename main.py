from fastapi import FastAPI
from verify_email import verify_email
from model.base_model import *
import service.otp as otp
import auth.register as register
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.post("/send-email")
async def email_verifier(email:Email):
    return otp.send_otp(email.email)


@app.post("/verify-otp")
async def otp_verifier(otp:OTP):
    return otp.verify_otp(otp)
    
@app.post("/register")
async def user_register(user:User):
    uid,content,jwt_token = register.register_user(user)
    response = JSONResponse(content=content)
    response.set_cookie(key = "jwt_bearer", value = jwt_token )
    print(response)

@app.port("/publish_key")
async def publish_key(keyBundle:KeyBundle):
    return "ya"
