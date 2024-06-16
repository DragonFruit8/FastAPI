from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str 
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE: int 
    
class Config:
    env_file = ".."
    
settings = Settings()    