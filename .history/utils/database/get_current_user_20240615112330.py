from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config.settings import settings
from schemas.user import UserOut
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")


def get_current_user(token: str = Depends(oauth2_scheme) ):
    ALGORITHM = "HS256"
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    email = payload.get("sub")
    if not email:
        return None
    user = User.get_by_email( email=email)
    return user