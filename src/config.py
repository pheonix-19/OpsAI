"""
Configuration management for OpsAI.
Handles environment variables and secrets loading safely.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/opsai.db")
    
    # AI/ML APIs
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    HUGGINGFACE_API_TOKEN: Optional[str] = os.getenv("HUGGINGFACE_API_TOKEN")
    
    # JIRA Integration
    JIRA_URL: Optional[str] = os.getenv("JIRA_URL")
    JIRA_USER: Optional[str] = os.getenv("JIRA_USER")
    JIRA_API_TOKEN: Optional[str] = os.getenv("JIRA_API_TOKEN")
    JIRA_WEBHOOK_SECRET: Optional[str] = os.getenv("JIRA_WEBHOOK_SECRET")
    
    # Slack Integration
    SLACK_BOT_TOKEN: Optional[str] = os.getenv("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN: Optional[str] = os.getenv("SLACK_APP_TOKEN")
    YOUR_BOT_USER_ID: Optional[str] = os.getenv("YOUR_BOT_USER_ID")
    
    # Freshdesk Integration
    FRESHDESK_DOMAIN: Optional[str] = os.getenv("FRESHDESK_DOMAIN")
    FRESHDESK_API_KEY: Optional[str] = os.getenv("FRESHDESK_API_KEY")
    
    # Application Configuration
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
    MODEL_PATH: str = os.getenv("MODEL_PATH", "./models/lora_adapter")
    
    @classmethod
    def validate_required_secrets(cls) -> list[str]:
        """Validate that required secrets are present."""
        missing = []
        
        # Check for required API keys based on enabled features
        if not cls.OPENAI_API_KEY:
            missing.append("OPENAI_API_KEY")
            
        if not cls.HUGGINGFACE_API_TOKEN:
            missing.append("HUGGINGFACE_API_TOKEN")
            
        # Only require integration secrets if the integration is configured
        if cls.JIRA_URL and not cls.JIRA_API_TOKEN:
            missing.append("JIRA_API_TOKEN")
            
        if cls.SLACK_BOT_TOKEN and not cls.SLACK_APP_TOKEN:
            missing.append("SLACK_APP_TOKEN")
            
        if cls.FRESHDESK_DOMAIN and not cls.FRESHDESK_API_KEY:
            missing.append("FRESHDESK_API_KEY")
            
        return missing
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production environment."""
        return os.getenv("ENVIRONMENT", "development").lower() == "production"
    
    @classmethod
    def get_secret(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Safely get a secret from environment variables.
        
        Args:
            key: Environment variable name
            default: Default value if not found
            
        Returns:
            Secret value or default
        """
        value = os.getenv(key, default)
        if value and cls.DEBUG:
            # In debug mode, show only first/last 4 characters
            masked = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            print(f"🔐 Loaded secret {key}: {masked}")
        return value


# Create a global config instance
config = Config()

# Validate configuration on import
missing_secrets = config.validate_required_secrets()
if missing_secrets and config.is_production():
    raise EnvironmentError(
        f"Missing required environment variables in production: {', '.join(missing_secrets)}"
    )
elif missing_secrets and config.DEBUG:
    print(f"⚠️  Missing optional environment variables: {', '.join(missing_secrets)}")
