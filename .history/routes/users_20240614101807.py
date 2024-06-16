from fastapi import APIRouter
from models.user import User
from schemas.users import UserCreate, UserOut
from utils.security import Password

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: UserCreate):
    user.password = Password.create_hash_password(password=user.password)

    user = await User(email=user.email, username=user.username, hashed_password=user.password)
    
    