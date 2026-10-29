# Integrations Guide

## Gmail Integration

### Setup

1. Get credentials from Google Cloud Console
2. Download service account JSON
3. Add to backend/.env:

```
GOOGLE_SERVICE_ACCOUNT_JSON=path/to/credentials.json
```

### Features

- Read emails
- Send emails
- Label management

## Google Calendar Integration

### Setup

Similar to Gmail setup with Google Cloud Console.

### Features

- View events
- Create events
- Update events

## Slack Integration

### Setup

1. Create Slack App
2. Get Bot Token
3. Add to backend/.env:

```
SLACK_BOT_TOKEN=xoxb-your-token
SLACK_SIGNING_SECRET=your-secret
```

### Features

- Send messages
- Receive messages
- Read channel info

## Notion Integration

### Setup

1. Create Notion Integration
2. Get API key
3. Add to backend/.env:

```
NOTION_API_KEY=your-api-key
```

## Todoist Integration

### Setup

1. Get Todoist API key
2. Add to backend/.env:

```
TODOIST_API_KEY=your-api-key
```

## Home Assistant Integration

### Setup

1. Set up Home Assistant
2. Get API token
3. Add to backend/.env:

```
HOME_ASSISTANT_URL=http://localhost:8123
HOME_ASSISTANT_TOKEN=your-token
```

## Web Search

### Setup

Uses Google Search API (already configured with GOOGLE_API_KEY).
