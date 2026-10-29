"""
Main FastAPI application for Jarvis Assistant.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from api import routes
from scheduler.tasks import start_scheduler, stop_scheduler
from utils.logger import logger

# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(routes.router)


@app.on_event("startup")
async def startup():
    """Run startup tasks."""
    logger.info("Starting Jarvis Assistant API")
    start_scheduler()


@app.on_event("shutdown")
async def shutdown():
    """Run shutdown tasks."""
    logger.info("Shutting down Jarvis Assistant API")
    stop_scheduler()


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Jarvis Assistant API",
        "version": settings.api_version,
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port
    )
