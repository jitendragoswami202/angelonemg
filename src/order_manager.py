# order_manager.py

import requests
import json
import time
from utils import log_message
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
API_URL = 'https://api.angelbroking.com/rest/'

class OrderManager:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'X-API-KEY': API_KEY
        }

    def place_order(self, symbol, qty, order_type, price=None):
        order_data = {
            "symbol": symbol,
            "qty": qty,
            "order_type": order_type,
            "price": price,
            "strategy": "market_making"
        }

        response = self.session.post(f'{API_URL}order/place', headers=self.headers, data=json.dumps(order_data))

        if response.status_code == 200:
            order_id = response.json().get('order_id')
            log_message(f'Order placed successfully: {order_id}')
            return order_id
        else:
            log_message(f'Failed to place order: {response.json()}')
            return None

    def cancel_order(self, order_id):
        response = self.session.delete(f'{API_URL}order/cancel/{order_id}', headers=self.headers)

        if response.status_code == 200:
            log_message(f'Order cancelled successfully: {order_id}')
        else:
            log_message(f'Failed to cancel order: {response.json()}')

    def get_order_status(self, order_id):
        response = self.session.get(f'{API_URL}order/status/{order_id}', headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            log_message(f'Failed to get order status: {response.json()}')
            return None


if __name__ == "__main__":
    manager = OrderManager()
    order_id = manager.place_order('NIFTY', 10, 'BUY')
    time.sleep(2)
    if order_id:
        status = manager.get_order_status(order_id)
        log_message(f'Order Status: {status}')
        manager.cancel_order(order_id)
