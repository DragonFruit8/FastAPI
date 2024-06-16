from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# Create a new User
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    
class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    
