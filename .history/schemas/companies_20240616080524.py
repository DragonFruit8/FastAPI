from pydantic import BaseModel, EmailStr, Field

class CompanyCreate(BaseModel):
    name: str
    address: str
    phone: str = Field(..., regex="^\d{3}-\d{3}-\d{4}$", max_length=18)
    email: EmailStr
    website: str