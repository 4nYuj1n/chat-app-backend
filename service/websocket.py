from fastapi import WebSocket, WebSocketDisconnect
from typing import List, Dict
from service.friends.check_is_friend import check_is_friend
from db.user import select_user_profile
from db.identity_key import select_user_identity
from db.pending_chat import select_pending_chat,insert_pending_chat,delete_pending_chat
from datetime import datetime
import time
import base64
import jwt
import json
import re

SECRET = "this_is_a_secret_token_indeed"

class ChannelCreationError(Exception):
    """Custom exception for channel creation errors"""
    pass

class ConnectionManager:
    def __init__(self):
        self.active_connections :Dict[str,WebSocket] = {}
        self.user_channels : Dict[str,List[str]]  ={}
    
    def parse_token(self,token:str):
        try:
            data=jwt.decode(
                token,
                SECRET,
                algorithms=["HS256"]
            )
            uid = data['uid']
            return True,uid
        except:
            return False,None

    async def connect(self,websocket:WebSocket,token:str):
        valid,uid = self.parse_token(token)
        if valid:
            await websocket.accept()
            self.active_connections[uid]=websocket
            data = select_pending_chat(uid)
            data_send = []
            if len(data):
                for i in data:
                    save = json.loads(re.sub("'",'"',i[2]))
                    data_send.append(save)
                delete_pending_chat(uid)
                await websocket.send_json(data_send[::-1])
            return uid
        else:
            return None
    
    
    def disconnect(self,websocket:WebSocket,uid:str):
        del self.active_connections[uid]
        for connections in self.channels.items():
            if websocket in connections:
                connections.remove(websocket)
    
    async def handle_chat(self,websocket,user_a,user_b,message):
        try:
            sender = user_a
            receiver = user_b
            print(sender,receiver)
            if int(user_a,16)>int(user_b,16):
                user_a,user_b = user_b,user_a
            if check_is_friend(user_a,user_b):
                message["uid"] = sender
                if receiver not in self.active_connections:
                    print("ORANGNYA OFF")
                    print("MASOK")
                    insert_pending_chat(receiver,str(message))
                else:
                    print("ORANGNYA ON")
                    self.active_connections[receiver].send_text(message)
                await websocket.send_text(f"successfully sending message")
                
        except Exception as err:
            print(err)
            await websocket.send_text(f"failed sending message")
 
    async def message_handler(self,data,websocket,uid):
        try:
            data=json.loads(data)
            message_type = int(data['type'])
            message = data['message']
            print(message)
        except Exception as err:
            print(err)
            await websocket.send_text(f"invalid message")
        try:
            print('='*32)
            if message['type'] == '1':
                print(message['IK1'])
                temp = select_user_identity(message['IK2'])
                print(temp[0])
                await self.handle_chat(websocket,uid,temp[0],message)
            elif message['type'] == '2':
                await self.handle_chat(websocket,uid,message['receiver'],message)
        except Exception as error:
            print(error)
            await websocket.send_text(f"failed sending message")
