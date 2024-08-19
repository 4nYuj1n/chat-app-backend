import db.database as database
def delete_user_register(email):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="DELETE FROM user_register WHERE email=%s"
        p=(email,)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        return err