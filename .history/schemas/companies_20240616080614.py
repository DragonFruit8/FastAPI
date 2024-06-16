from pydantic import BaseModel, EmailStr, Field

class CompanyCreate(BaseModel):
    name: str
    address: str
    email: EmailStr
    phone: str = Field(..., regex="^\d{3}-\d{3}-\d{4}$", max_length=18)
    website: str
    
    class CompanyOut(BaseModel):
        name: str
        address: str
        email: EmailStr
        phone: str
        website: str
        created_at: datetime

        class Config:
            orm_mode = True