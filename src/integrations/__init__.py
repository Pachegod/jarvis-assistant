"""
Integrations module for Jarvis Assistant
"""

from .gmail import GmailIntegration
from .calendar import CalendarIntegration
from .claude_code import ClaudeCodeIntegration
from .slack import SlackIntegration

__all__ = [
    "GmailIntegration",
    "CalendarIntegration",
    "ClaudeCodeIntegration",
    "SlackIntegration",
]
