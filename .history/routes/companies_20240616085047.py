from fastapi import APIRouter, Depends, status

from models.companies import Company
from models.users import User
from schemas.companies import CompanyCreate, CompanyOut
from schemas.users import UserOut
from utils.get_current_user import get_admin, get_current_active_user

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company( company: CompanyCreate, user: UserOut = Depends(get_current_active_user)):
    
    return new_company