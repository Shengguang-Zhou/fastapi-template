from pydantic_settings import BaseSettings
import os
from safety.safety import safety_config


class Settings(BaseSettings):
    NAME: str = "YOUR APP NAME"
    ENV: str = "DEVELOPMENT"
    DEBUG: bool = False if ENV == 'PRODUCTION' else True

    BASE_PATH: str = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

    SERVER_HOST: str = safety_config.get('deployment', 'host')
    SERVER_PORT: int = safety_config.get('deployment', 'port')

    URL: str = safety_config.get('deployment', 'url')
    TIME_ZONE: str = "RPC"


    class Config:
        env_prefix = 'APP_'
        env_file = ".env"
        env_file_encoding = 'utf-8'



settings = Settings()