import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from backend.api.routes.auth import router as auth_router

app = FastAPI()

SECRET_KEY = os.environ.get('SECRET_KEY') or None
if SECRET_KEY is None:
    raise 'Missing SECRET_KEY'

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (for testing)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
# app.mount('./frontend/static', StaticFiles(directory="./frontend/static"), name="static")

