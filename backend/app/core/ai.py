"""
Claude AI integration core module.
Handles communication with the Claude API.
"""

from anthropic import Anthropic
from app.config import settings
from typing import Optional, List


class AICore:
    """Main AI interface using Claude API."""
    
    def __init__(self):
        """Initialize Claude client."""
        self.client = Anthropic(api_key=settings.claude_api_key)
        self.model = settings.claude_model
        self.conversation_history: List[dict] = []
    
    def chat(self, message: str, system_prompt: Optional[str] = None) -> str:
        """
        Send a message to Claude and get a response.
        
        Args:
            message: User message
            system_prompt: Optional custom system prompt
            
        Returns:
            Claude's response
        """
        # Implementation placeholder
        pass
    
    def reset_conversation(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_context(self) -> str:
        """Get current conversation context."""
        # Implementation placeholder
        pass


# Global instance
ai_core = AICore()
