# Jarvis Assistant - Architecture

## System Overview

Jarvis Assistant is a multi-platform AI assistant with the following key components:

- **Backend**: FastAPI REST API with WebSocket support
- **Frontend**: React web application
- **Mobile**: React Native application
- **CLI**: Command-line interface
- **Database**: PostgreSQL for data persistence

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                   Jarvis Assistant                   │
├─────────────────────────────────────────────────────┤
│  Web (React)  │  Mobile (RN)  │  CLI (Python)      │
├─────────────────────────────────────────────────────┤
│            REST API + WebSocket (FastAPI)            │
├─────────────────────────────────────────────────────┤
│  Claude AI  │  Google Cloud  │  Integrations      │
│  (LLM)      │  (Voice, STT)  │  (Gmail, Slack)    │
├─────────────────────────────────────────────────────┤
│  PostgreSQL Database & File Storage                 │
└─────────────────────────────────────────────────────┘
```

## Backend Architecture

### Core Modules

1. **app/core/**: Core functionality
   - `ai.py`: Claude AI integration
   - `memory.py`: Conversation memory and context
   - `preferences.py`: User preferences
   - `security.py`: Credential management

2. **voice/**: Voice handling
   - `stt.py`: Speech-to-Text (Google Cloud)
   - `tts.py`: Text-to-Speech (Google Cloud)
   - `audio_processor.py`: Audio processing utilities

3. **integrations/**: External service integrations
   - `gmail.py`: Gmail integration
   - `calendar.py`: Google Calendar
   - `slack.py`: Slack integration
   - `notion.py`: Notion integration
   - `todoist.py`: Todoist integration
   - `home_assistant.py`: Smart home control
   - `web_search.py`: Web search

4. **database/**: Data persistence
   - `models.py`: SQLAlchemy ORM models
   - `database.py`: Database connection
   - `crud.py`: CRUD operations

5. **api/**: REST API and WebSocket
   - `routes.py`: REST endpoints
   - `websocket.py`: WebSocket connections
   - `schemas.py`: Request/response schemas

6. **scheduler/**: Background tasks
   - `tasks.py`: Scheduled tasks using APScheduler

## API Endpoints

### Chat
- `POST /api/chat` - Send message and get response
- `GET /api/conversations` - List conversations
- `POST /api/conversations` - Create conversation
- `WebSocket /ws` - Real-time chat connection

## Data Models

### User
- Email, username, preferences, created_at

### Conversation
- Title, created_at, messages

### Message
- Content, role (user/assistant), timestamp

## Security

- API key management for external services
- User authentication and authorization
- End-to-end encryption for sensitive data
- Secure credential storage

## Deployment

- Docker containerization
- Docker Compose for local development
- Kubernetes ready (with additional config)
- PostgreSQL database
