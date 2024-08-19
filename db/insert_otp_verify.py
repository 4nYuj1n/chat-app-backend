from datetime import datetime
from db import get_max_id
import db.database as database
def insert_otp_verify(email,token,OTP):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        current_time = datetime.now()
        max_id=get_max_id("otp_verify")
        q="INSERT INTO otp_verify VALUES(%s,%s,%s,%s,%s)"
        p=(email,token,OTP,current_time,max_id)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except:
        return None