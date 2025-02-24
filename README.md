# OpenWebUI Proxy Server

## Overview

This proxy server translates requests from OpenAI-compatible endpoints to the OpenWebUI API, allowing seamless integration with applications designed for OpenAI APIs.

## Features
- **Seamless Integration**: Works with applications expecting OpenAI API responses.
- **Preserves Authorization**: Passes through the `Authorization` header for secure requests.
- **Timeout Handling**: Increased timeout settings to handle longer processing times.
- **Logging and Debugging**: Detailed logging for issue resolution.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/openwebui-proxy-server.git
   cd openwebui-proxy-server
   ```

2. **Install Dependencies**

   Ensure you have Python 3 and `pip` installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set OpenWebUI Base URL**

   Update the `OPENWEBUI_BASE_URL` in the `proxy_server.py` file to point to your OpenWebUI server.

   ```python
   OPENWEBUI_BASE_URL = "http://your-openwebui-url:3000"
   ```

2. **Run the Proxy Server**

   You can run the proxy server using Flask or Gunicorn for better performance.

   **Using Flask:**

   ```bash
   python proxy_server.py
   ```

   **Using Gunicorn (Recommended for Production):**

   ```bash
   gunicorn -w 1 -k gevent --timeout 300 proxy_server:app --bind 0.0.0.0:5001
   ```

## Usage

### Example Requests

#### GET /v1/models

```bash
curl -X GET http://localhost:5001/v1/models \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json"
```

#### POST /v1/chat/completions

```bash
curl -X POST http://localhost:5001/v1/chat/completions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "ytm-website",
    "messages": [{"role": "user", "content": "Why is the sky blue?"}]
}'
```

## Logging

Detailed logging is included to help diagnose and resolve issues. Logs are output to the console by default.

```bash
# Example log entry
DEBUG:Request to OpenWebUI models: {'Authorization': 'Bearer YOUR_API_KEY', 'Content-Type': 'application/json'}
DEBUG:Response from OpenWebUI models: 200 - {"models": ["model1", "model2"]}
```

## Contributing

We welcome contributions to improve the functionality and robustness of this proxy server. Here’s how you can contribute:

1. **Fork the Repository**

   ```bash
   git clone https://github.com/uwzis/openwebuiapi-proxy-service.git
   cd openwebuiapi-proxy-service
   ```

2. **Create a New Branch**

   ```bash
   git checkout -b feature/new-feature
   ```

3. **Make Your Changes**

4. **Commit and Push Your Changes**

   ```bash
   git add .
   git commit -m "Add new feature"
   git push origin feature/new-feature
   ```

5. **Create a Pull Request**

   Visit the repository on GitHub and create a pull request.
