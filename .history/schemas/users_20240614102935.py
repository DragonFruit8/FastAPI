from pydantic import BaseModel, EmailStr, Field

# Create a new User
class UserCreate(BaseModel):
    email: str = EmailStr
    password: str = Field(..., min_length=8)
    
class UserOut(BaseModel):
    email: str = EmailStr
    created_at: str
    
