from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_CONNECTION: str
    JWT_SECRET: str
    ALGORITHM: str
    JWT_TOKEN_EXPIPRY_DURATION: int 


settings = Settings()
