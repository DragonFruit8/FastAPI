class Password:
    @staticmethod
    def create_access_token(subject: str, expire_delta: Optional[timedelta] = None) -> str:
        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
        to_encode = {"sub": subject, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    # Rest of the code...
