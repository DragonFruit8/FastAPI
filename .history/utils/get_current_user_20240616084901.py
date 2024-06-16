from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config.settings import settings
from models.users import User
from schemas.users import UserOut

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")

async def get_current_user(token: str = Depends(oauth2_scheme) ):
    ALGORITHM = "HS256"
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    email = payload.get("sub")
    if not email:
        return None
    user = await User.get_by_email( email=email)
    return user

async def get_current_active_user(token: str = Depends(oauth2_scheme) ):
    user = await get_current_user(token)
    if not user.is_active:
        return None
    return UserOut(email=user.email, created_at=user.created_at.isoformat())

async def get_admin(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token)
    if not user.is_admin:
        return None
    return UserOut(email=user.email, created_at=user.created_at.isoformat())

async def get_admin(email: str):
    User.find_one(User.is_superuser == True)
    if not user.is_admin:
        return None
    return UserOut(email=user.email, created_at=user.created_at.isoformat())