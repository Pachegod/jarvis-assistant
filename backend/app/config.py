"""
Configuration module for Jarvis Assistant backend.
Handles environment variables and application settings.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # Database
    database_url: str = "postgresql://jarvis:jarvis_password@localhost:5432/jarvis_db"
    
    # API
    api_title: str = "Jarvis Assistant API"
    api_version: str = "1.0.0"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # Claude AI
    claude_api_key: str = ""
    claude_model: str = "claude-3-5-sonnet-20241022"
    
    # Google Services
    google_api_key: Optional[str] = None
    google_service_account_json: Optional[str] = None
    
    # Voice Settings
    enable_tts: bool = True
    enable_stt: bool = True
    
    # Security
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
