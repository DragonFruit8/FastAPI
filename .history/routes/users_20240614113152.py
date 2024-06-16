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
    # Hash password
    user.password = Password.get_password_hash(user.password)
    # Save user
    new_user = User(**user.dict())
a   wait User.insert_one(new_user)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"msg": "User created successfully"}
            )    