import logging
import requests
import json

class OrderManager:
    def __init__(self, api_key, access_token, base_url):
        self.api_key = api_key
        self.access_token = access_token
        self.base_url = base_url

    def place_order(self, order_type, symbol, quantity, price):
        try:
            endpoint = f'{self.base_url}/order/place'
            headers = {
                'Content-Type': 'application/json',
                'X-Api-Key': self.api_key,
                'Authorization': f'Bearer {self.access_token}'
            }

            order_data = {
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
                'order_type': order_type
            }

            response = requests.post(endpoint, headers=headers, data=json.dumps(order_data))
            result = response.json()

            if response.status_code == 200 and result.get('status') == 'success':
                logging.info(f'{order_type} Order placed successfully: {result}')
                return result
            else:
                logging.error(f'Failed to place order: {result}')
                return None
        except Exception as e:
            logging.error(f'Error in placing order: {str(e)}')
            return None

    def check_order_status(self, order_id):
        try:
            endpoint = f'{self.base_url}/order/status/{order_id}'
            headers = {
                'X-Api-Key': self.api_key,
                'Authorization': f'Bearer {self.access_token}'
            }

            response = requests.get(endpoint, headers=headers)
            result = response.json()

            if response.status_code == 200:
                logging.info(f'Order status retrieved successfully: {result}')
                return result
            else:
                logging.error(f'Failed to retrieve order status: {result}')
                return None
        except Exception as e:
            logging.error(f'Error in retrieving order status: {str(e)}')
            return None
            
