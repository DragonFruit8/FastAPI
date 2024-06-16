from pydantic import BaseModel, EmailStr, Field

class CompanyCreate(BaseModel):
    name: str
    address: str
    email: EmailStr
    phone: str = Field(..., regex="^\d{3}-\d{3}-\d{4}$", max_length=18)
    website: str