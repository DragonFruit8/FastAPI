from datetime import datetime
from typing import Optional

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
    async def authenticate(cls, email: str, password: str):
        user = await cls.find_one(cls.email == email)
        if not user or not Password.verify_password(
            plain_password=password,
            hashed_password=user.hashed_password
        ):
            return 
        return user