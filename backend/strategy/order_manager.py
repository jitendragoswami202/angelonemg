import os
import requests
from dotenv import load_dotenv

load_dotenv()

class OrderManager:
    def __init__(self):
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.api_key = os.getenv('API_KEY')
        self.base_url = 'https://api.angelbroking.com/rest/secure/angelbroking/order/v1/'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/json'
        }

    def place_order(self, order_data):
        url = self.base_url + 'placeOrder'
        response = requests.post(url, json=order_data, headers=self.headers)
        return response.json()

    def modify_order(self, order_id, order_data):
        url = self.base_url + f'modifyOrder/{order_id}'
        response = requests.put(url, json=order_data, headers=self.headers)
        return response.json()

    def cancel_order(self, order_id):
        url = self.base_url + f'cancelOrder/{order_id}'
        response = requests.delete(url, headers=self.headers)
        return response.json()


if __name__ == "__main__":
    order_manager = OrderManager()
    sample_order = {
        "symbol": "NSE:RELIANCE",
        "quantity": 1,
        "price": 2400,
        "orderType": "LIMIT",
        "productType": "INTRADAY",
        "duration": "DAY"
    }

    response = order_manager.place_order(sample_order)
    print(response)
