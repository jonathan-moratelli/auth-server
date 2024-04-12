from fastapi import FastAPI

from app.api.auth import auth

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

