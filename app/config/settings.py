from pydantic import BaseSettings, Field

class DatabaseSettings(BaseSettings):
    user: str = Field(env='DB_USER')
    password: str = Field(env='DB_PASSWORD')
    server: str = Field(env='DB_SERVER')
    name: str = Field(env='DB_NAME')

class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
   