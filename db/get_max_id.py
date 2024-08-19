import db.database as database
def get_max_id(table_name):
    db=database.db_connect()
    conn,cursor=db.get_conn_and_cursor()
    try:
        q=f"SELECT MAX(id) FROM {table_name} LIMIT 1"
        cursor.execute(q)
        return int(cursor.fetchall()[0][0])+1
    except Exception as err:
        print(err)