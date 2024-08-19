import db.database as database
def select_user_register(cursor,auth_token):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="SELECT * FROM user_register WHERE verif_token=%s"
        p=(auth_token,)
        cursor.execute(q,p)
        return cursor.fetchall()[0]
    except Exception as err:
        return err