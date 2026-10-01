from functools import lru_cache
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )

    app_name: str = "todo"
    database_url: str

    @field_validator("database_url")
    @classmethod
    def validate_db_url(cls, v: str) -> str:
        if not v.startswith(("sqlite:///", "postgresql://", "mysql://")):
            raise ValueError(f"Invalid Database URL : {v}")

        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
