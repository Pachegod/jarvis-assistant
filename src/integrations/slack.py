"""
Slack integration for sending notifications
"""

import os
from typing import Dict, Any, List
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging

logger = logging.getLogger(__name__)


class SlackIntegration:
    """Integration with Slack API for notifications"""

    def __init__(self):
        """Initialize Slack integration"""
        self.bot_token = os.getenv("SLACK_BOT_TOKEN")
        self.channel = os.getenv("SLACK_CHANNEL")
        self.client = None
        self._authenticate()

    def _authenticate(self) -> None:
        """Authenticate with Slack API"""
        try:
            if not self.bot_token:
                logger.warning("Slack bot token not configured")
                return

            self.client = WebClient(token=self.bot_token)
            # Test connection
            self.client.auth_test()
            logger.info("Slack authentication successful")

        except SlackApiError as e:
            logger.error(f"Slack authentication failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during Slack authentication: {e}")

    def send_message(self, text: str, blocks: List[Dict[str, Any]] = None) -> bool:
        """Send a message to the configured Slack channel"""
        try:
            if not self.client:
                logger.error("Slack client not initialized")
                return False

            if not self.channel:
                logger.error("Slack channel not configured")
                return False

            kwargs = {"channel": self.channel}

            if blocks:
                kwargs["blocks"] = blocks
            else:
                kwargs["text"] = text

            response = self.client.chat_postMessage(**kwargs)
            logger.info(f"Message sent successfully: {response['ts']}")
            return True

        except SlackApiError as e:
            logger.error(f"Failed to send Slack message: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending message: {e}")
            return False

    def send_formatted_message(
        self, title: str, sections: Dict[str, List[str]]
    ) -> bool:
        """Send a formatted message with sections"""
        try:
            blocks = [
                {
                    "type": "header",
                    "text": {"type": "plain_text", "text": title, "emoji": True},
                }
            ]

            for section_title, items in sections.items():
                blocks.append(
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*{section_title}*\n" + "\n".join(items),
                        },
                    }
                )

            blocks.append({"type": "divider"})

            return self.send_message("", blocks=blocks)

        except Exception as e:
            logger.error(f"Failed to send formatted message: {e}")
            return False

    def send_task_summary(
        self,
        gmail_tasks: List[Dict[str, Any]],
        calendar_events: List[Dict[str, Any]],
        claude_code_summary: Dict[str, Any],
    ) -> bool:
        """Send a summary of tasks, calendar, and Claude Code"""
        try:
            sections = {}

            # Gmail Tasks Section
            if gmail_tasks:
                sections["Gmail Tasks"] = [
                    f"• {task.get('subject', 'No Subject')}"
                    for task in gmail_tasks[:5]
                ]
            else:
                sections["Gmail Tasks"] = ["No pending tasks"]

            # Calendar Events Section
            if calendar_events:
                sections["Today's Events"] = [
                    f"• {event.get('summary', 'No Title')} at {event.get('start', 'TBD')}"
                    for event in calendar_events[:5]
                ]
            else:
                sections["Today's Events"] = ["No events scheduled"]

            # Claude Code Section
            if claude_code_summary:
                claude_items = [
                    f"Active Sessions: {claude_code_summary.get('active_sessions', 0)}",
                    f"Open PRs: {claude_code_summary.get('open_prs', 0)}",
                    f"Recent Activities: {claude_code_summary.get('recent_activities', 0)}",
                ]
                sections["Claude Code"] = claude_items
            else:
                sections["Claude Code"] = ["No data available"]

            return self.send_formatted_message(
                ":jarvis: Jarvis Daily Assistant", sections
            )

        except Exception as e:
            logger.error(f"Failed to send task summary: {e}")
            return False

    def send_error_message(self, error: str) -> bool:
        """Send an error message to Slack"""
        try:
            blocks = [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":warning: Jarvis Assistant Error",
                        "emoji": True,
                    },
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"```{error}```"},
                },
            ]

            return self.send_message("", blocks=blocks)

        except Exception as e:
            logger.error(f"Failed to send error message: {e}")
            return False

    def update_message(
        self, channel: str, ts: str, text: str, blocks: List[Dict[str, Any]] = None
    ) -> bool:
        """Update an existing message"""
        try:
            if not self.client:
                logger.error("Slack client not initialized")
                return False

            kwargs = {"channel": channel, "ts": ts}

            if blocks:
                kwargs["blocks"] = blocks
            else:
                kwargs["text"] = text

            response = self.client.chat_update(**kwargs)
            logger.info(f"Message updated successfully: {response['ts']}")
            return True

        except SlackApiError as e:
            logger.error(f"Failed to update Slack message: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error updating message: {e}")
            return False
