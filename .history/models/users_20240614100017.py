from beanie import Docuemnt 

class User(Docuemnt):
    name: str
    email: str
    password: str

    class Collection:
        name = "users"