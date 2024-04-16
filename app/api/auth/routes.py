from fastapi import APIRouter, HTTPException

from app.core.schemas.auth import AuthSchema
from app.api.auth import auth


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/start")
def start(data: AuthSchema):
    try:
        auth.start_authentication(data)
        return {"status": "OK"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

@router.post("/refresh")
def refresh(data: AuthSchema):
    try:
        ret = auth.refresh_authentication(data)
        return ret
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
