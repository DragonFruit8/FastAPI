from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from config.settings import settings
from 
from schemas.users import UserCreate



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

