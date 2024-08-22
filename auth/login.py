from db.user import select_user_creds
from service.generate_jwt import generate_jwt
def login_user(request,creds):
    email = creds.email
    password = creds.password
    data = select_user_creds(email,password)

    if data == None:
        return {
            "code" : "500",
            "status" : "failed",
            "message" : "Failed logging in"
        }
    else:
        jwt = generate_jwt({"uid":data[0]})

        return {
            "code" : "200",
            "status" : "success",
            "message" : "Sucessfully logged in",
            "authorization" : jwt
        }