# trade_executor.py

import requests
import json
import time
from utils import log_message
from dotenv import load_dotenv
import os

load_dotenv()

class TradeExecutor:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.api_url = "https://api.angelone.in"

    def place_order(self, symbol, qty, order_type, price=None):
        order_data = {
            "symbol": symbol,
            "qty": qty,
            "order_type": order_type,
            "price": price,
            "api_key": self.api_key,
            "access_token": self.access_token
        }

        response = requests.post(f"{self.api_url}/orders", json=order_data)

        if response.status_code == 200:
            log_message(f"Order placed successfully: {response.json()}")
            return response.json()
        else:
            log_message(f"Order placement failed: {response.text}")
            return None

    def cancel_order(self, order_id):
        response = requests.delete(f"{self.api_url}/orders/{order_id}", headers={
            "api_key": self.api_key,
            "access_token": self.access_token
        })

        if response.status_code == 200:
            log_message(f"Order cancelled successfully: {response.json()}")
        else:
            log_message(f"Order cancellation failed: {response.text}")

    def get_positions(self):
        response = requests.get(f"{self.api_url}/positions", headers={
            "api_key": self.api_key,
            "access_token": self.access_token
        })

        if response.status_code == 200:
            return response.json()
        else:
            log_message(f"Failed to fetch positions: {response.text}")
            return []

    def get_open_orders(self):
        response = requests.get(f"{self.api_url}/orders", headers={
            "api_key": self.api_key,
            "access_token": self.access_token
        })

        if response.status_code == 200:
            return response.json()
        else:
            log_message(f"Failed to fetch open orders: {response.text}")
            return []


if __name__ == "__main__":
    executor = TradeExecutor()
    positions = executor.get_positions()
    log_message(f"Positions: {positions}")
    orders = executor.get_open_orders()
    log_message(f"Open Orders: {orders}")
