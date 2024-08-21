import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from service.generate_jwt import generate_jwt
import json
SECRET = "this_is_a_secret_token_indeed"

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        if request.url.path not in ["/ping","/send-email","/favicon.ico","/docs","/openapi.json"]:
            auth_token = request.headers.get("Authorization")
            try:
                data=jwt.decode(
                    auth_token,
                    SECRET,
                    algorithms=["HS256"]
                )
                request.state.user_data = data
            except jwt.ExpiredSignatureError:
                return JSONResponse(status_code=401,content={"code":"401","status":"failed","message":"Token has expired"})
            except Exception as err:
                return JSONResponse(status_code=500,content={"code":"500","status":"failed","message":"Invalid token"})
            response = await call_next(request)

            #getting response of api route
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            response_body = response_body.decode()
            response_body = json.loads(response_body)

            #checking if JWT changed and put JWT
            if response_body != None and "Authorization" in response_body:
                response=JSONResponse(content=response_body,headers={"Authorization":response_body["Authorization"]})
            else:
                response=JSONResponse(content=response_body,headers={"Authorization":auth_token})
            return response
            
        elif request.url.path in ["/send-email"] and request.method == "POST":
            # getting email before consumed
            await request.body()
            email = await request.json()
            email = email['email']

            #getting response of route
            response = await call_next(request)
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            response_body = response_body.decode()
            response_body = json.loads(response_body)

            #checking if route succeed
            if response_body['status']=='success':
                response_body.update({"Authorization": generate_jwt({"email":email})})
            return JSONResponse(response_body)
        else:
            return await call_next(request)
