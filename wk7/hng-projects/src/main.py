from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import FastAPI
from src.api.routes.user import router as user_router
from src.core.logging import setup_logging

app = FastAPI(
    title="User Profile API",
    description="API for fetching user profiles with random cat facts"
    version="1.0.0",
    docs_url="/docs"
    redoc_url="/redoc"
)

app.include_router(user_router)

setup_logging()


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"status": "error", "detail": exc.errors()}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "detail": "Internal server error"}
    )
