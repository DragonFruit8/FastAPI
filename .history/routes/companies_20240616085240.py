from fastapi import APIRouter, Depends,HTTPException, status

from models.companies import Company
from models.users import User
from schemas.companies import CompanyCreate, CompanyOut
from schemas.users import UserOut
from utils.get_current_user import get_current_active_user, is_admin

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company(company: CompanyCreate, user: UserOut = Depends(get_current_active_user)):
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to create a company"
        )
    new_company = await Company.insert_one(Company(**company.dict()))
    return CompanyOut(**new_company.dict())