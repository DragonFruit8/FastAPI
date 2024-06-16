from beanie import Document, Indexed

class Company(Document):
    name: str
    address: str
    phone: str
    email: str
    website: str

    @property
    def full_address(self):
        return f"{self.address}, {self.name}"

    class Meta:
        collection = "companies"
        indexes = [Indexed("name", unique=True)]