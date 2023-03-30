from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AidMap"
    GOOGLE_MAPS_API_KEY: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"
