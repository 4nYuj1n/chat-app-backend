import db.database as database
import bcrypt
def insert_user(cursor,conn,uid,username,password,email,profile_url,curr_time):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q="INSERT INTO user VALUES(%s,%s,%s,%s,%s)"
        p=(uid,username,email,bcrypt.hashpw(password.encode(), bcrypt.gensalt(16)),profile_url,curr_time)
        cursor.execute(q,p)
        conn.commit()
        return 'OK'
    except Exception as err:
        print(err)
        return err