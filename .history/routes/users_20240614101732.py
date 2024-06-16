from fastapi import APIRouter
from models.user import User
from schemas.users import UserCreate, UserOut
from utils.security import Password

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: UserCreate):
    user.password = User(email=user.email, hashed_password=Password.create_hash_password(password=user.password))
    await user.commit()