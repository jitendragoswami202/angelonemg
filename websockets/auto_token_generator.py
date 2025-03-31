# auto_token_generator.py

import requests
import json
import os
from dotenv import load_dotenv
from utils import log_message

load_dotenv()

API_KEY = os.getenv('API_KEY')
CLIENT_CODE = os.getenv('CLIENT_CODE')
PASSWORD = os.getenv('PASSWORD')
TOTP_SECRET = os.getenv('TOTP_SECRET')
BASE_URL = os.getenv('BASE_URL')


def generate_totp(secret):
    import pyotp
    totp = pyotp.TOTP(secret)
    return totp.now()

def generate_access_token():
    totp = generate_totp(TOTP_SECRET)
    url = f"{BASE_URL}/login"
    payload = {
        "api_key": API_KEY,
        "client_code": CLIENT_CODE,
        "password": PASSWORD,
        "totp": totp
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            result = response.json()
            access_token = result.get('data', {}).get('access_token')
            if access_token:
                log_message("Access token generated successfully.")
                return access_token
            else:
                log_message("Failed to retrieve access token from response.")
        else:
            log_message(f"Failed to generate access token: {response.status_code} {response.text}")
    except Exception as e:
        log_message(f"Error generating access token: {e}")
    return None


if __name__ == "__main__":
    token = generate_access_token()
    if token:
        log_message(f"Access Token: {token}")
    else:
        log_message("Failed to generate access token.")
