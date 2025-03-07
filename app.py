import requests
from flask import Flask, request
import time  # to add timestamp

app = Flask(__name__)

API_KEY = "22e06cd0-331e-4af4-ba7f-b4e2f0260520"
MATCH_ID = "c57dc00a-7070-4068-8869-80c40dbbd009"

@app.route("/")
def get_score():
    timestamp = int(time.time())  # current time in seconds
    url = f"https://api.cricapi.com/v1/match_info?apikey={API_KEY}&id={MATCH_ID}&t={timestamp}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and data["data"]:
        match = data["data"]
        score = match.get("score", [])

        if len(score) >= 2:
            score1 = f"{score[0]['inning']} {score[0]['r']}/{score[0]['w']} ({score[0]['o']} ov)"
            score2 = f"{score[1]['inning']} {score[1]['r']}/{score[1]['w']} ({score[1]['o']} ov)"
            result = f"{score1} vs {score2} - {match['status']}"
        else:
            result = f"{match['teams'][0]} vs {match['teams'][1]} - {match['status']} (Score not available)"
    else:
        result = "Match data not available"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
