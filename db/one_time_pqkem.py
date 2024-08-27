import db.database as database
from db.get_max_id import get_max_id
from datetime import datetime

def select_one_time_pqkem(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM one_time_pq_key WHERE uid=%s LIMIT 1"
        p=(uid,)
        cursor.execute(q,p)
        return cursor.fetchone()
    except Exception as err:
        print(err)
        return None

def insert_one_time_pqkem(uid,key,identifier,signature):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        id=get_max_id("one_time_pq_key")
        curr=datetime.now()
        q="INSERT INTO one_time_pq_key VALUES(%s,%s,%s,%s,%s,%s)"
        p=(id,uid,key,identifier,signature,curr)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return err

def count_one_time_pqkem(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT count(*) FROM one_time_pq_key WHERE uid=%s"
        p=(uid,)
        cursor.execute(q,p)
        result=cursor.fetchall()[0][0]
        return result,None
    except Exception as err:
        return None,err