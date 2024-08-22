from db.user import select_user_profile
def get_profile(request):
    uid = request.state.user_data['uid']
    response = select_user_profile(uid)
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
            "email" : response[2],
            "profile_url" : response[4],
        }
    }
