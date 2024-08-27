import db.database as database
from datetime import datetime

def insert_last_resort_pqkem(uid,key,identifier,signature):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        curr=datetime.now()
        q="INSERT INTO pq_key VALUES(%s,%s,%s,%s,%s)"
        p=(uid,key,identifier,signature,curr)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return err
def select_last_resort_pqkem(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM pq_key WHERE uid=%s ORDER BY id DESC LIMIT 1"
        p=(uid,)
        cursor.execute(q,p)
        row=cursor.fetchone()
        return row
    except Exception as err:
        print(err)
        return None