# Setup Guide

## Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- Docker and Docker Compose
- PostgreSQL 15 or higher (if not using Docker)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant
```

### 2. Environment Setup

Copy `.env.example` to `.env` in each directory:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
cp mobile/.env.example mobile/.env
```

### 3. Configure API Keys

Edit the `.env` files and add your API keys:

- `CLAUDE_API_KEY`: Get from https://console.anthropic.com
- `GOOGLE_API_KEY`: Get from Google Cloud Console
- Database credentials

### 4. Install Dependencies

**Option A: Using Make (Recommended)**

```bash
make setup
```

**Option B: Manual Installation**

```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install

# Mobile
cd mobile
npm install

# CLI
cd cli
pip install -r requirements.txt
```

### 5. Database Setup

Using Docker Compose:

```bash
docker-compose up -d postgres
```

Or install PostgreSQL locally:

```bash
# Create database
createdb jarvis_db

# Apply migrations
cd backend
alembic upgrade head
```

## Running the Application

### Development Mode

```bash
# Start all services
make dev
```

Or manually:

```bash
# Terminal 1: Backend
cd backend
python -m uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm run dev

# Terminal 3: CLI (optional)
cd cli
python main.py --help
```

### Docker Compose

```bash
docker-compose up
```

Access:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Troubleshooting

### Database Connection Issues

```bash
# Check PostgreSQL is running
docker-compose ps

# Verify connection string in backend/.env
# Should be: postgresql://jarvis:jarvis_password@localhost:5432/jarvis_db
```

### API Key Errors

- Ensure `.env` file is in the correct directory
- Check API keys are valid and not expired
- Restart the backend after changing `.env`

### Port Already in Use

```bash
# Change ports in environment or docker-compose.yml
# Or kill existing processes:
lsof -ti:8000 | xargs kill -9
```

## Next Steps

1. Read [API.md](API.md) for API documentation
2. Check [INTEGRATIONS.md](INTEGRATIONS.md) for service setup
3. See [DEVELOPMENT.md](DEVELOPMENT.md) for development guidelines
