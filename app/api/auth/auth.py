from app.core.schemas.auth import AuthSchema
from app.core.db.db import db_conn


def start_authentication(data: AuthSchema):
    cursor = db_conn.cursor()
    params = {"key": data.key}
    result = cursor.execute("SELECT * FROM licenses WHERE license_key = :key", params)
    row = result.fetchone()
    cursor.close()
    
    # if not row:
    #     return None
    
    return row


def refresh_authentication(data: AuthSchema):
    pass

