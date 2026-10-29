# Development Guide

## Code Structure

- **Backend**: Python with FastAPI
- **Frontend**: TypeScript with React
- **Mobile**: TypeScript with React Native
- **CLI**: Python with Click

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/feature-name
```

### 2. Make Changes

- Write code following project conventions
- Add tests for new features
- Update documentation

### 3. Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### 4. Code Style

```bash
# Backend (using black and flake8)
black backend/
flake8 backend/

# Frontend (using prettier and eslint)
cd frontend
npm run lint
npm run format
```

### 5. Commit and Push

```bash
git add .
git commit -m "feat: description of changes"
git push origin feature/feature-name
```

### 6. Pull Request

Create PR on GitHub with:
- Clear description
- Link to related issues
- Screenshots if UI changes

## Adding Features

### Backend

1. Create module in appropriate directory
2. Add endpoints in `api/routes.py`
3. Add database models if needed
4. Add tests

### Frontend

1. Create components in `src/components/`
2. Create pages in `src/pages/`
3. Add API calls in `src/services/`
4. Add types in `src/types/`

### Mobile

Similar to frontend structure.

## Database Migrations

```bash
cd backend

# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Environment Variables

Never commit `.env` files. Use `.env.example` as template.

## Debugging

### Backend

```python
import logging
logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

### Frontend

Use React DevTools browser extension for debugging.

## Performance Optimization

- Use database indexes for frequently queried columns
- Implement pagination for large datasets
- Cache API responses where appropriate
- Minimize frontend bundle size

## Deployment

See infrastructure documentation for deployment procedures.

## Getting Help

- Check documentation in `docs/`
- Review existing code for examples
- Ask in project discussions
- Create issues for bugs
