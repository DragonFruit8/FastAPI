from argon2 import PasswordHasher

class Security:
    ph = PasswordHasher()
    
    @classmethod
    def create_hash_