"""
Pydantic request/response schemas for API endpoints.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatMessageRequest(BaseModel):
    """Chat message request schema."""
    content: str
    conversation_id: Optional[int] = None


class ChatMessageResponse(BaseModel):
    """Chat message response schema."""
    id: int
    role: str
    content: str
    created_at: datetime


class ConversationRequest(BaseModel):
    """Conversation creation request."""
    title: str


class ConversationResponse(BaseModel):
    """Conversation response."""
    id: int
    title: str
    created_at: datetime
