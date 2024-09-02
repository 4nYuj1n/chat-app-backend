import db.database as database
import bcrypt
def select_user(username):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM user WHERE username = %s"
    p=(username,)
    cursor.execute(q,p)
    data=cursor.fetchall()
    if len(data)!=0:
        data=list(data[0])
        return data
    else:
        return None

def select_user_email(email):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM user WHERE email = %s"
    p=(email,)
    cursor.execute(q,p)
    data=cursor.fetchall()
    if len(data)!=0:
        data=list(data[0])
        return data
    else:
        return None
def select_user_creds(email,password):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM user WHERE email = %s"

    p=(email,)
    cursor.execute(q,p)
    data=cursor.fetchall()

    if len(data)!=0 and bcrypt.checkpw(password.encode(),data[0][3].encode()):
        data=list(data[0])
        return data
    else:
        return None
def select_user_profile(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM user LEFT JOIN identity_key ON identity_key.uid = user.uid WHERE user.uid = %s"
    p=(uid,)
    cursor.execute(q,p)
    data=cursor.fetchall()
    if len(data)!=0:
        data=list(data[0])
        return data
    else:
        return None