import db.database as database
def delete_otp_verify(id):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="DELETE FROM otp_verify WHERE id=%s"
        p=(id,)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return err
    