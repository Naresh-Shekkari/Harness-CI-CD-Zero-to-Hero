"""
Harness CI/CD Course - Episode 2
Simple Python Flask App
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Harness CI/CD Course!",
        "episode": 2,
        "project": "Python Flask App",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/info")
def info():
    return jsonify({
        "app": "Harness Course Python App",
        "version": "1.0.0",
        "framework": "Flask",
        "language": "Python"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
