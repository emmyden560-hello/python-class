import httpx
from fastapi import HTTPException
from src.core.config import settings 

async def fetch_cat_fact() -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.cat_fact_api_url, timeout=5.0)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=503, detail=f"Failed to fetch cat fact: {str(e)}")
