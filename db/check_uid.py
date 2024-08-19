import db.database as database
def check_uid(uid):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q=f"SELECT * FROM user WHERE uid=%s"
        p=(uid,)
        cursor.execute(q,p)
        temp=cursor.fetchall()
        return temp
    except Exception as err:
        print(err)