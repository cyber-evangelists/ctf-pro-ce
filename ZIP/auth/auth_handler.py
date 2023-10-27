
import time
from typing import Dict
import os
import jwt
import dotenv
dotenv.load_dotenv()


JWT_SECRET = os.environ.get("SECRET")
JWT_ALGORITHM = os.environ.get("ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }
def signJWT(email: str) -> Dict[str, str]:
    payload = {
        "email": email,
        "expires": time.time() + 86400
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        return {}


