from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # GROQ_API_KEY: str
    # GROQ_MODEL: str
    VET_API_BASE_URL: str
    VET_API_TOKEN: str
    
    GEMINI_API_KEY: str
    GEMINI_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()