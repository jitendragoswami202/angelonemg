# order_manager.py - Handles placing, modifying, and canceling orders

import requests
import json
from config import API_KEY, CLIENT_ID
from auth import generate_token

# Angel One order endpoints
ORDER_URL = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/placeOrder"
MODIFY_URL = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/modifyOrder"
CANCEL_URL = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/cancelOrder"

# Generate authentication token
TOKEN = generate_token()

def place_order(symbol, quantity, order_type="LIMIT", price=22000, transaction_type="BUY"):
    """Places a new order."""
    payload = {
        "variety": "NORMAL",
        "tradingsymbol": symbol,
        "symboltoken": "26009",  # Replace with actual token
        "transactiontype": transaction_type,
        "exchange": "NSE",
        "ordertype": order_type,
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": price,
        "quantity": quantity
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY,
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(ORDER_URL, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Order Placed:", data)
        return data
    else:
        print("❌ Order Placement Failed:", response.text)
        return None

def modify_order(order_id, new_price):
    """Modifies an existing order."""
    payload = {
        "orderid": order_id,
        "price": new_price
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY,
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(MODIFY_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ Order Modified:", response.json())
    else:
        print("❌ Order Modification Failed:", response.text)

def cancel_order(order_id):
    """Cancels an order."""
    payload = {
        "orderid": order_id
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY,
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(CANCEL_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ Order Canceled:", response.json())
    else:
        print("❌ Order Cancellation Failed:", response.text)

if __name__ == "__main__":
    # Example: Place a test order
    place_order(symbol="NIFTY", quantity=50, order_type="LIMIT", price=22000, transaction_type="BUY")
