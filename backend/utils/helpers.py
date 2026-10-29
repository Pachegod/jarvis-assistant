"""
Helper functions for common tasks.
"""

from datetime import datetime
from typing import Any, Dict


def serialize_datetime(dt: datetime) -> str:
    """Convert datetime to ISO format string."""
    if dt:
        return dt.isoformat()
    return None


def parse_datetime(date_string: str) -> datetime:
    """Parse ISO format string to datetime."""
    return datetime.fromisoformat(date_string)


def dict_to_readable(data: Dict[str, Any]) -> str:
    """Convert dictionary to readable string."""
    # Implementation placeholder
    pass
