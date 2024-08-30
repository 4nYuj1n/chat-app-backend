from db.friend import select_friend_relation
from db.user import select_user_profile
def get_friend_list(request):
    uid = request.state.user_data['uid']
    data = select_friend_relation(uid)
    friend_data= [] 
    for user in data:
        temp = select_user_profile(user[0])
        print(temp)
        data = {
            "uid" : temp[0],
            "username" : temp[1],
            "profile_url" : temp[4],
            "IKX" : temp[8],
        }
        friend_data.append(data)
    if data != None:
        return {
            "code" : "200",
            "status" : "success",
            "message" : friend_data
        }
    else:
        return{
            "code" : "500",
            "status" : "failed",
            "message" : "user not found"
        }