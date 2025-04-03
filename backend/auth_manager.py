import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AuthManager:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')
        self.totp = os.getenv('TOTP')
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.refresh_token = os.getenv('REFRESH_TOKEN')

    def refresh_auth_token(self):
        url = 'https://api.angelbroking.com/rest/auth/refresh'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.refresh_token}'
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.auth_token = data['data']['authToken']
            self.refresh_token = data['data']['refreshToken']

            # Save tokens to .env
            with open('.env', 'a') as f:
                f.write(f'\nAUTH_TOKEN={self.auth_token}')
                f.write(f'\nREFRESH_TOKEN={self.refresh_token}')

            print('Tokens refreshed successfully.')
        else:
            print('Failed to refresh tokens:', response.json())

    def get_auth_token(self):
        return self.auth_token


if __name__ == "__main__":
    auth_manager = AuthManager()
    auth_manager.refresh_auth_token()
