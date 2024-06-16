from fastapi import APIRouter, HTTPException, status
from models.user import User
from schemas.users import UserCreate, UserOut
from utils.security import Password

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: UserCreate):
    exist = await User.find_one(User.email == user.email)
    if exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    user.password = Password.create_hash_password(password=user.password)

    user = await User(email=user.email, username=user.username, hashed_password=user.password)
    return UserOut(email=user.email, created_at=user.created_at)