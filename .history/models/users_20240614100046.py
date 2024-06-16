from beanie import Docuemnt 
from datetime import datetime


class User(Docuemnt):
    email: str
    hashed_password: str
    created_at: datetime