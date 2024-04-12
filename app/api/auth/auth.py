from fastapi import APIRouter

from app.core.schemas.auth import AuthSchema


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/start")
async def start(data: AuthSchema):
    return data

@router.post("/refresh")
async def refresh(data: AuthSchema):
    return data
