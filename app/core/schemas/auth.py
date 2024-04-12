from pydantic import BaseModel

class AuthSchema(BaseModel):
    key: str
    machine_id: str
