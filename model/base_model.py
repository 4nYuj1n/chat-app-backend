from pydantic import BaseModel


class Email(BaseModel):
    email : str

class Username(BaseModel):
    username : str
    
class OTP(BaseModel):
    otp : str

class UserData(BaseModel):
    username : str
    password : str
    profile_image : str

class LoginCreds(BaseModel):
    email : str
    password : str

class IdentityKey(BaseModel):
    identity_key:str
    identity_key_x:str

class SignedKey(BaseModel):
    type:int
    key:str
    identifier:str
    signature:str
