from fastapi import Request
from functools import wraps
from fastapi.responses import RedirectResponse
import time
from backend.database.models import User
from backend.database.operations import get_user, update_user

def auth_required(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.session.get("access_token")
        token_expire_date = request.session.get("token_expire_date")

        if not token or time.time() > token_expire_date:
            return RedirectResponse("/auth")
        
        return await func(request, *args, **kwargs)
    return wrapper

async def validate_user(user_info: dict[str: str]) -> User | None:
    if user_info["email_verified"]:
        user_from_db = await get_user(email=user_info["email"])
        if user_from_db:
            update_user(user=User(_id=user_from_db.id, email=user_from_db.email, name=user_info["given_name"], photo=user_info["picture"]))
            return user_from_db
    else:
        return None
