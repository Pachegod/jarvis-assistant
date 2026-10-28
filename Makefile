.PHONY: help install run schedule setup clean test docker-build docker-up docker-down

help:
	@echo "Jarvis Assistant - Available Commands"
	@echo "====================================="
	@echo ""
	@echo "make install      - Install Python dependencies"
	@echo "make run          - Run the assistant once"
	@echo "make schedule     - Start the scheduler (runs daily at 8:30 AM)"
	@echo "make setup        - Initial setup (install + create env)"
	@echo "make clean        - Remove cache and temporary files"
	@echo "make test         - Run tests (when available)"
	@echo ""
	@echo "Docker commands:"
	@echo "make docker-build - Build Docker image"
	@echo "make docker-up    - Start Docker container"
	@echo "make docker-down  - Stop Docker container"
	@echo ""

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "Dependencies installed successfully!"

run:
	@echo "Running Jarvis Assistant..."
	python -m src.main

schedule:
	@echo "Starting scheduler..."
	python -m src.scheduler

setup: install
	@echo "Setting up environment..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file - please update with your credentials"; \
	else \
		echo ".env file already exists"; \
	fi
	@echo "Setup completed!"

clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	@echo "Cleanup completed!"

test:
	@echo "Running tests..."
	pytest -v
	@echo "Tests completed!"

docker-build:
	@echo "Building Docker image..."
	docker-compose build
	@echo "Docker image built successfully!"

docker-up:
	@echo "Starting Docker container..."
	docker-compose up -d
	@echo "Docker container started! Check logs with: docker-compose logs -f"

docker-down:
	@echo "Stopping Docker container..."
	docker-compose down
	@echo "Docker container stopped!"

docker-logs:
	docker-compose logs -f

.DEFAULT_GOAL := help
