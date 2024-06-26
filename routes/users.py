from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from models.users import User
from schemas.users import UserCreate, UserOut
from utils.get_current_user import get_current_active_user
from utils.security import Password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup")
async def signup(user: UserCreate):
    exist = await User.find_one(User.email == user.email)
    if exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )
    # Hash password
    hashed_password = Password.hash_password(user.password)
    # Save user
    new_user = User(**user.dict(), hashed_password=hashed_password)
    await User.insert_one(new_user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED , content={"msg": "User created successfully", "email": new_user.email, "created_at": new_user.created_at.isoformat()}
    )
    
@router.post("/access-token")
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )    
    token = create_access_token(subject=user.email)

    return {"access_token": token, "type": "bearer"}

@router.get("/me")
async def dashboard(user: UserOut = Depends(get_current_active_user)):
    return user   
