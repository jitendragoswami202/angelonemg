import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
API_KEY = os.getenv('API_KEY')
REDIRECT_URL = os.getenv('REDIRECT_URL')

BASE_URL = 'https://smartapi.angelone.in'
LOGIN_URL = f'{BASE_URL}/publisher-login'
TOKEN_URL = f'{BASE_URL}/oauth/token'

class Auth:
    def __init__(self):
        self.access_token = None
        self.refresh_token = None

    def generate_auth_url(self):
        auth_url = f"{LOGIN_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&response_type=code"
        return auth_url

    def generate_access_token(self, auth_code):
        try:
            payload = {
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'grant_type': 'authorization_code',
                'code': auth_code,
                'redirect_uri': REDIRECT_URL
            }
            response = requests.post(TOKEN_URL, data=payload)
            data = response.json()

            if 'access_token' in data:
                self.access_token = data['access_token']
                self.refresh_token = data['refresh_token']
                self.save_tokens()
                print('Access Token Generated Successfully')
                return self.access_token
            else:
                print(f"Error generating access token: {data}")
                return None

        except Exception as e:
            print(f"Error in generate_access_token: {str(e)}")
            return None

    def refresh_access_token(self):
        try:
            payload = {
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token
            }
            response = requests.post(TOKEN_URL, data=payload)
            data = response.json()

            if 'access_token' in data:
                self.access_token = data['access_token']
                self.save_tokens()
                print('Access Token Refreshed Successfully')
                return self.access_token
            else:
                print(f"Error refreshing access token: {data}")
                return None

        except Exception as e:
            print(f"Error in refresh_access_token: {str(e)}")
            return None

    def save_tokens(self):
        with open('tokens.json', 'w') as f:
            json.dump({
                'access_token': self.access_token,
                'refresh_token': self.refresh_token
            }, f)

    def load_tokens(self):
        try:
            with open('tokens.json', 'r') as f:
                tokens = json.load(f)
                self.access_token = tokens.get('access_token')
                self.refresh_token = tokens.get('refresh_token')
        except FileNotFoundError:
            print('No tokens file found. Generate a new access token.')

if __name__ == "__main__":
    auth = Auth()
    auth_url = auth.generate_auth_url()
    print(f"Visit this URL to authorize the application: {auth_url}")

    
    auth_code = input("Enter the authorization code: ")
    auth.generate_access_token(auth_code)
