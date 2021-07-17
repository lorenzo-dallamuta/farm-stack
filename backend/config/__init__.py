from pydantic import BaseSettings

import os
from dotenv import load_dotenv

load_dotenv()
DEBUG_MODE = os.getenv('DEBUG_MODE')
DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
