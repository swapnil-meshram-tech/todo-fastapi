from functools import lru_cache
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )

    database_url: str

    app_name: str = "todo"
    debug: bool = False

    log_level: str = "INFO"
    json_logs: bool = False

    @field_validator("database_url")
    @classmethod
    def validate_db_url(cls, v: str) -> str:
        if not v.startswith(("sqlite:///", "postgresql+asyncpg://", "mysql://")):
            raise ValueError("Invalid Database URL scheme")
            # raise ValueError(f"Invalid Database URL: {v}")
        return v

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        v = v.upper()
        if v not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            raise ValueError(f"Invalid log level: {v}")
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
