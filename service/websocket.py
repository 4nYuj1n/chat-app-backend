from fastapi import WebSocket, WebSocketDisconnect
from typing import List, Dict
from service.friends.check_is_friend import check_is_friend
from db.user import select_user_profile
from db.identity_key import select_user_identity
import base64
import jwt
import json
'''
type of pending event : 
0 = chatting channel connection

'''
SECRET = "this_is_a_secret_token_indeed"

class ChannelCreationError(Exception):
    """Custom exception for channel creation errors"""
    pass

class ConnectionManager:
    def __init__(self):
        self.active_connections :Dict[str,WebSocket] = {}
        self.chat_channels : Dict[str,List[str]] ={}
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
            return uid
        else:
            return None
    
    
    def disconnect(self,websocket:WebSocket,uid:str):
        del self.active_connections[uid]
        for connections in self.channels.items():
            if websocket in connections:
                connections.remove(websocket)
    
    async def create_channel(self,user_a:str,user_b:str):
        try:
            if int(user_a,16)>int(user_b,16):
                user_a,user_b = user_b,user_a
        except:
            raise ChannelCreationError(f"Invalid User")
        
        if (select_user_profile(user_a) == None) or (select_user_profile(user_b) == None):
            raise ChannelCreationError(f"Invalid User")
        if check_is_friend(user_a,user_b):
            channel_name = f"{user_a}_{user_b}"
            if user_a not in self.chat_channels:
                self.chat_channels[user_a] = []
            if user_b not in self.chat_channels:
                self.chat_channels[user_b] = []

            self.chat_channels[user_a].append(channel_name)
            self.chat_channels[user_b].append(channel_name)
            print("AMAN")

        else:
            raise ChannelCreationError(f"Invalid User")
    
    async def message_handler(self,data,websocket,uid):
        try:
            data=json.loads(data)
            message_type = int(data['type'])
            message = data['message']
        except Exception as err:
            print(err)
            await websocket.send_text(f"invalid message")
        
        if message_type == 0:
            await websocket.send_text(f"connection established")
        #create message channel
        if message_type == 1:
            try:
  
                await self.create_channel(uid,select_user_identity(message['IK'])[0])
                await websocket.send_text(f"channel created")
            except Exception as err:
                print(err)
                await websocket.send_text(f"channel creation failed")