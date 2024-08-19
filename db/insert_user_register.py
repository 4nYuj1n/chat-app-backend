import db.database as database
from db.get_max_id import get_max_id
def insert_user_register(email,curr_time):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        id=get_max_id('user_register')
        q="INSERT INTO user_register VALUES(%s,%s,%s)"
        p=(id,email,curr_time)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return err