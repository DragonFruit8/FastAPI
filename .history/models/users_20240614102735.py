from beanie import Document, Indexed
from datetime import datetime
from pydantic import Field, Optional


class User(Document):
    email: Indexed(str, unique=True)
    username: Optional[str]
    hashed_password: str
    DOB: str = Optional[datetime]
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False