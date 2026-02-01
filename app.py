from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Cloud API!",
        "endpoints": {
            "/hello": "GET - Returns a greeting",
            "/time": "GET - Returns current server time",
            "/health": "GET - API health check"
        },
        "instructions": "Add /hello, /time, or /health to the URL"
    })

@app.route('/hello')
def hello():
    return jsonify({
        "message": "Hello from the cloud! 🌩️",
        "status": "success",
        "service": "Flask API on Render/Railway"
    })

@app.route('/time')
def get_time():
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "timezone": "UTC",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "online",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)