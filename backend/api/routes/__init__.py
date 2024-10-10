from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from ...utils.security import auth_required
from ...config import TEMPLATES


router = APIRouter()

@router.get("/")
@auth_required
async def index(request: Request):
    return {"ALL": "WORKS"}

@router.get("/me")
@auth_required
async def me(request: Request):
    return request.session['user_data']