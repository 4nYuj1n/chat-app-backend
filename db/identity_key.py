from datetime import datetime
from db.get_max_id import get_max_id
import db.database as database
def select_identity_key(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM identity_key WHERE uid=%s"
        p=(uid,)
        cursor.execute(q,p)
        return cursor.fetchall()
    except Exception as err:
        print(err)
        return False

def select_user_identity(ik):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()

    try:
        q="SELECT * FROM identity_key WHERE key_value_x=%s"
        p=(ik,)
        cursor.execute(q,p)
        temp = cursor.fetchall()
        print(temp)
        print(temp[0][0])
        print("YA BEGINILAH")
        return temp[0]
    except Exception as err:
        print(err)
        return False

def update_identity_key(uid,key,key_x):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    curr = datetime.now()
    try:
        q="UPDATE identity_key SET key_value=%s,key_value_x=%s,created_at=%s  WHERE uid=%s"
        p=(key,key_x,str(datetime.now()),uid)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return False
    
def insert_identity_key(uid,key,key_x):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        current_time = datetime.now()
        q="INSERT INTO identity_key VALUES(%s,%s,%s,%s)"
        p=(uid,key,key_x,current_time,)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return False