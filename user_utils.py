import db_utils
from datetime import datetime
def register_user(user):
    conn=db_utils.db_connect()
    id,auth_token,email,curr_time=conn.select_register_token(user.authorization)
    if auth_token==user.authorization:
        conn.register_user(user.username,user.password,email,datetime.now())