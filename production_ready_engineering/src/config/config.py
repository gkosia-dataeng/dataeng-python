from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    LOG_LEVEL: str
    DATA_PATH: str
    DLQ_PATH: str
    DB_PATH: str
    model_config = SettingsConfigDict(env_file= './src/config/.env')