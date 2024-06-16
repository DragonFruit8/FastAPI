from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str 
    SECRET_KEY: str
    ACCESS
    
class Config:
    env_file = ".env"
    
settings = Settings()    