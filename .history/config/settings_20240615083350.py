from pydantic_settings import BaseSettings
from 

class Settings(BaseSettings):
    MONGODB_URL: str 
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE: int 
    
class Config:
    env_file = ".env"
    
settings = Settings()    