import db.database as database
from db.get_max_id import get_max_id
from datetime import datetime
def insert_friend_relation(uid1,uid2) -> bool:
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        current_time = datetime.now()
        max_id=get_max_id("friend_relation")
        q="INSERT INTO friend_relation VALUES(%s,%s,%s,%s)"
        p=(max_id,uid1,uid2,current_time)
        cursor.execute(q,p)
        conn.commit()
        max_id=get_max_id("friend_relation")
        q="INSERT INTO friend_relation VALUES(%s,%s,%s,%s)"
        p=(max_id,uid2,uid1,current_time)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return False

def select_friend_relation(uid1,uid2=None):
    db=database.db_connect()
    print(uid1,uid2)
    conn,cursor=db.get_conn_and_cursor()
    try:
        if uid2==None:
            q="SELECT uid2 FROM friend_relation WHERE uid1=%s"
            p=(uid1,)
        else:
            q="SELECT * FROM friend_relation WHERE uid1=%s and uid2=%s"
            p=(uid1,uid2,)
        cursor.execute(q,p)
        rows=cursor.fetchall()
        return rows
    except Exception as err:
        print(err)
        return None