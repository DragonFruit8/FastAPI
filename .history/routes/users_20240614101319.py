from fastapi import APIRouter
from models.user import User
from schemas.users import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: UserCreate):
    user = User(email=user.email, hashed_password=user.password)