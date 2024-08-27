from fastapi import FastAPI,Request,WebSocket, WebSocketDisconnect
from model.base_model import *
from fastapi.responses import JSONResponse

import service.otp_utils as otp_utils
import auth.register as register
from middleware.jwt_handler import JWTAuthMiddleware
from service.key_publish.check_key import check_key
from service.key_publish.verify_identity_key import verify_identity_key
from service.key_publish.get_key_bundle import get_key_bundle
from service.key_publish.verify_key import verify_key
from service.friends.get_friends import get_friends
from service.user.profile import get_profile
from auth.login import login_user
from service.friends.add_friend_relation import add_friend_relation
from service.friends.get_friend_list import get_friend_list
from typing import Union
from service.websocket import ConnectionManager

app = FastAPI()
manager = ConnectionManager()

app.add_middleware(JWTAuthMiddleware)

@app.get("/ping")
async def _ping():
    return {"message": "pong"}

@app.post("/send-email")
async def _email_verifier(email:Email):
    content = otp_utils.send_otp(email.email)

    return content


@app.post("/verify-otp")
async def _otp_verifier(request:Request,otp:OTP):
    return otp_utils.verify_otp(request,otp)
    
@app.post("/register")
async def _user_register(request:Request,user:UserData):
    response = register.register_user(request,user)
    return response

@app.post("/login")
async def _user_login(request:Request,creds:LoginCreds):
    response = login_user(request,creds)
    return response

@app.post("/publish-key")
async def _publish_key(request:Request,key_bundle:Union[IdentityKey,SignedKey]):
    if isinstance(key_bundle,IdentityKey):
        response = verify_identity_key(request,key_bundle)
        return response
    elif isinstance(key_bundle,SignedKey):
        response = verify_key(request,key_bundle)
        return response
@app.get("/key-bundle")
async def _get_key_bundle(request:Request,username:str):
    response = get_key_bundle(request,username)
    return response

@app.get("/check-key")
async def _check_key(request:Request,type:int):
    response = check_key(request,type)
    return response
@app.get("/profile")
async def _profile(request:Request):
    response = get_profile(request)
    return response
@app.get("/find-friend")
async def _find_friend(request:Request,username:str):
    response = get_friends(request.state.user_data['uid'],username)
    return response

@app.post("/add-friend")
async def _add_friend_relation(request:Request,addFriend:Username):
    response = add_friend_relation(request,addFriend.username)
    return response

@app.get("/friend-list")
async def _get_friend_list(request:Request):
    response = get_friend_list(request)
    return response

import json

@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    token = websocket.query_params.get('authorization')
    
    uid = await manager.connect(websocket,token)
    try:
        while True:
            print(uid)

            data = await websocket.receive_text()
            print('got',data)
            res = await manager.message_handler(data,websocket,uid)
            await websocket.send_text(res)
    except:
        await websocket.send_text("invalid request")
