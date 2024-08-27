from fastapi import WebSocket, WebSocketDisconnect
from typing import List, Dict
from service.friends import check_is_friend
from db.user import select_user_profile
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
    
    async def create_channel(self,message:str):
        user_a,user_b = base64.b64decode(message).split(',')
        try:
            if int(user_a,16)>int(user_b,16):
                user_a,user_b = user_b,user_a
            user_a,user_b = user_a.decode('utf-8'),user_b.decode('utf-8')
        except:
            raise ChannelCreationError(f"Invalid User")
        
        if not (select_user_profile(user_a)) or not(select_user_profile(user_b)):
            raise ChannelCreationError(f"Invalid User")
        
        if check_is_friend(user_a,user_b):
            channel_name = f"{user_a}_{user_b}"
            self.chat_channels[channel_name] = []
            self.chat_channels[channel_name].append(user_a)
            self.chat_channels[channel_name].append(user_b)

        else:
            raise ChannelCreationError(f"Invalid User")
    
    async def message_handler(self,data,websocket,uid):
        data=json.loads(data)
        try:
            message_type = int(data['type'])
            message = data['message']
        except Exception as err:
            print(err)
            await websocket.send_text(f"invalid message")
        
        if message_type == 0:
            await websocket.send_text(f"connection established")
        #create message channel
        if message_type == 1:
            await websocket.send_text(f"{message}")
            try:
                return "OK"

                await self.create_channel(message)
                await websocket.send_text(f"channel created")
            except:
                await websocket.send_text(f"channel creation failed")