from fastapi import APIRouter, HTTPException

from app.core.schemas.auth import AuthSchema
from app.api.license import license


router = APIRouter(
    prefix="/license",
    tags=["License"]
)


@router.post("")
def generate_new_license():
    try:
        key = license.generate_new_license()
        return {"license_key": str(key)}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
    
    
@router.get("")
def get_licenses(key: str = '', machine_id: str = ''):
    try:
        filter = {}
        if key:
            filter["license_key"] = key
        if machine_id:
            filter["machine_id"] = machine_id
        
        licenses = license.get_licences(filter)
        return licenses
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

