from db.curve_key import insert_curve_key
import base64

def verify_key(request,key_bundle):
    #curve prekey
    if key_bundle.type==1:
        if insert_curve_key(request.state.user_data['uid'],key_bundle.key,key_bundle.identifier,key_bundle.signature) == "OK":
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