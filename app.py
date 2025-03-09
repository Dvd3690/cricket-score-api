from flask import Flask, jsonify  
import requests  

app = Flask(__name__)  

API_KEY = "22e06cd0-331e-4af4-ba7f-b4e2f0260520"  
MATCH_ID = "445e4eac-2a9c-4810-afd4-77197aeed7c3"  

@app.route("/")  
def get_score():  
    url = f"https://api.cricketdata.org/match/{MATCH_ID}"  
    headers = {"X-Api-Key": API_KEY}  

    try:  
        response = requests.get(url, headers=headers)  
        response.raise_for_status()  # raises error if request fails  
        data = response.json()  

        if "status" in data and data["status"] == "success":  
            match = data.get("match", {})  
            team1 = match.get("team_1", {}).get("name", "Unknown")  
            team2 = match.get("team_2", {}).get("name", "Unknown")  
            score1 = match.get("team_1", {}).get("scores", "0/0")  
            score2 = match.get("team_2", {}).get("scores", "0/0")  
            overs1 = match.get("team_1", {}).get("overs", "0.0")  
            overs2 = match.get("team_2", {}).get("overs", "0.0")  
            status = match.get("status_note", "No update")  

            return f"{team1} {score1} ({overs1} ov) - {team2} {score2} ({overs2} ov) | {status}"  

        return "match data not available yet"  

    except requests.exceptions.RequestException as e:  
        return f"error fetching score: {e}"  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
