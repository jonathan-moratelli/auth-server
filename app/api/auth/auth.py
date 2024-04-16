from app.core.schemas.auth import AuthSchema
from app.core.db.db import db_conn


def start_authentication(data: AuthSchema):
    
    erro = ""
    
    if not data.key:
        raise ValueError("A license key deve ser informada")
    
    if not data.machine_id:
        raise ValueError("machine_id inválido")
    
    cursor = db_conn.cursor()
    params = {"key": data.key}
    result = cursor.execute("SELECT machine_id FROM licenses WHERE license_key = :key", params)
    row = result.fetchone()
    if not row:
        erro = "A license key é inválida"
    
    if not erro:
        machine_id = row[0]
        if data.machine_id != machine_id:
            params["machine_id"] = data.machine_id
            result = cursor.execute("UPDATE licenses SET machine_id = :machine_id WHERE license_key = :key", params)
            db_conn.commit()
    
    cursor.close()
    
    if erro:
        raise ValueError(erro)


def refresh_authentication(data: AuthSchema):
    pass

