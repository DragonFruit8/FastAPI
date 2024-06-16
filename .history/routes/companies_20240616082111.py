from fastapi import APIRouter, Depends, status
from models.companies import Company
from sche

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company(company: CompanyCreate):
    pass