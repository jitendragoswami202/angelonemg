import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class OrderManager:
    def __init__(self, api_key, api_secret, access_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.base_url = 'https://api.angelbroking.com/rest/order/place'

    def place_order(self, symbol, action, quantity):
        try:
            logging.info(f'Placing {action} order for {quantity} units of {symbol}')

            payload = {
                'symbol': symbol,
                'action': action,
                'quantity': quantity,
                'api_key': self.api_key,
                'access_token': self.access_token
            }

            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()

            data = response.json()
            if data['status'] == 'success':
                logging.info(f'Order placed successfully: {data}')
                return True
            else:
                logging.error(f'Error placing order: {data}')
                return False

        except requests.RequestException as e:
            logging.error(f'Request error while placing order: {str(e)}')
            return False
        except Exception as e:
            logging.error(f'Unexpected error: {str(e)}')
            return False
            
