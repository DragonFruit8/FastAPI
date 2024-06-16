from bcrypt import hashpw, gensalt, checkpw
from jose.jwt import encode as jwt_encode
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

from schemas.users import UserCreate
from config.settings import settings
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")
# Rest of the code...

class Password:
@
def create_access_token(subject: str, expire_delta: Optional[timedelta] = None) -> str::
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
    to_encode = {"sub": subject, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


# Rest of the code...
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    email = payload.get("sub")
    if not email:
        return None
    user = User.find_one(User.email == email)
    return user


# def get_current_active_superuser(current_user: User = Depends(get_current_user)):
#     if not current_user.is_superuser:
#         raise HTTPException(status_code=401, detail="Inactive user")
#     return current_user

# def get_current_active_superuser(current_user: User = Depends(get_current_user)):
#     if not current_user.is_superuser:
#         raise HTTPException(status_code=401, detail="Inactive user")
#     return current_user    