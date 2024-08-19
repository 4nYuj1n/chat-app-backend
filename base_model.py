from pydantic import BaseModel


class Email(BaseModel):
    email : str
    
class OTP(BaseModel):
    otp : str
    authorization : str

class User(BaseModel):
    username : str
    password : str
    authorization : str

class LoginCreds(BaseModel):
    username:str
    password:str
