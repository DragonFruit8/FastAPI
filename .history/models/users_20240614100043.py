from beanie import Docuemnt 
from date

class User(Docuemnt):
    email: str
    hashed_password: str
    created_at: datetime