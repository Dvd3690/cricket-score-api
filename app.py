from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "22e06cd0-331e-4af4-ba7f-b4e2f0260520"
MATCH_ID = "445e4eac-2a9c-4810-afd4-77197aeed7c3"
BASE_URL = f"https://api.cricketdata.org/match/{MATCH_ID}?apikey={API_KEY}"

@app.route("/")
def home():
    return "Cricket Score API is Running!"

@app.route("/match", methods=["GET"])
def get_match():
    try:
        response = requests.get(BASE_URL, timeout=5)
        data = response.json()

        return jsonify(data)  # show raw response

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "failed to fetch match data", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
    
