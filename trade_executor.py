# trade_executor.py - Trade Execution Logic
import requests
import json
import time
import logging
from auth import Auth
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradeExecutor:
    def __init__(self):
        self.auth = Auth()
        self.auth.load_tokens()
        self.access_token = self.auth.access_token
        self.base_url = os.getenv('BASE_URL')
        self.api_key = os.getenv('API_KEY')

    def execute_trade(self, symbol, quantity, order_type):
        endpoint = f'{self.base_url}/placeOrder'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        order_data = {
            "symbol": symbol,
            "quantity": quantity,
            "order_type": order_type,
            "api_key": self.api_key
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(order_data))
            if response.status_code == 200:
                logging.info(f"Trade Executed Successfully: {response.json()}")
                return response.json()
            else:
                logging.error(f"Trade Execution Failed: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            logging.error(f"Error Executing Trade: {str(e)}")
            return None

if __name__ == "__main__":
    executor = TradeExecutor()

    while True:
        # Replace with your trading logic and symbols
        executor.execute_trade(symbol="NIFTY22JUL20000CE", quantity=1, order_type="BUY")
        time.sleep(1)
