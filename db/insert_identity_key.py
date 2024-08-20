from datetime import datetime
from db.get_max_id import get_max_id
import db.database as database
def insert_identity_key(uid,key):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        current_time = datetime.now()
        q="INSERT INTO identity_key VALUES(%s,%s,%s)"
        p=(uid,key,current_time,)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return None