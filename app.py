from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "22e06cd0-331e-4af4-ba7f-b4e2f0260520"
BASE_URL = "https://api.cricketdata.org/match/"

@app.route("/match", methods=["GET"])
def get_match():
    match_id = request.args.get("id")
    if not match_id:
        return jsonify({"error": "match id required"}), 400

    url = f"{BASE_URL}{match_id}?apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code != 200 or "error" in data:
            return jsonify({"error": "invalid match id or data not available"}), 404

        # extract match details
        match_info = data.get("match", {})
        teams = match_info.get("teams", "TBC vs TBC")
        status = match_info.get("status", "No update")
        
        # extract score details
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
    app.run(debug=True)
    
