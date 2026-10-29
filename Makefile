.PHONY: help install setup dev build deploy clean

help:
	@echo "Jarvis Assistant - Development Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make setup              Setup everything"
	@echo "  make install            Install all dependencies"
	@echo ""
	@echo "Backend:"
	@echo "  make backend-install    Install backend dependencies"
	@echo "  make backend-dev        Run backend dev server"
	@echo "  make backend-test       Run backend tests"
	@echo ""
	@echo "Frontend:"
	@echo "  make frontend-install   Install frontend dependencies"
	@echo "  make frontend-dev       Run frontend dev server"
	@echo "  make frontend-build     Build frontend"
	@echo ""
	@echo "Mobile:"
	@echo "  make mobile-install     Install mobile dependencies"
	@echo ""
	@echo "CLI:"
	@echo "  make cli-install        Install CLI dependencies"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build       Build Docker images"
	@echo "  make docker-up          Start all services"
	@echo "  make docker-down        Stop all services"
	@echo "  make docker-logs        View Docker logs"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate         Run database migrations"
	@echo "  make db-reset           Reset database"
	@echo ""
	@echo "Full Stack:"
	@echo "  make dev                Run all dev servers"
	@echo "  make clean              Clean up cache and artifacts"

setup:
	@echo "Setting up Jarvis Assistant..."
	@echo "1. Installing backend..."
	cd backend && pip install -r requirements.txt
	@echo "2. Installing frontend..."
	cd frontend && npm install
	@echo "3. Installing CLI..."
	cd cli && pip install -r requirements.txt
	@echo "Setup complete! Run 'make dev' to start development"

install: setup

backend-install:
	cd backend && pip install -r requirements.txt

backend-dev:
	cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

backend-test:
	cd backend && pytest

frontend-install:
	cd frontend && npm install

frontend-dev:
	cd frontend && npm run dev

frontend-build:
	cd frontend && npm run build

mobile-install:
	cd mobile && npm install

cli-install:
	cd cli && pip install -r requirements.txt

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

db-migrate:
	cd backend && alembic upgrade head

db-reset:
	docker-compose down -v
	docker-compose up -d postgres
	@echo "Database reset. Run 'make db-migrate' to create tables"

dev:
	@echo "Starting Jarvis Assistant stack..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:5173"
	@echo "API Docs: http://localhost:8000/docs"
	@echo ""
	docker-compose up

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name node_modules -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name dist -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete!"
