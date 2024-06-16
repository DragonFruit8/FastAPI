from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field, EmailStr
from pydantic_core import CoreSchema, core_schema


class User(Document):
    email: EmailStr
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
    @classmethod
    def
    
    