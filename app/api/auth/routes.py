from fastapi import APIRouter, HTTPException

from app.core.schemas.auth import AuthSchema
from app.api.auth.auth import start_authentication, refresh_authentication


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/start")
def start(data: AuthSchema):
    try:
        ret = start_authentication(data)
        return ret
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

@router.post("/refresh")
def refresh(data: AuthSchema):
    try:
        ret = refresh_authentication(data)
        return ret
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
