from datetime import datetime
from db.get_max_id import get_max_id
import db.database as database
def insert_otp_verify(email,OTP):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        current_time = datetime.now()
        max_id=get_max_id("otp_verify")
        q="INSERT INTO otp_verify VALUES(%s,%s,%s,%s)"
        p=(max_id,email,OTP,current_time)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return None