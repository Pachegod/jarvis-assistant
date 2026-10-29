"""
API routes for FastAPI application.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from . import schemas


router = APIRouter(prefix="/api", tags=["chat"])


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@router.post("/chat", response_model=schemas.ChatMessageResponse)
async def send_message(
    message: schemas.ChatMessageRequest,
    db: Session = Depends(get_db)
):
    """Send a chat message and get response."""
    # Implementation placeholder
    pass


@router.get("/conversations")
async def get_conversations(db: Session = Depends(get_db)):
    """Get user's conversations."""
    # Implementation placeholder
    pass


@router.post("/conversations", response_model=schemas.ConversationResponse)
async def create_conversation(
    conversation: schemas.ConversationRequest,
    db: Session = Depends(get_db)
):
    """Create a new conversation."""
    # Implementation placeholder
    pass
