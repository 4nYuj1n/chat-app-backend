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
def select_otp_verify(email):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM otp_verify WHERE email = %s"
    p=(email,)
    cursor.execute(q,p)
    data=cursor.fetchall()
    if len(data)!=0:
        print(data[0])
        data=list(data[0])
        return data
    else:
        return None,None,None,None
    
def delete_otp_verify(id):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="DELETE FROM otp_verify WHERE id=%s"
        p=(id,)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return err
    
def update_otp_verify(email,OTP):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="UPDATE otp_verify SET otp=%s WHERE email=%s"
        p=(OTP,email,)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return err