import smtplib
import random
import sys
import os
import secrets
from email.mime.text import MIMEText
from datetime import datetime
# Add the parent directory to sys.path
sys.path.insert(0, '../server')
from db.insert_otp_verify import insert_otp_verify
from db.select_otp_verify import select_otp_verify 
from db.delete_otp_verify import delete_otp_verify 
from db.insert_user_register import insert_user_register


def send_email(email,OTP):
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

def send_otp(email):
    try:
        OTP = random.randint(100000,999999)
        send_email(email,OTP)
        if insert_otp_verify(email,OTP)=='OK':
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Email send successfully",
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

def verify_otp(request,otp):
    email = request.state.user['email']
    id,email,db_otp,_=select_otp_verify(email)
    if db_otp==otp.otp:
        delete_otp_verify(id)
        current_time=datetime.now()
        if insert_user_register(email,current_time) =="OK":
            return{
            "code" : "200",
            "status" : "success",
            "message" : "OTP Verified",
            }
        else:
            return{
                "code" : "500",
                "status" : "failed",
                "messsage" : "failed verifying OTP",
            }
    else:
       return{
                "code" : "500",
                "status" : "failed",
                "messsage" : "failed verifying OTP",
        }
    