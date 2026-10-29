"""
Logging configuration for the application.
"""

import logging
from app.config import settings


def setup_logger(name: str) -> logging.Logger:
    """Set up a logger with the configured level."""
    logger = logging.getLogger(name)
    logger.setLevel(settings.log_level)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


logger = setup_logger(__name__)
