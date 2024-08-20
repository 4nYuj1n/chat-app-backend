from pydantic import BaseModel


class Email(BaseModel):
    email : str
    
class OTP(BaseModel):
    otp : str

class User(BaseModel):
    username : str
    password : str
    profile_image : str

class IdentityKey(BaseModel):
    identity_key:str

class SignedKey(BaseModel):
    type:int
    key:str
    identifier:str
    signature:str
