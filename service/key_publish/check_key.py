from db.one_time_curve_key import count_one_time_curve_key
from db.one_time_pqkem import count_one_time_pqkem
def check_key(request,_type):
    if  _type == 1:
        cnt,err = count_one_time_curve_key(request.state.user_data['uid'])
        if err == None:
            return {
                    "code" : "200",
                    "status" : "success",
                    "message" : {
                        "count" : cnt
                    },
            }
        else:
            print(err)
            return {
                    "code" : "500",
                    "status" : "faied",
                    "message" : "failed fetching keys"
            }
    elif _type == 2:
        cnt,err = count_one_time_pqkem(request.state.user_data['uid'])
        if err == None:
            return {
                    "code" : "200",
                    "status" : "success",
                    "message" : {
                        "count" : cnt
                    },
            }
        else:
            print(err)
            return {
                    "code" : "500",
                    "status" : "faied",
                    "message" : "failed fetching keys"
            }     
    else:
        return {
                    "code" : "500",
                    "status" : "faied",
                    "message" : "failed fetching keys"
        }