from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

@app.get("/me")
def get_profile():
    cat_facts = requests.get("https://catfact.ninja/fact")
    cat_response = cat_facts.json().get("fact")

    response = {
        "status": "success",
        "user": {
            "email": "emmanueldenis560@gmail.com",
            "name": "Emmanuel Denis",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.utcnow().isoformat(),
        "fact": cat_response
    }
    
    return response