from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, HTTPException, Request
from starlette.config import Config
from starlette.responses import RedirectResponse

from ...database.models import User

config = Config(".env")
oauth = OAuth(config=config)
oauth.register(
    name="google",
    client_id="",
    client_secret="",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile",
    },
)

router = APIRouter()


@router.get("/login")
async def login(request: Request) -> None:
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("login_callback")
async def auth_callback(request: Request) -> None:
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")

    if not user_info:
        raise HTTPException(
            status_code=400, detail="Failed to fetch user information from Google"
        )
    
    email = user_info.get("email")

    return RedirectResponse(url="/main")

@router.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)

