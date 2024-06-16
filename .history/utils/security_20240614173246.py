import bcrypt
from jose import JWTError, jwt
from typing import Optional

class Password:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        try:
            return cls.check_password(plain_password, hashed_password)
        except ValueError:
            return False
    @staticmethod
    def check_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
def create_access_token(data: dict, secret_key: str, expires_delta: Optional[datetime]) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": expires_delta})
    return jwt.encode(to_encode, secret_key, algorithm="HS256")