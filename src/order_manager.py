import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class OrderManager:
    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.order_url = 'https://api.angelbroking.com/rest/secure/order'

    def place_order(self, symbol, action, quantity, price):
        try:
            logging.info(f'Placing {action} order for {symbol}...')

            payload = {
                'api_key': self.api_key,
                'access_token': self.access_token,
                'symbol': symbol,
                'action': action,
                'quantity': quantity,
                'price': price
            }

            response = requests.post(self.order_url, json=payload)
            response.raise_for_status()

            data = response.json()

            if data['status'] == 'success':
                logging.info(f'{action} order for {symbol} placed successfully.')
                return data['order_id']
            else:
                logging.error(f'Error placing order: {data}')
                return None

        except requests.RequestException as e:
            logging.error(f'Request error during order placement: {str(e)}')
            return None
        except Exception as e:
            logging.error(f'Unexpected error: {str(e)}')
            return None


if __name__ == "__main__":
    order_manager = OrderManager(api_key="YOUR_API_KEY", access_token="YOUR_ACCESS_TOKEN")
    order_id = order_manager.place_order(symbol="RELIANCE", action="BUY", quantity=1, price=2500)
    logging.info(f'Order ID: {order_id}')
    
