"""
Gmail integration for fetching tasks and labels
"""

import os
import pickle
from typing import List, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.api_python_client import discovery
import logging

logger = logging.getLogger(__name__)

# Gmail API scopes
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


class GmailIntegration:
    """Integration with Gmail API for task management"""

    def __init__(self):
        """Initialize Gmail integration"""
        self.credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")
        self.token_path = os.getenv("GOOGLE_TOKEN_PATH", "token.pickle")
        self.user_email = os.getenv("GMAIL_USER_EMAIL")
        self.task_label = os.getenv("GMAIL_TASK_LABEL", "Tarefas")
        self.service = None
        self._authenticate()

    def _authenticate(self) -> None:
        """Authenticate with Google APIs"""
        try:
            # Check if token already exists
            if os.path.exists(self.token_path):
                with open(self.token_path, "rb") as token_file:
                    creds = pickle.load(token_file)
            else:
                creds = None

            # If credentials expired, refresh them
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            elif not creds or not creds.valid:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save credentials for next run
            with open(self.token_path, "wb") as token_file:
                pickle.dump(creds, token_file)

            # Build the Gmail service
            self.service = discovery.build("gmail", "v1", credentials=creds)
            logger.info("Gmail authentication successful")

        except FileNotFoundError:
            logger.error(f"Credentials file not found: {self.credentials_path}")
            raise
        except Exception as e:
            logger.error(f"Gmail authentication failed: {e}")
            raise

    def get_labels(self) -> Dict[str, str]:
        """Get all Gmail labels"""
        try:
            results = self.service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])
            label_dict = {label["name"]: label["id"] for label in labels}
            logger.info(f"Found {len(labels)} labels")
            return label_dict
        except Exception as e:
            logger.error(f"Failed to get labels: {e}")
            return {}

    def get_task_label_id(self) -> str:
        """Get the ID of the task label"""
        try:
            labels = self.get_labels()
            label_id = labels.get(self.task_label)
            if not label_id:
                logger.warning(f"Label '{self.task_label}' not found")
                return None
            logger.info(f"Task label ID: {label_id}")
            return label_id
        except Exception as e:
            logger.error(f"Failed to get task label ID: {e}")
            return None

    def get_messages_by_label(self, label_id: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Get messages with a specific label"""
        try:
            query = f"label:{label_id}"
            results = (
                self.service.users()
                .messages()
                .list(userId="me", q=query, maxResults=max_results)
                .execute()
            )
            messages = results.get("messages", [])
            logger.info(f"Found {len(messages)} messages with label {label_id}")
            return messages
        except Exception as e:
            logger.error(f"Failed to get messages: {e}")
            return []

    def get_message_details(self, message_id: str) -> Dict[str, Any]:
        """Get full details of a message"""
        try:
            message = (
                self.service.users()
                .messages()
                .get(userId="me", id=message_id, format="full")
                .execute()
            )
            return message
        except Exception as e:
            logger.error(f"Failed to get message details: {e}")
            return {}

    def get_tasks(self, max_results: int = 10) -> List[Dict[str, Any]]:
        """Get all tasks from Gmail with task label"""
        try:
            label_id = self.get_task_label_id()
            if not label_id:
                logger.warning("Cannot retrieve tasks without label ID")
                return []

            messages = self.get_messages_by_label(label_id, max_results)
            tasks = []

            for message in messages:
                details = self.get_message_details(message["id"])
                if details:
                    task = self._parse_message_to_task(details)
                    tasks.append(task)

            logger.info(f"Retrieved {len(tasks)} tasks")
            return tasks

        except Exception as e:
            logger.error(f"Failed to get tasks: {e}")
            return []

    def _parse_message_to_task(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Parse Gmail message into task object"""
        try:
            headers = message.get("payload", {}).get("headers", [])
            subject = next(
                (h["value"] for h in headers if h["name"] == "Subject"), "No Subject"
            )
            from_addr = next(
                (h["value"] for h in headers if h["name"] == "From"), "Unknown"
            )
            date = next(
                (h["value"] for h in headers if h["name"] == "Date"), "Unknown"
            )

            task = {
                "id": message.get("id"),
                "subject": subject,
                "from": from_addr,
                "date": date,
                "snippet": message.get("snippet", ""),
            }
            return task

        except Exception as e:
            logger.error(f"Failed to parse message: {e}")
            return {}
