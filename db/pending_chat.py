import db.database as database
from db.get_max_id import get_max_id
from datetime import datetime

def select_pending_chat(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM message_sent WHERE receiver=%s"
        p=(uid,)
        cursor.execute(q,p)
        return cursor.fetchall()
    except Exception as err:
        return None,err

def insert_pending_chat(receiver,message):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        id=get_max_id("message_sent")
        curr=datetime.now()
        q="INSERT INTO message_sent VALUES(%s,%s,%s,%s)"
        p=(id,receiver,message,curr)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return False