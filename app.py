from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Root endpoint
@app.route("/")
def home():
    return jsonify({
        "info": "Cloud API is running",
        "endpoint": "/hello"
    })

# /hello endpoint
@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Render!",
        "status": "success",
        "timestamp": datetime.now().isoformat()
    })

# /time endpoint (optional, can keep for testing)
@app.route("/time")
def get_time():
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    })

# /health endpoint (optional)
@app.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "online",
        "timestamp": datetime.now().isoformat()
    })
