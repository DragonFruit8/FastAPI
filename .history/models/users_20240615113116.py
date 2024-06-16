from datetime import datetime
from typing import Optional
from utils.security import Password
from models.users import User

from beanie import Document, Indexed
from pydantic import Field, EmailStr 


class User(Document):
    email: EmailStr
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
    
    @classmethod
    async def get_by_email(cls, *, email: str) -> Optional["User"]:
        return await cls.find_one(cls.email == email)
    
    @classmethod
    async def authenticate(cls, email: str, password: str) -> Optional["User"]:
        user = await cls.find_one(cls.email == email)
        if not user or not Password.verify_password(
            plain_password=password,
            hashed_password=user.hashed_password
        ):
            return None
        return user
    
    @classmethod
    async def create(cls, email: str, password: str) -> "User":
        hashed_password = Password.hash_password(password)
        user = cls(email=email, hashed_password=hashed_password)
        await user.save()
        return user