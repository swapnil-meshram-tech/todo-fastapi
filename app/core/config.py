# from dotenv import load_dotenv
# import os

# load_dotenv()


# class Settings:
#     DATABASE_URL = os.getenv("DATABASE_URL")

# settings = Settings()


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str
    DATABASE_URL: str


settings = Settings()
