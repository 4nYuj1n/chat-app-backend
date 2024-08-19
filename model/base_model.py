from pydantic import BaseModel


class Email(BaseModel):
    email : str
    
class OTP(BaseModel):
    otp : str
    authorization : str

class User(BaseModel):
    username : str
    password : str
    profile_image : str
    authorization : str

class KeyBundle(BaseModel):
    identityKey                         : str
    curvePreKey                         : str
    curvePreKeyIdentifier               : str
    curvePreKeySignature                : str
    lastResortPQKemPreKey               : str
    lastResortPQKemPreKeyIdentifier     : str
    oneTimePQKemPreKeySet               : str
    oneTimePQKemPreKeyIdentifierSet     : str