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

        if response.status_code != 200 or "error" in data:
            return jsonify({"error": "invalid match id or data not available"}), 404

        match_info = data.get("match", {})
        teams = match_info.get("teams", "TBC vs TBC")
        status = match_info.get("status", "No update")

        score_info = match_info.get("score", {})
        score = score_info.get("current", "Score not available")
        overs = score_info.get("overs", "N/A")
        wickets = score_info.get("wickets", "N/A")

        return jsonify({
            "match": teams,
            "status": status,
            "score": f"{score}/{wickets} in {overs} overs"
        })

    except requests.exceptions.RequestException:
        return jsonify({"error": "failed to fetch match data"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
