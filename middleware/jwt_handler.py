import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime,timedelta
SECRET = "this_is_a_secret_token_indeed"

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def VerifyToken(self,request:Request,call_next):
        if request.url.path not in ["/ping","/send-email","/verify-otp","/register"]:
            auth_token = request.cookies.get("jwt_bearer")
            print(f"Custom middleware applied to {request.url.path}")
            try:
                data=jwt.decode(
                    auth_token,
                    SECRET,
                    algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                return JSONResponse(status_code=401,content={"code":"401","status":"failed","message":"Token has expired"})
        print(data)
