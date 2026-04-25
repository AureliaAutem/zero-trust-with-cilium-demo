from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "http://clientdb:9000")

@app.route("/login")
def login():
    return jsonify({"message": "You have been logged successfully"})

@app.route("/user/list")
def user_list():
    try:
        # Call internal DB service
        res = requests.get(f"{DB_HOST}/user/list")
        return jsonify({
            "source": "clientapi",
            "data": res.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(host="0.0.0.0", port=8000)