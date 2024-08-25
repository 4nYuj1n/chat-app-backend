from db.friend import select_friend_relation
def check_is_friend(uid1,uid2):
    data = check_is_friend(uid1,uid2)
    if data == None:
        return False
    if len(data) == 0:
        return False
    return True
    