import db.database as database
from db.get_max_id import get_max_id
from datetime import datetime

def insert_one_time_pqkem(uid,key,identifier):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        id=get_max_id("one_time_pq_key")
        curr=datetime.now()
        q="INSERT INTO one_time_pq_key VALUES(%s,%s,%s,%s,%s)"
        p=(id,uid,key,identifier,curr)
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
        q="SELECT count(*) FROM one_time_curve_key WHERE uid=%s"
        p=(uid,)
        cursor.execute(q,p)
        result=cursor.fetchall()[0][0]
        print(result)
        return result,None
    except Exception as err:
        return None,err