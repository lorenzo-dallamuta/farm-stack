from pydantic import BaseSettings

import os
from dotenv import load_dotenv

load_dotenv()
DEBUG_MODE = os.getenv('DEBUG_MODE')
DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')
DB_NAME = os.getenv('DB_NAME')
REALM_APP_ID = os.getenv('REALM_APP_ID')


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    REALM_APP_ID: str
    DB_URL: str
    DB_NAME: str


class AuthSettings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SECURE_COOKIE: bool = False


class Settings(CommonSettings, ServerSettings, DatabaseSettings, AuthSettings):
    pass


settings = Settings()
