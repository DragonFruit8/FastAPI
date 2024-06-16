from fastapi import APIRouter, Depends, status

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def create_company(company):
    pass