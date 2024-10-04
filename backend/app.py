from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from backend.api.routes.auth import router as auth_router
import os

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

app.include_router(auth_router, prefix="/auth", tags=["auth"])