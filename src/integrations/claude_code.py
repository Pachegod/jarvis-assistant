"""
Claude Code integration for fetching tasks and sessions
"""

import os
import requests
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ClaudeCodeIntegration:
    """Integration with Claude Code API"""

    def __init__(self):
        """Initialize Claude Code integration"""
        self.api_key = os.getenv("CLAUDE_CODE_API_KEY")
        self.user_id = os.getenv("CLAUDE_CODE_USER_ID")
        self.session_id = os.getenv("CLAUDE_CODE_SESSION_ID")
        self.base_url = "https://api.claude.ai"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_active_sessions(self) -> List[Dict[str, Any]]:
        """Get all active Claude Code sessions"""
        try:
            if not self.api_key:
                logger.warning("Claude Code API key not configured")
                return []

            # Placeholder: Actual endpoint depends on Claude Code API
            endpoint = f"{self.base_url}/v1/sessions"
            response = requests.get(endpoint, headers=self.headers, timeout=10)
            response.raise_for_status()

            sessions = response.json().get("sessions", [])
            logger.info(f"Found {len(sessions)} active sessions")
            return sessions

        except requests.RequestException as e:
            logger.error(f"Failed to fetch active sessions: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching sessions: {e}")
            return []

    def get_session_tasks(self, session_id: str = None) -> List[Dict[str, Any]]:
        """Get tasks for a specific session"""
        try:
            if not self.api_key:
                logger.warning("Claude Code API key not configured")
                return []

            session_id = session_id or self.session_id
            if not session_id:
                logger.warning("Session ID not configured")
                return []

            # Placeholder: Actual endpoint depends on Claude Code API
            endpoint = f"{self.base_url}/v1/sessions/{session_id}/tasks"
            response = requests.get(endpoint, headers=self.headers, timeout=10)
            response.raise_for_status()

            tasks = response.json().get("tasks", [])
            logger.info(f"Found {len(tasks)} tasks in session {session_id}")
            return tasks

        except requests.RequestException as e:
            logger.error(f"Failed to fetch session tasks: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching tasks: {e}")
            return []

    def get_pull_requests(self) -> List[Dict[str, Any]]:
        """Get open pull requests from Claude Code"""
        try:
            if not self.api_key:
                logger.warning("Claude Code API key not configured")
                return []

            # Placeholder: Actual endpoint depends on Claude Code API
            endpoint = f"{self.base_url}/v1/pull-requests"
            response = requests.get(endpoint, headers=self.headers, timeout=10)
            response.raise_for_status()

            prs = response.json().get("pull_requests", [])
            logger.info(f"Found {len(prs)} open pull requests")
            return prs

        except requests.RequestException as e:
            logger.error(f"Failed to fetch pull requests: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching PRs: {e}")
            return []

    def get_recent_activity(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent Claude Code activity"""
        try:
            if not self.api_key:
                logger.warning("Claude Code API key not configured")
                return []

            # Placeholder: Actual endpoint depends on Claude Code API
            endpoint = f"{self.base_url}/v1/activity"
            params = {"limit": limit}
            response = requests.get(
                endpoint, headers=self.headers, params=params, timeout=10
            )
            response.raise_for_status()

            activity = response.json().get("activity", [])
            logger.info(f"Found {len(activity)} recent activities")
            return activity

        except requests.RequestException as e:
            logger.error(f"Failed to fetch recent activity: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching activity: {e}")
            return []

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of Claude Code activity"""
        try:
            sessions = self.get_active_sessions()
            prs = self.get_pull_requests()
            activity = self.get_recent_activity()

            summary = {
                "active_sessions": len(sessions),
                "open_prs": len(prs),
                "recent_activities": len(activity),
                "sessions": sessions[:5],  # Top 5 sessions
                "pull_requests": prs[:5],  # Top 5 PRs
            }

            return summary

        except Exception as e:
            logger.error(f"Failed to get Claude Code summary: {e}")
            return {}
