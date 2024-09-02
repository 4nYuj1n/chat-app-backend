import secrets
import sys
import os



from db.check_uid import check_uid
def generate_uid():
    uid = secrets.token_hex(6)
    while True:
        if len(check_uid(uid)) == 0 :
            return uid

