from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(".env"))

class Settings(BaseSettings):
    MONGODB_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE: int 
    ALGORITHM: str
    
class Config:
    env_file = ".env"
    
settings = Settings()