from fastapi import APIRouter, Depends, status
from models.companies import Company
from models.users import User
from schemas.users import UserOut
from schemas.companies import CompanyCreate, CompanyOut

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company( company: CompanyCreate, user: UserOut = Depends(get_current_active_user)):
    new_company = await Company.insert_one(company)
    return new_company