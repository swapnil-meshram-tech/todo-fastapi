from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    APP_NAME: str = "todo"
    DATABASE_URL: str = "sqlite:///db/test.db"

    @field_validator("DATABASE_URL")
    @classmethod
    def validate_db_url(cls, v: str) -> str:
        if not v.startswith(("sqlite:///", "postgresql://", "mysql://")):
            raise ValueError(f"Invalid Database URL : {v}")

        return v


settings = Settings()
