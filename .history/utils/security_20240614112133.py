from argon2 import PasswordHasher


class Password:
    
    ph = PasswordHasher()
    
    @classmethod
    def create_hash_password(cls, password: str):
        = cls.ph.hash(password)
        return user.password
    
    