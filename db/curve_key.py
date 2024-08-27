import db.database as database
from datetime import datetime

def select_curve_key(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM curve_prekey WHERE uid=%s"
        p=(uid,)
        cursor.execute(q,p)
        return cursor.fetchall()
    except Exception as err:
        print(err)
        return err
def insert_curve_key(uid,key,identifier,signature):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        curr=datetime.now()
        q="INSERT INTO curve_prekey VALUES(%s,%s,%s,%s,%s)"
        p=(uid,key,identifier,signature,curr)
        cursor.execute(q,p)
        conn.commit()
        return True
    except Exception as err:
        print(err)
        return err
