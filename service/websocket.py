from fastapi import WebSocket, WebSocketDisconnect
from typing import List, Dict
from service.friends.check_is_friend import check_is_friend
from db.user import select_user_profile
from db.identity_key import select_user_identity
from db.pending_chat import select_pending_chat,insert_pending_chat
from datetime import datetime
import time
import base64
import jwt
import json
import re

'''
type of pending event : 
0 = chatting channel connection
1 = sending initial message to channel
'''
SECRET = "this_is_a_secret_token_indeed"

class ChannelCreationError(Exception):
    """Custom exception for channel creation errors"""
    pass

class ConnectionManager:
    def __init__(self):
        self.active_connections :Dict[str,WebSocket] = {}
        # self.chat_channels : Dict[str,List[str]] ={}
        self.user_channels : Dict[str,List[str]]  ={}
        self.profile_channel : Dict[str,List[str]]  ={}
        # self.pending_event : Dict[str,(str)]
    
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

            if len(data):
                for i in data:
                    print(i[2])
                    save = json.loads(re.sub("'",'"',i[2]))
                    # print(type(i[2]))
                    print(save)
                    await websocket.send_json(save)
            return uid
        else:
            return None
    
    
    def disconnect(self,websocket:WebSocket,uid:str):
        del self.active_connections[uid]
        for connections in self.channels.items():
            if websocket in connections:
                connections.remove(websocket)
    
    async def handle_chat(self,user_a:str,user_b:str,message:str):
        try:
            sender = user_a
            receiver = user_b
            print(sender,receiver)
            if int(user_a,16)>int(user_b,16):
                user_a,user_b = user_b,user_a
            if check_is_friend(user_a,user_b):
                if receiver not in self.active_connections:
                    message["timestamp"] = str(int(time.time()))
                    print("MASOK")
                    insert_pending_chat(receiver,str(message))
                else:
                    self.active_connections[receiver].send_text(message)
        except Exception as err:
            print(err)
 
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
            print(message['IK'])
            await self.handle_chat(uid,select_user_identity(message['IK'])[0],message)
            await websocket.send_text(f"successfully sending message")
        except Exception as error:
            print(error)
            await websocket.send_text(f"failed sending message")
