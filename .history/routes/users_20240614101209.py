from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/signup')
async def signup(user: a):
    return {"msg": "signup"}