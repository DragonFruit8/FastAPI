from beanie import Docuemnt 


class User(Docuemnt):
    email: str
    hashed_password: str
    created_at: datetime