# Jarvis Assistant - Project Context

Personal AI assistant with voice control, multiple interfaces, and cloud sync.

## Technology Stack

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React 18 + TypeScript + Vite
- **Mobile**: React Native (Expo)
- **CLI**: Python + Click + Rich
- **AI**: Claude API (Anthropic)
- **Voice**: Google Cloud Speech-to-Text + Text-to-Speech
- **Infrastructure**: Docker + Docker Compose

## Key Features

- 🎤 Voice + Text interaction
- 🔄 Local + Cloud sync
- 📱 Multi-platform (Web, Mobile, CLI, Desktop)
- 🧠 AI Conversational (Claude)
- 🏠 Smart Home Integration
- 📊 Task Management
- 📧 Email/Calendar Integration (Gmail, Google Calendar)
- 🔍 Web Search
- 💾 User Preferences Learning
- 🔐 Secure Credential Management

## Project Structure

```
jarvis-assistant/
├── backend/              # FastAPI + SQLAlchemy
├── frontend/             # React + TypeScript
├── mobile/               # React Native (Expo)
├── cli/                  # Python CLI
├── docs/                 # Documentation
├── docker-compose.yml    # Docker configuration
├── Makefile              # Build automation
└── CLAUDE.md             # This file
```

## Core Modules

### Backend (backend/app/)

- **core/**: AI, Memory, Preferences, Security
- **voice/**: STT, TTS, Audio Processing
- **integrations/**: Gmail, Slack, Notion, Todoist, etc.
- **database/**: Models, CRUD, Connections
- **api/**: Routes, WebSocket, Schemas
- **scheduler/**: Background Tasks

### Frontend (frontend/src/)

- **components/**: ChatInterface, VoiceControl, TaskDashboard, Sidebar
- **pages/**: Chat, Dashboard, Settings, Integrations
- **services/**: API, WebSocket, Voice
- **types/**: TypeScript interfaces

## API Endpoints

- `POST /api/chat` - Send message
- `GET /api/conversations` - List conversations
- `POST /api/conversations` - Create conversation
- `WebSocket /ws` - Real-time chat

## Getting Started

```bash
# Setup
make setup

# Development
make dev

# API Docs
http://localhost:8000/docs
```

## Important Notes

1. **Environment Variables**: Never commit `.env` files
2. **Database**: PostgreSQL required (Docker provided)
3. **API Keys**: Needed for Claude, Google services
4. **Architecture**: See docs/ARCHITECTURE.md for detailed design

## Development Workflow

1. Create feature branch: `git checkout -b feature/name`
2. Make changes
3. Test locally
4. Commit with clear messages
5. Create Pull Request

## Useful Commands

```bash
make help              # Show all available commands
make docker-up         # Start all services
make docker-down       # Stop all services
make backend-dev       # Run backend only
make frontend-dev      # Run frontend only
make db-migrate        # Apply database migrations
make clean             # Clean cache and artifacts
```

## Debugging

- Backend logs: `docker-compose logs backend`
- Frontend: Use React DevTools browser extension
- API: http://localhost:8000/docs (Swagger UI)

## Next Steps

- Read [docs/SETUP.md](docs/SETUP.md) for detailed setup
- Check [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for system design
- See [docs/API.md](docs/API.md) for API documentation
- Review [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for development guidelines
