from datetime import datetime

from beanie import Document, Indexed
from pydantic import Field, EmailStr


class User(Document):
    email: EmailStr = Field(..., index=Indexed(unique=True))
    hashed_password: str
    created_at: Field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_superuser: bool = False
#     @classmethod
#     def __get_pydantic_core_schema__(
#         cls, source_type: any, handler: GetCoreSchemaHandler
#     ) -> CoreSchema:
#         return core_schema(cls, source_type, handler(EmailStr), handler(str), handler(datetime), handler(bool))
    
# ta = TypeAdapter(User)
# res = ta.validate_python({"email": " ", "hashed_password": " ", "created_at": " ", "is_active": " ", "is_superuser": " "})
# assert isinstance(res, User)
# assert res == User(email=" ", hashed_password=" ", created_at=" ", is_active=" ", is_superuser=" ")    
    
    