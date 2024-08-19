import db.database as database
def select_otp_verify(email):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    q="SELECT * FROM otp_verify WHERE email = %s"
    p=(email,)
    cursor.execute(q,p)
    data=cursor.fetchall()
    data=list(data[0])
    return data