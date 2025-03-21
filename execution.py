import time
import requests
from retrying import retry
from config import BASE_URL

class TradingAPI:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Client-Id": CLIENT_ID,
            "X-Secret-Key": SECRET_KEY,
        }

    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def place_order(self, order_data):
        response = requests.post(f"{BASE_URL}/order", headers=self.headers, json=order_data)
        response.raise_for_status()
        return response.json()

    def get_market_data(self, symbol, exchange):
        response = requests.get(f"{BASE_URL}/marketdata/{symbol}/{exchange}", headers=self.headers)
        data = response.json()
        return data.get("best_bid", data.get("ltp")), data.get("best_ask", data.get("ltp"))

api = TradingAPI()
