from fastapi import FastAPI
from verify_email import verify_email
from base_model import *
import otp_utils
import user_utils

app = FastAPI()

@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.post("/send-email")
async def email_verifier(email:Email):
    return otp_utils.send_otp(email.email)


@app.post("/verify-otp")
async def otp_verifier(otp:OTP):
    return otp_utils.verify_otp(otp)
    
@app.post("/register")
async def user_register(user:User):
    return user_utils.register_user(user)