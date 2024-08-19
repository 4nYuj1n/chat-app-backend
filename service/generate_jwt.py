from datetime import datetime,timedelta

import jwt

SECRET = "this_is_a_secret_token_indeed"
def generate_jwt(data):
    content={"exp":datetime.now()+timedelta(days=7)}
    content.update(data)
    return jwt.encode(content, SECRET, algorithm='HS256')