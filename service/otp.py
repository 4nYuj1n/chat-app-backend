import smtplib
import random
import db.database as database
import secrets
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime


<<<<<<< HEAD:service/otp.py
=======
def get_otp_from_db(auth_token):
    try:
        conn=db_utils.db_connect()
        q="SELECT * FROM otp_verify_tbl WHERE verif_token = %s"
        p=(auth_token,)
        data=conn.select_data(q,p)
        data=list(data[0])
        return data[0],data[2],data[3],data[4]
    except:
        return None,None,None,None
        
def save_otp_to_db(email,token,OTP):
    conn=db_utils.db_connect()
    current_time = datetime.now()
    max_id=conn.get_max_id("otp_verify_tbl")
    q="INSERT INTO otp_verify_tbl VALUES(%s,%s,%s,%s,%s)"
    p=(email,token,OTP,current_time,max_id)
    simpan=conn.insert_data(q,p)
    conn.close_db()
    if  simpan != None:
        return "failed"
    else:
        return "success"

>>>>>>> e45bd02374a06e74b8b76a9383baf5b627506c6b:otp_utils.py
def send_otp(email):
    try:
        OTP = random.randint(100000,999999)
        auth_token = secrets.token_hex(32)
        sender_email="lala@mail.id"
        receiver_email=email
        with smtplib.SMTP('localhost', 1025) as smtpServer:    
            text=f"""
            your OTP is {OTP}
            """
            message = MIMEText(text, "plain")
            message["Subject"] = "Plain text email"
            message["From"] = sender_email
            message["To"] = receiver_email
            smtpServer.sendmail(sender_email,receiver_email,message.as_string())
        
        if database.save_otp_to_db(email,auth_token,OTP)==None:
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Email send successfully",
                "authorization" : str(auth_token),
            }
        else:
            raise Exception("failed saving otp")

    except Exception as err:
        print(err)
        return{
            "code" : "200",
            "status" : "failed",
            "message" : "Email sending failed"
        }

def verify_otp(otp):
    email,db_otp,time_init,id=database.get_otp_from_db(otp.authorization)
    if db_otp==otp.otp:
        auth_token = secrets.token_hex(32)
        conn=database.db_connect()
        conn.delete_otp_token(id)
        current_time=datetime.now()
        if conn.insert_register_token(email,auth_token,current_time) =="OK":
            conn.close_db()
            return{
            "code" : "200",
            "status" : "success",
            "message" : "OTP Verified",
            "authorization" : auth_token,
            }
        else:
            return{
                "code" : "200",
                "status" : "failed",
                "messsage" : "failed updating auth token",
            }
    else:
       return{
                "code" : "200",
                "status" : "failed",
                "messsage" : "failed verifying otp token",
        }
    