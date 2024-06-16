from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field


class Company(Document):
    name: Indexed(str)
    address: str
    phone: str
    email: str
    website: str
    created_at: datetime = datetime.now()

    @property
    def full_address(self):
        return f"{self.address}, {self.name}"

    class Meta:
        collection = "companies"
        indexes = [Indexed("name", unique=True)]