from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Render!",
        "status": "success"
    })

@app.route("/")
def home():
    return jsonify({
        "info": "Cloud API is running",
        "endpoint": "/hello"
    })
