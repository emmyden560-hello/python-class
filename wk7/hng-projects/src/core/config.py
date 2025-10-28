from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    cat_fact_api_url: str
    environment: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
