from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from models.users import User
from schemas.users import UserCreate
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/access-token")

class Password:
    @classmethod
    def hash_password(cls, password: str) -> str:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
def create_access_token(subject: str, expire_delta: Optional[timedelta] = None) -> str:
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": subject, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    email = payload.get("sub")
    if not email:
        return None
    user = await User.find_one(User.email == email)
    if not user:
        return None
    user = User.get
    