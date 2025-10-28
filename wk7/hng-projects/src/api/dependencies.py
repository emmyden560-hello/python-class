from fastapi import Security, HTTPException
from fastapi import Depends, HTTPException, status
from src.api.models.user import User
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Security(oauth2_scheme)) -> User:
    # Verify JWT token and fetch user (simplified)
    try:
        # Add JWT decoding logic here
        return User(
            email="emmanueldenis560@gmail.com",
            name="Emmanuel Denis",
            stack="Python/FastAPI"
        )
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
