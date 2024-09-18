import smtplib
import random
import sys
import os
import secrets
from email.mime.text import MIMEText
from datetime import datetime
from mailjet_rest import Client

# Add the parent directory to sys.path
sys.path.insert(0, '../server')
from db.otp import insert_otp_verify,select_otp_verify,delete_otp_verify,update_otp_verify
from db.user import select_user_email
from db.insert_user_register import insert_user_register

mailjet = Client(auth=(api_key, secret_key), version='v3.1')
def send_email(email,OTP):
    sender_email="jossie@tennet.id"
    receiver_email=email
    data = {
    'Messages': [
    {
      "From": {
        "Email": sender_email,
        "Name": sender_email,
      },
      "To": [
        {
          "Email": receiver_email,
          "Name":  receiver_email,
        }
      ],
      "Subject": "OTP Verification",
      "TextPart": str(OTP),
    #   "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
    }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    # with smtplib.SMTP('localhost', 1025) as smtpServer:    
    #     text=f"""
    #     your OTP is {OTP}
    #     """
    #     message = MIMEText(text, "plain")
    #     message["Subject"] = "Plain text email"
    #     message["From"] = sender_email
    #     message["To"] = receiver_email
    #     smtpServer.sendmail(sender_email,receiver_email,message.as_string())

def send_otp(email):
    try:
        if select_user_email(email) == None:
            OTP = random.randint(100000,999999)
            send_email(email,OTP)
            if select_otp_verify(email)[0]==None:
                if insert_otp_verify(email,OTP)=='OK':
                    return {
                        "code" : "200",
                        "status" : "success",
                        "message" : "Email send successfully",
                    }
                else:
                    raise Exception("failed saving otp")
            else:
                if update_otp_verify(email,OTP)=='OK':
                    return {
                        "code" : "200",
                        "status" : "success",
                        "message" : "Email send successfully",
                    }
                else:
                    raise Exception("failed saving otp")
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
    email = request.state.user_data['email']
    id,email,db_otp,_=select_otp_verify(email)
    if id==None:

        return{
            "code" : "500",
            "status" : "failed",
            "messsage" : "failed verifying OTP",
        }      
    elif db_otp==otp.otp:

        temp = delete_otp_verify(id)
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
    