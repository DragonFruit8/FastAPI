import bcrypt
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime

class Password:
    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        try:
            return cls.check_password(plain_password, hashed_password)
        except ValueError:
            return False

    @classmethod
    def check_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        
    def create_access_token(data: dict, secret_key: str, expires_delta: Optional[datetime]) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": expires_delta})
        return jwt.encode(to_encode, secret_key, algorithm="HS256")
    
def create_access_token(subject: str, expire_delta: Optional[datetime]) -> str:
    if expire_delta:
        expire =     