import bcrypt

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
        