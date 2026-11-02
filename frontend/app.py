import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
API_GATEWAY_URL = os.environ.get("API_GATEWAY_URL", "http://localhost:5000/api")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    payload = {"name": name, "email": email, "message": message}
    try:
        response = requests.post(f"{API_GATEWAY_URL}/submit", json=payload, timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
