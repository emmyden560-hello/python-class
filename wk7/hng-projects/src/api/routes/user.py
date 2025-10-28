from fastapi import APIRouter, Depends
from datetime import datetime
from src.api.models.user import ProfileResponse
from src.api.services.cat_fact import fetch_cat_fact
from src.api.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=ProfileResponse)
async def get_profile(user: User = Depends(get_current_user)):
    cat_fact = await fetch_cat_fact()
    return ProfileResponse(
        status="success",
        user=user,
        timestamp=datetime.utcnow().isoformat + "Z",
        fact=cat_fact
    )
