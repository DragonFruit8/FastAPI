from argon2 import PasswordHasher
from models.


class Password:
    ph = PasswordHasher()
    
    @classmethod
    def create_hash_password(cls, *, password: str) -> str:
        user.password = cls.ph.hash(password)
        return cls.ph.hash(password)