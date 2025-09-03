# Ping Service

A simple Flask application that provides a ping service for employees to check network connectivity.

## Installation

```bash
pip install flask
```

## Usage

Run the application:
```bash
python app.py
```

The service will start on port 5001.

## API Endpoint

### GET /ping

Sends a ping request to a specified host.

**Parameters:**
- `host` (optional): The hostname or IP address to ping. Defaults to 'localhost' if not provided.

**Example:**
```
GET http://localhost:5001/ping?host=google.com
```

**Response:**
Returns a confirmation message indicating the ping was sent.

## Requirements

- Python 3.x
- Flask
- Unix-like operating system (for ping command)
