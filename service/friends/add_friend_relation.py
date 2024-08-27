from db.friend import insert_friend_relation
from service.friends.check_is_friend import check_is_friend
from db.user import select_user
def add_friend_relation(request,username2):
    uid1=request.state.user_data['uid']
    uid2=select_user(username2)[0]
    if uid2 == None:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "Failed adding friend",
        }
    if check_is_friend(uid1,uid2):
        return {
            "code" : "200",
            "status" : "success",
            "message" : "Friend added",
        }
    if insert_friend_relation(uid1,uid2):
        return {
            "code" : "200",
            "status" : "success",
            "message" : "Friend added",
        }
    else:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "Failed adding friend",
        }