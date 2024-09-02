from db.friend import select_friend_relation
def check_is_friend(uid1,uid2):
    try:
        data = select_friend_relation(uid1,uid2)
        print('check is friend : ',data)
        if data == None:
            return False
        if len(data) == 0:
            return False
        return True
    except Exception as err:
        print(err)
        return False