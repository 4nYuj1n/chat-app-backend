from db.user import select_user
def get_friends(username):
    response = select_user(username)
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
        }
    }