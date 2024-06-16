from datetime import datetime

from beanie import Document, Indexed
from pydantic import EmailStr, Field


class Company(Document):
    name: Indexed(str)
    address: str
    phone: str = Field(...)
    email: EmailStr
    website: str
    created_at: datetime = datetime.now()

    @property
    def full_address(self):
        return f"{self.address}, {self.name}"

    class Meta:
        collection = "companies"
        indexes = [Indexed("name", unique=True)]