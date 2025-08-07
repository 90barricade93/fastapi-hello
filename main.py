"""
FastAPI application for Sharif's API.

This module provides endpoints for greeting and message exchange functionality.
"""

import logging
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
TIMEZONE_OFFSET = 2  # UTC+2 (Nederland zomertijd)

app = FastAPI(
    title="Demo for Sharif API",
    description="A simple API for message exchange with Sharif",
    version="1.0.0",
    openapi_url=f"/openapi.json"
)

# Models
class Message(BaseModel):
    """Base message model for API responses."""
    message: str = Field(..., description="The message content")

class SharifReply(BaseModel):
    """Model for message replies from Sharif."""
    message: str = Field(..., description="The message content")
    sent_by: str = Field(
        default="Sharif",
        description="Name of the message sender"
    )
    received_at: Optional[str] = Field(
        default=None,
        description="Timestamp when the message was received (ISO 8601 format)"
    )

class APIResponse(BaseModel):
    """Standard API response model."""
    status: str = Field(..., description="Status of the operation")
    data: dict = Field(..., description="Response data")

# Helper functions
def get_current_time() -> str:
    """Get current time in the configured timezone."""
    return datetime.now(timezone(timedelta(hours=TIMEZONE_OFFSET))).isoformat()

# Endpoints
@app.get("/", include_in_schema=False)
async def root() -> Message:
    """Root endpoint with welcome message."""
    return Message(
        message="Welkom bij de API van Raymond voor Sharif! 🎉 Gebruik /hello of POST naar /talk"
    )

@app.get("/hello", response_model=Message)
async def hello() -> Message:
    """
    Greet the user with a friendly message and current time.
    
    Returns:
        Message: A greeting message with the current timestamp
    """
    current_time = get_current_time()
    logger.info(f"Sending greeting at {current_time}")
    
    return Message(
        message=(
            "Hallo Sharif! 👋 Deze begroeting komt realtime uit Raymond's eigen "
            f"FastAPI-backend, op {current_time} verzonden 🚀"
        )
    )

@app.post(
    "/talk",
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED
)
async def talk(reply: SharifReply) -> APIResponse:
    """
    Process a message from Sharif.
    
    Args:
        reply: The message from Sharif
        
    Returns:
        APIResponse: Status and processed message data
    """
    try:
        # Set received_at if not provided
        if not reply.received_at:
            reply.received_at = get_current_time()
            
        logger.info(f"Received message from {reply.sent_by}: {reply.message}")
        
        return APIResponse(
            status="success",
            data={
                "reply": reply.dict(),
                "note": "Bedankt voor je bericht! 👊"
            }
        )
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Er is een fout opgetreden bij het verwerken van je bericht."
        )

# Add health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict:
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "timestamp": get_current_time()}