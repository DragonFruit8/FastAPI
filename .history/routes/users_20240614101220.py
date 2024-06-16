from fastapi import APIRouter
from models.user import User


router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: a):
    return {"msg": "signup"}