from cryptography.hazmat.primitives.asymmetric import ed25519
from db.insert_identity_key import insert_identity_key
import base64
def verify_identity_key(request,key_bundle):
    try:

        ed25519.Ed25519PublicKey.from_public_bytes(base64.b64decode(key_bundle.key))
        if insert_identity_key(request.state.user_data['uid'],key_bundle.key) == "OK":

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
    except Exception as err:
        print(err)
        return{
                "code" : "500",
                "status" : "failed",
                "messsage" : "failed failed publishing key",
        }
