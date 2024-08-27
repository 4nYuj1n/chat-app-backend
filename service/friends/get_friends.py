from db.user import select_user
from service.friends.check_is_friend import check_is_friend
def get_friends(uid1,username):
    response = select_user(username)
    uid2 = response[0]
    if check_is_friend(uid1,uid2):
        friends = "true"
    else:
        friends = "false"
    if response == None:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "user not found"
        }
    return {
        "code" : "200",
        "status" : "success",
        "message" : {
            "username" : response[1],
            "profile_url" : response[4],
            "friends" : friends
        }
    }