from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.users import User
from schemas.users import UserCreate, UserOut
from utils.security import Password



router = APIRouter(
            prefix="/users", 
            tags=["Users"]
            )

@router.post('/signup')
async def signup(user: UserCreate):
    exist = await User.find_one(
            User.email == user.email
            )
    if exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already exists"
            )
    user.password = Password.get_password_hash( )

    user = await User(
            email=user.email, 
            created_at=user.created_at
            ).insert()
    
    return JSONResponse(content=UserOut(email=user.email, created_at=user.created_at).model_dump(), status_code=status.HTTP_201_CREATED)

    return UserOut(email=user.email, created_at=user.created_at)