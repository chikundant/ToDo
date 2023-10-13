from typing import Literal, Optional

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    ENV: Literal["local", "dev", "main"] = "local"
    DEBUG: bool = True
    SERVICE_NAME: str = "to-do-app"

    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = "./system_configs/.env"


settings = AppSettings()
