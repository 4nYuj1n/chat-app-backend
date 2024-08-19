import secrets
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, '../server')

import db.database as database
from db import check_uid
def generate_uid():
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    uid = secrets.token_hex(6)
    while True:
        if len(check_uid(cursor,uid)) == 0 :
            return uid

