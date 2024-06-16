from pydantic import BaseModel, EmailStr, Field

# Create a new User
class UserCreate(BaseModel):
    email: EmailStr
    password: Field(..., min_length=8)
    DOB: str = None
    
class UserOut(BaseModel):
    email: EmailStr
    created_at: str
    
