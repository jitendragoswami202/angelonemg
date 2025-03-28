# auth.py - Handles login authentication and session token generation

import requests
import json
from config import API_KEY, CLIENT_ID, SECRET_KEY, LOGIN_URL

def generate_token():
    payload = {
        "clientcode": CLIENT_ID,
        "password": SECRET_KEY,
    }
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY
    }

    response = requests.post(LOGIN_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "success":
            print("✅ Authentication Successful!")
            return data["data"]["token"]
        else:
            print("❌ Authentication Failed:", data.get("message"))
    else:
        print("❌ API Error:", response.status_code)

    return None

if __name__ == "__main__":
    token = generate_token()
    print("Token:", token)
