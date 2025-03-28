import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AngelOneAuth:
    def __init__(self, api_key, api_secret, redirect_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.redirect_url = redirect_url
        self.access_token = None
        self.feed_token = None

    def generate_access_token(self, request_token):
        try:
            logging.info('Generating access token...')
            url = 'https://api.angelbroking.com/rest/authenticate'
            payload = {
                'api_key': self.api_key,
                'api_secret': self.api_secret,
                'redirect_url': self.redirect_url,
                'request_token': request_token
            }
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

            if data['status'] == 'success':
                self.access_token = data['data']['access_token']
                self.feed_token = data['data']['feed_token']
                logging.info('Access token generated successfully.')
            else:
                logging.error(f'Error generating access token: {data}')
                return False
        except requests.RequestException as e:
            logging.error(f'Request error while generating access token: {str(e)}')
            return False
        return True

    def get_access_token(self):
        return self.access_token

    def get_feed_token(self):
        return self.feed_token
        
