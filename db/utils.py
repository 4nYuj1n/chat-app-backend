def get_max_id(conn,cursor,table_name):
    try:
        q=f"SELECT MAX(id) FROM {table_name} LIMIT 1"
        cursor.execute(q)
        return int(cursor.fetchall()[0][0])+1
    except Exception as err:
        print(err)