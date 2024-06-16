from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field, EmailStr


class User(Document):
    email: EmailStr
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
    
    @classmethod
    async def get_by_email(cls, email: str) -> "User":
        return await cls.find_one(cls.email == email)