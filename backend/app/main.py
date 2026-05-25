from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.upload import router as upload_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(upload_router)