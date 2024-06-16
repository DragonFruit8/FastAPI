from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field, EmailStr, GetCoreSchemaHandler, TypeAdapter
from pydantic_core import CoreSchema, core_schema


class User(Document):
    email: EmailStr
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema(cls, source_type, handler(EmailStr), handler(str), handler(datetime), handler(bool))
    
ta = TypeAdapter(User)
res     
    
    