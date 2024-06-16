from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(None, max_length=50)
    password: Field(..., min_length=8)
    DOB: str = None
    