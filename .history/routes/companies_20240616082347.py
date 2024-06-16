from fastapi import APIRouter, Depends, status
from models.companies import Company
from models.users import User
from sche
from schemas.companies import CompanyCreate, CompanyOut

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company( company: CompanyCreate):
    new_company = await Company.insert_one(company)
    return new_company