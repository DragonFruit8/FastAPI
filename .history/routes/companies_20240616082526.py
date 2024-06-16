from fastapi import APIRouter, Depends, status
from utils.get_current_user import get_current_active_user
from models.companies import Company
from schemas.companies import CompanyCreate, CompanyOut
from models.users import User
from schemas.users import UserOut

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company( company: CompanyCreate, user: UserOut = Depends(get_current_active_user)):
    new_company = await Company.insert_one(company)
    return new_company