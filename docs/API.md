# API Documentation

## Base URL

```
http://localhost:8000/api
```

## Authentication

Currently using API keys. Full JWT authentication coming soon.

## Endpoints

### Health Check

```
GET /health
```

Returns: `{"status": "healthy"}`

### Chat

#### Send Message

```
POST /chat
Content-Type: application/json

{
  "content": "Hello, how are you?",
  "conversation_id": 1
}
```

Response:
```json
{
  "id": 123,
  "role": "assistant",
  "content": "I'm doing great! How can I help?",
  "created_at": "2024-01-01T12:00:00Z"
}
```

### Conversations

#### List Conversations

```
GET /conversations
```

Response:
```json
[
  {
    "id": 1,
    "title": "General Chat",
    "created_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Create Conversation

```
POST /conversations
Content-Type: application/json

{
  "title": "Project Discussion"
}
```

Response:
```json
{
  "id": 2,
  "title": "Project Discussion",
  "created_at": "2024-01-01T12:00:00Z"
}
```

## WebSocket

Real-time chat via WebSocket:

```
WS ws://localhost:8000/ws
```

### Example (JavaScript)

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onopen = () => {
  ws.send('Hello from WebSocket!');
};

ws.onmessage = (event) => {
  console.log('Message:', event.data);
};
```

## Error Handling

All errors return appropriate HTTP status codes with error messages:

```json
{
  "detail": "Error message"
}
```

Common status codes:
- 200: Success
- 400: Bad request
- 401: Unauthorized
- 404: Not found
- 500: Server error
