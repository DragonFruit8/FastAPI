from argon2 import PasswordHasher

class Security:
    ph = PasswordHasher()
    
    @classmethod
    def create_hash_password(cls, *, password: str) -> str:
        return cls.ph.hash(password)