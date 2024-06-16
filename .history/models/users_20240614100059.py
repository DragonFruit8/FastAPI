from beanie import Docuemnt 
from datetime import datetime
from pydantic import Field


class User(Docuemnt):
    email: str
    hashed_password: str
    created_at: datetime