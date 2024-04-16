from fastapi import FastAPI

from app.core.db.db import init_db
from app.api.auth.routes import router as auth_router
from app.api.license.routes import router as license_router


init_db()

app = FastAPI()

app.include_router(auth_router)
app.include_router(license_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


