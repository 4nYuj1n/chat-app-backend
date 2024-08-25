from cryptography.hazmat.primitives.asymmetric import ed25519
from db.identity_key import select_identity_key,update_identity_key,insert_identity_key
import base64
def verify_identity_key(request,key_bundle):
    try:
        print("MASUK")
        ed25519.Ed25519PublicKey.from_public_bytes(base64.b64decode(key_bundle.identity_key))
        if len(select_identity_key(request.state.user_data['uid'])) == 0:
            if insert_identity_key(request.state.user_data['uid'],key_bundle.identity_key):
                return {
                    "code" : "200",
                    "status" : "success",
                    "message" : "Key published",
                }
            else:
                raise Exception
        else:
            if update_identity_key(request.state.user_data['uid'],key_bundle.identity_key):
               return {
                   "code" : "200",
                   "status" : "success",
                   "message" : "Key published",
               }
            
            else:
               raise Exception
    except Exception as err:
        print(err)
        return{
                "code" : "500",
                "status" : "failed",
                "messsage" : "failed failed publishing key",
        }
