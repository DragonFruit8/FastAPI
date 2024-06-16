from beanie import Docuemnt 
from 

class User(Docuemnt):
    email: str
    hashed_password: str
    created_at: datetime