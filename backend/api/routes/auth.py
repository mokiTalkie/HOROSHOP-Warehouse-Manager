import os

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Request
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse
from ...config import TEMPLATES

from backend.utils.security import validate_user

from dotenv import load_dotenv

load_dotenv()

# OAuth settings
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID") or None
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET") or None
if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
    raise BaseException("Missing env variables")

# Set up oauth
config_data = {
    "GOOGLE_CLIENT_ID": GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET": GOOGLE_CLIENT_SECRET,
}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return TEMPLATES.TemplateResponse(request=request, name="login.html")


@router.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.route("/auth")
async def auth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url="/auth")
    
    user_info = access_token.get("userinfo")
    if await validate_user(user_info=user_info):
        print("User found!")



    request.session["user"] = 1
    return RedirectResponse(url="/auth")
