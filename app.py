from flask import Flask, request  
import requests  

app = Flask(__name__)  

API_KEY = "22e06cd0-331e-4af4-ba7f-b4e2f0260520"  
MATCH_ID = "445e4eac-2a9c-4810-afd4-77197aeed7c3"  

@app.route("/")  
def get_score():  
    url = f"https://api.cricketdata.org/match/{MATCH_ID}"  
    headers = {"X-Api-Key": API_KEY}  
    response = requests.get(url, headers=headers)  
    data = response.json()  

    if "status" in data and data["status"] == "success":  
        try:  
            match = data["match"]  
            team1 = match["team_1"]["name"]  
            team2 = match["team_2"]["name"]  
            score1 = match["team_1"]["scores"]  
            score2 = match["team_2"]["scores"]  
            overs1 = match["team_1"]["overs"]  
            overs2 = match["team_2"]["overs"]  
            status = match["status_note"]  

            return f"{team1} {score1}/{overs1} - {team2} {score2}/{overs2} | {status}"  
        except KeyError:  
            return "score not available yet"  
    return "error fetching score"  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
