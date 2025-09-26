from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Configuration for OpenWebUI
OPENWEBUI_BASE_URL = os.getenv("OPENWEBUI_BASE_URL", "host.docker.internal:5000")

@app.route('/v1/models', methods=['GET'])
def get_models():
    auth_header = request.headers.get('Authorization')
    
    headers = {
        'Authorization': auth_header,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(f"{OPENWEBUI_BASE_URL}/api/models", headers=headers, timeout=30)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to retrieve models"}), response.status_code
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 502

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    auth_header = request.headers.get('Authorization')
    
    headers = {
        'Authorization': auth_header,
        'Content-Type': 'application/json'
    }
    
    data = request.get_json()
    
    openwebui_payload = {
        "model": data.get("model"),
        "messages": data.get("messages")
    }
    
    try:
        response = requests.post(f"{OPENWEBUI_BASE_URL}/api/chat/completions", headers=headers, json=openwebui_payload, timeout=1200)  # Increased to 120 seconds
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to get chat completion"}), response.status_code
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 502

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
