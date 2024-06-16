from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field


class User(Document):
    email: Indexed( )
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False