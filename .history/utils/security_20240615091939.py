from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from config.settings import settings


class Password:
    @classmethod
    def hash_password(cls, password: str) -> str:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    @classmethod
    def verify_password( cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    @classmethod
    def create_access_token(cls, subject: str, expire_delta: Optional[timedelta] = None) -> str:
        to_encode = {"sub": subject}
        if expire_delta:
            expire = datetime.utcnow() + timedelta(minutes=expire_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    
def create_access_token(subject: str, expire_delta: Optional[timedelta] = None) -> str:
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": subject, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    