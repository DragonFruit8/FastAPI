from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.companies import Company
from models.users import User
from schemas.companies import CompanyCreate, CompanyOut
from schemas.users import UserOut
from utils.get_current_user import get_current_active_user, is_admin

router = APIRouter(prefix="/companies", tags=["Company"])


@router.post("/")
async def create_company(
    company: CompanyCreate, user: UserOut = Depends(get_current_active_user)
):
    if not await is_admin(user.email):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user"
        )
    company = await Company(**company.model_dump()).insert()
    json_encoded = jsonable_encoder(company)
    return JSONResponse(content=json_encoded, status_code=status.HTTP_201_CREATED)

@router.get("/")
async def get_companies(user: UserOut = Depends(get_current_active_user)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user"
        )
        