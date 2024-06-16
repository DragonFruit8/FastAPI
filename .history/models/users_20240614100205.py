from beanie import Docuemnt 
from datetime import datetime
from pydantic import Field, Optional


class User(Docuemnt):
    email: str
    username: str
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False