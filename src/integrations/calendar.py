"""
Google Calendar integration for fetching events
"""

import os
import pickle
from datetime import datetime, timedelta
from typing import List, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.api_python_client import discovery
import logging

logger = logging.getLogger(__name__)

# Calendar API scopes
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


class CalendarIntegration:
    """Integration with Google Calendar API"""

    def __init__(self):
        """Initialize Calendar integration"""
        self.credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")
        self.token_path = os.getenv("GOOGLE_TOKEN_PATH", "token.pickle")
        self.calendar_id = os.getenv("CALENDAR_ID", "primary")
        self.service = None
        self._authenticate()

    def _authenticate(self) -> None:
        """Authenticate with Google Calendar API"""
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

            # Build the Calendar service
            self.service = discovery.build("calendar", "v3", credentials=creds)
            logger.info("Calendar authentication successful")

        except FileNotFoundError:
            logger.error(f"Credentials file not found: {self.credentials_path}")
            raise
        except Exception as e:
            logger.error(f"Calendar authentication failed: {e}")
            raise

    def get_today_events(self) -> List[Dict[str, Any]]:
        """Get all events for today"""
        try:
            now = datetime.utcnow()
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            today_end = today_start + timedelta(days=1)

            return self._get_events_between(
                today_start.isoformat() + "Z",
                today_end.isoformat() + "Z",
                max_results=20,
            )

        except Exception as e:
            logger.error(f"Failed to get today's events: {e}")
            return []

    def get_upcoming_events(self, days: int = 7) -> List[Dict[str, Any]]:
        """Get all events for the next N days"""
        try:
            now = datetime.utcnow()
            start = now.isoformat() + "Z"
            end = (now + timedelta(days=days)).isoformat() + "Z"

            return self._get_events_between(start, end, max_results=20)

        except Exception as e:
            logger.error(f"Failed to get upcoming events: {e}")
            return []

    def _get_events_between(
        self, start_time: str, end_time: str, max_results: int = 20
    ) -> List[Dict[str, Any]]:
        """Get events between two times"""
        try:
            events_result = (
                self.service.events()
                .list(
                    calendarId=self.calendar_id,
                    timeMin=start_time,
                    timeMax=end_time,
                    maxResults=max_results,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )

            events = events_result.get("items", [])
            logger.info(f"Found {len(events)} events")

            return [self._parse_event(event) for event in events]

        except Exception as e:
            logger.error(f"Failed to get events: {e}")
            return []

    def _parse_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Parse calendar event into simplified format"""
        try:
            start = event.get("start", {})
            start_time = start.get("dateTime") or start.get("date")

            parsed_event = {
                "id": event.get("id"),
                "summary": event.get("summary", "No Title"),
                "start": start_time,
                "end": event.get("end", {}).get("dateTime")
                or event.get("end", {}).get("date"),
                "description": event.get("description", ""),
                "location": event.get("location", ""),
                "status": event.get("status", "unknown"),
            }
            return parsed_event

        except Exception as e:
            logger.error(f"Failed to parse event: {e}")
            return {}
