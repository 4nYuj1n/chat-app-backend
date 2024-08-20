import db.database as database
def select_user_register(email):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM user_register WHERE email=%s"
        p=(email,)
        cursor.execute(q,p)
        return cursor.fetchall()[0]
    except Exception as err:
        return None,None,None