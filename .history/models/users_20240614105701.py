from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field, EmailStr, ConfigDict


class User(Document):
    email: EmailStr
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
    arbitray
    
    