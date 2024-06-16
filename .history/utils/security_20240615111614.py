from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

from schemas.users import UserCreate
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")

# Fetch user data from database
user_data = fetch_user_data_from_database(email)

# Create UserCreate instance with all required data
user = UserCreate(**user_data)

class Password:
    @classmethod
    def hash_password(cls, password: str) -> str:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
def create_access_token(subject: str, expire_delta: Optional[timedelta] = None) -> str:
    ALGORITHM = "HS256"
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
    to_encode = {"sub": subject, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str):
    ALGORITHM = "HS256"
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    email = payload.get("sub")
    if not email:
        return None
    user = 
    return user


# def get_current_active_superuser(current_user: User = Depends(get_current_user)):
#     if not current_user.is_superuser:
#         raise HTTPException(status_code=401, detail="Inactive user")
#     return current_user

# def get_current_active_superuser(current_user: User = Depends(get_current_user)):
#     if not current_user.is_superuser:
#         raise HTTPException(status_code=401, detail="Inactive user")
#     return current_user    