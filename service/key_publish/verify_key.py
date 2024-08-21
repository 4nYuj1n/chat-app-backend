from db.curve_key import insert_curve_key
from db.last_resort_pqkem import insert_last_resort_pqkem
from db.one_time_curve_key import insert_one_time_curve_key
from db.one_time_pqkem import insert_one_time_pqkem


def verify_key(request,key_bundle):
    #curve prekey
    if key_bundle.type==1:
        if insert_curve_key(request.state.user_data['uid'],key_bundle.key,key_bundle.identifier,key_bundle.signature):
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Key published",
            }
        else:
            return{
                "code" : "500",
                "status" : "failed",
                "messsage" : "failed publishing key",
            }
    elif key_bundle.type==2:
        if insert_last_resort_pqkem(request.state.user_data['uid'],key_bundle.key,key_bundle.identifier,key_bundle.signature):
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Key published",
            }
        else:
            return {
                "code" : "500",
                "status" : "failed",
                "message" : "failed publishing key",
            }
    elif key_bundle.type==3:
        if insert_one_time_curve_key(request.state.user_data['uid'],key_bundle.key,key_bundle.identifier):
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Key published",
            }
        else:
            return {
                "code" : "500",
                "status" : "failed",
                "message" : "failed publishing key",
            }
    elif key_bundle.type==4:
        if insert_one_time_pqkem(request.state.user_data['uid'],key_bundle.key,key_bundle.identifier,key_bundle.signature):
            return {
                "code" : "200",
                "status" : "success",
                "message" : "Key published",
            }
        else:
            return{
                "code" : "500",
                "status" : "failed",
                "message" : "failed publishing key",
            }
    else:
        return{
            "code" : "500",
            "status" : "failed",
            "message" : "invalid type",
        }
