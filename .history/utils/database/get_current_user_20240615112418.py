from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config.settings import settings
from models.user import User
from schemas.user import UserOut

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")


# def get_current_active_superuser(current_user: User = Depends(get_current_user)):
#     if not current_user.is_superuser:
#         raise HTTPException(status_code=401, detail="Inactive user")
#     return current_user


def get_current_user(token: str = Depends(oauth2_scheme) ):
    ALGORITHM = "HS256"
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    email = payload.get("sub")
    if not email:
        return None
    user = User.get_by_email( email=email)
    return user