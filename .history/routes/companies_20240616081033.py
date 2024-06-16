from router import APIRouter, Depends, status

router = APIRouter( prefix="/companies", tags=["Company"])

@router.post("/")
async def