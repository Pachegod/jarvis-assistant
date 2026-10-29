# Jarvis Assistant

Personal AI assistant with voice control, multiple interfaces, and cloud sync.

## Features

- 🎤 **Voice Control**: Speech-to-Text and Text-to-Speech capabilities
- 💬 **Multi-Platform**: Web, Mobile, CLI, and Desktop interfaces
- 🧠 **AI-Powered**: Claude API integration for intelligent conversations
- 🔄 **Cloud Sync**: Synchronize data across all devices
- 📊 **Task Management**: Integrated task and productivity tools
- 📧 **Email & Calendar**: Gmail and Google Calendar integration
- 🏠 **Smart Home**: Control smart home devices
- 🔍 **Web Search**: Integrated web search capabilities
- 💾 **User Preferences**: Learn and adapt to user preferences
- 🔐 **Secure**: End-to-end encryption for sensitive data

## Technology Stack

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React 18 + TypeScript + Vite
- **Mobile**: React Native (Expo)
- **CLI**: Python + Click
- **AI**: Anthropic Claude API
- **Voice**: Google Cloud Speech-to-Text & Text-to-Speech
- **Infrastructure**: Docker + Docker Compose

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant

# Setup everything
make setup

# Start development
make dev
```

### Development

- **Backend**: `make backend-dev` (http://localhost:8000)
- **Frontend**: `make frontend-dev` (http://localhost:5173)
- **API Docs**: http://localhost:8000/docs
- **CLI**: `python -m cli --help`

## Project Structure

```
jarvis-assistant/
├── backend/          # FastAPI backend
├── frontend/         # React web interface
├── mobile/           # React Native mobile app
├── cli/              # Command-line interface
└── docs/             # Documentation
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md) - System design and architecture
- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [API Documentation](docs/API.md) - REST API reference
- [Integrations](docs/INTEGRATIONS.md) - External service integrations
- [Development](docs/DEVELOPMENT.md) - Developer guide

## Contributing

See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for contribution guidelines.

## License

MIT License - see LICENSE file for details

## Contact

For questions and support, open an issue on GitHub.
