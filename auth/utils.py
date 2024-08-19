import secrets
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, '../server')

import db.database as database

def generate_uid():
    conn=database.db_connect()
    uid = secrets.token_hex(6)
    while True:
        if len(conn.check_uid(uid)) == 0 :
            return uid

