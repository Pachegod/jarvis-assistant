"""
Main script for Jarvis Assistant
Orchestrates all integrations and sends daily summary to Slack
"""

import os
import sys
import logging
from typing import Dict, Any, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

from .integrations import (
    GmailIntegration,
    CalendarIntegration,
    ClaudeCodeIntegration,
    SlackIntegration,
)


def main():
    """Main entry point for Jarvis Assistant"""
    try:
        logger.info("Starting Jarvis Assistant...")

        # Initialize integrations
        logger.info("Initializing integrations...")
        gmail = None
        calendar = None
        claude_code = ClaudeCodeIntegration()
        slack = SlackIntegration()

        # Try to initialize Gmail
        try:
            gmail = GmailIntegration()
        except Exception as e:
            logger.warning(f"Gmail initialization failed: {e}")

        # Try to initialize Calendar
        try:
            calendar = CalendarIntegration()
        except Exception as e:
            logger.warning(f"Calendar initialization failed: {e}")

        # Collect data
        logger.info("Collecting data from all sources...")
        gmail_tasks = []
        calendar_events = []
        claude_code_summary = {}

        if gmail:
            try:
                gmail_tasks = gmail.get_tasks(max_results=10)
                logger.info(f"Retrieved {len(gmail_tasks)} Gmail tasks")
            except Exception as e:
                logger.error(f"Failed to retrieve Gmail tasks: {e}")

        if calendar:
            try:
                calendar_events = calendar.get_today_events()
                logger.info(f"Retrieved {len(calendar_events)} calendar events")
            except Exception as e:
                logger.error(f"Failed to retrieve calendar events: {e}")

        try:
            claude_code_summary = claude_code.get_summary()
            logger.info("Retrieved Claude Code summary")
        except Exception as e:
            logger.error(f"Failed to retrieve Claude Code summary: {e}")

        # Send to Slack
        logger.info("Sending summary to Slack...")
        if slack.client:
            success = slack.send_task_summary(
                gmail_tasks, calendar_events, claude_code_summary
            )
            if success:
                logger.info("Summary sent successfully to Slack")
            else:
                logger.error("Failed to send summary to Slack")
        else:
            logger.warning("Slack client not initialized, skipping notification")

        logger.info("Jarvis Assistant completed successfully")
        return True

    except Exception as e:
        logger.error(f"Jarvis Assistant failed: {e}", exc_info=True)

        # Try to send error to Slack
        try:
            slack = SlackIntegration()
            if slack.client:
                slack.send_error_message(str(e))
        except Exception as slack_error:
            logger.error(f"Failed to send error notification to Slack: {slack_error}")

        return False


def validate_environment():
    """Validate that required environment variables are set"""
    required_vars = [
        "SLACK_BOT_TOKEN",
        "SLACK_CHANNEL",
    ]

    optional_vars = [
        "GOOGLE_CREDENTIALS_PATH",
        "GMAIL_USER_EMAIL",
        "CALENDAR_ID",
        "CLAUDE_CODE_API_KEY",
    ]

    missing_required = []
    for var in required_vars:
        if not os.getenv(var):
            missing_required.append(var)

    if missing_required:
        logger.error(f"Missing required environment variables: {', '.join(missing_required)}")
        logger.info("Please check your .env file")
        return False

    logger.info("Environment validation passed")
    return True


if __name__ == "__main__":
    if not validate_environment():
        sys.exit(1)

    success = main()
    sys.exit(0 if success else 1)
