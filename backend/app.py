from flask import Flask, jsonify
import json, os

app = Flask(__name__)

@app.route("/api/courses")
def get_courses():
    if os.path.exists("courses.json"):
        with open("courses.json") as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route("/")
def home():
    return {"status": "API running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
